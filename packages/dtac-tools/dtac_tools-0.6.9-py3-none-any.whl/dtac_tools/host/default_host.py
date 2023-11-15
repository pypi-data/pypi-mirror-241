# default_host.py
import os
import queue
import sys
import json
import grpc
import traceback
import dtac_tools.host.plugin_pb2_grpc

from grpc import ssl_server_credentials
from urllib.parse import quote
from concurrent import futures
from .helpers.debug_sender import DebugSender
from .helpers.encryptor import RpcEncryptor
from .plugin_host import PluginHost
from .helpers.network import get_unused_tcp_port
from ..plugins.types import InputArgs, ReturnVal
from .plugin_pb2 import PluginRequest, PluginResponse, RegisterReply, PluginEndpoint, ReturnVal as ApiReturnVal, LogField, LogMessage


class DefaultPluginHost(PluginHost):
    def __init__(self, plugin, debug=False, debug_port=5678):
        self.plugin = plugin
        self.rpc_proto = "grpc"
        self.proto = "tcp"
        self.ip = "127.0.0.1"
        self.interface_version = 'plug_api_1.0'
        self.port = None
        self.route_map = {}
        self.encryptor = RpcEncryptor.new_encryptor()
        self.log_channel = None
        self.debug_sender = None
        if debug:
            self.debug_sender = DebugSender(debug_port)
            self.debug(f"PluginHost debugging enabled on port {debug_port}")
            self.debug(f"Plugin Name: {self.plugin.name()}")

    def debug(self, message):
        if hasattr(self, "debug_sender") and self.debug_sender is not None:
            self.debug_sender.write(message + "\n")

    def Register(self, request, context):
        try :
            params = {}
            if request.config is not None:
                self.debug(f"config: {request.config}")
                params["config"] = request.config

            if request.default_secure is not None:
                self.debug(f"default_secure: {request.default_secure}")
                params["default_secure"] = request.default_secure

            response = self.plugin.register(params)

            # build the route map
            for endpoint in response:
                self.route_map[endpoint.path] = endpoint

            return_eps = []
            for endpoint in response:
                api_ep = PluginEndpoint(
                    path = endpoint.path,
                    action = endpoint.action,
                    uses_auth = endpoint.uses_auth,
                    expected_args = "",
                    expected_body = "",
                    expected_output = "",
                )
                return_eps.append(api_ep)

            self.debug(f"response: {response}")
            return_val = RegisterReply(
                endpoints = return_eps,
            )
            return return_val
        except Exception as ex:
            self.debug(f"Exception: {ex}")
            self.debug(traceback.format_exc())


    def Call(self, request: PluginRequest, context):
        try:
            method = request.method
            request_args = request.input_args
            self.debug(f"method: {method}")
            self.debug(f"request_args: {request_args}")
            input = InputArgs.from_grpc(request_args)
            self.debug(f"input: {input}")
            function = self.route_map[method].function
            ret = function(input)
            self.debug(f"output: {ret}")

            return PluginResponse(
                id = 1234,
                return_val = ApiReturnVal(
                    headers = ret.headers,
                    params = ret.params,
                    value = ret.value_to_json(),
                ),
                error = "",
            )

        except Exception as ex:
            self.debug(f"Exception: {ex}")
            self.debug(traceback.format_exc())
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Internal error: {}'.format(ex))
            return PluginResponse()


    def LoggingStream(self, request, context):
        try:
            if self.plugin.log_channel is None:
                self.plugin.log_channel = queue.Queue(maxsize=4096)
        except Exception as ex:
            self.debug(f"Exception: {ex}")
            self.debug(traceback.format_exc())
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Internal error: {}'.format(ex))
            return PluginResponse()

        while True:
            try:
                msg = self.plugin.log_channel.get()
                yield msg
            except Exception as e:
                self.debug(f"Logging Exception: {e}")
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details('Logging error: {}'.format(e))
                break

    def serve(self):

        env_cookie = os.getenv("DTAC_PLUGINS")
        if env_cookie is None:
            print('============================ WARNING ============================')
            print('This is a DTAC plugin and is not designed to be executed directly')
            print('Please use the DTAC agent to load this plugin')
            print('==================================================================')
            sys.exit(-1)

        self.port = get_unused_tcp_port()

        # Check for certificate and key files passed via ENV variables
        cert = os.getenv("DTAC_TLS_CERT")
        key = os.getenv("DTAC_TLS_KEY")

        options = [
            f'enc={quote(self.encryptor.key_string())}',
            f'tls={True if cert is not "" and key is not "" else False}',
        ]



        print(f"CONNECT{{{{{self.plugin.name()}:{self.plugin.root_path()}:{self.rpc_proto}:{self.proto}:{self.ip}:{self.port}:{self.interface_version}:[{','.join(options)}]}}}}")
        sys.stdout.flush()



        # Create a gRPC server
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        # Check if both certificate and key are provided
        if cert and key:
            # Convert certificate and key strings into bytes
            certificate_chain = cert.encode('utf-8')
            private_key = key.encode('utf-8')

            # Create server SSL credentials
            server_credentials = ssl_server_credentials(
                [(private_key, certificate_chain)]
            )

            # Add secure port using credentials
            server.add_secure_port(f"[::]:{self.port}", server_credentials)
        else:
            # Add insecure port if no TLS credentials are provided
            server.add_insecure_port(f"[::]:{self.port}")

        dtac_tools.host.plugin_pb2_grpc.add_PluginServiceServicer_to_server(self, server)
        server.add_insecure_port(f"[::]:{self.port}")
        server.start()
        server.wait_for_termination()

    def get_port(self):
        return self.port