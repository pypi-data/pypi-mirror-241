import json
from ..host.plugin_pb2 import InputArgs as ApiInputArgs, ReturnVal as ApiReturnVal, StringList
from enum import Enum
from ..host.plugin_pb2 import LogLevel as apiLogLevel

# EndpointAction is an enum that represents the actions that the plugin can perform
class EndpointAction(Enum):
    ActionRead = "read"
    ActionWrite = "write"
    ActionDelete = "delete"
    ActionCreate = "create"

class LoggingLevel(Enum):
    LevelDebug = 0
    LevelInfo = 1
    LevelWarning = 2
    LevelError = 3
    LevelFatal = 4

    def to_api_level(self):
        if self == LoggingLevel.LevelDebug:
            return apiLogLevel.Debug
        elif self == LoggingLevel.LevelInfo:
            return apiLogLevel.INFO
        elif self == LoggingLevel.LevelWarning:
            return apiLogLevel.WARNING
        elif self == LoggingLevel.LevelError:
            return apiLogLevel.ERROR
        elif self == LoggingLevel.LevelFatal:
            return apiLogLevel.FATAL
        else:
            return apiLogLevel.ERROR

class LogMessage:
    def __init__(self, level, message, fields):
        self.level = level
        self.message = message
        self.fields = fields

class InputArgs:
    def __init__(self, headers=None, params=None, body=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        self.headers = headers
        self.params = params
        self.body = body

    def to_dict(self):
        return {
            "headers": self.headers,
            "params": self.params,
            "body": self.body.decode('utf-8') if self.body else None
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        body = data.get("body")
        if body is not None:
            body = body.encode('utf-8')
        return cls(
            headers=data.get("headers"),
            params=data.get("params"),
            body=body
        )

    @classmethod
    def from_dict(cls, data):
        body = data.get("body")
        if body is not None:
            body = body.encode('utf-8')
        return cls(
            headers=data.get("headers"),
            params=data.get("params"),
            body=body
        )

    @classmethod
    def from_grpc(cls, grpc_obj: ApiInputArgs):
        headers = {}
        # for key, value in grpc_obj.headers.items():
        #     headers[key] = value
        #
        params = {}
        # for key, value in grpc_obj.params.items():
        #     params[key] = value

        return cls(
            headers=headers,
            params=params,
            body=grpc_obj.body
        )

class ReturnVal:
    def __init__(self, headers=None, params=None, value=None):
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        self.headers = headers
        self.params = params
        self.value = value

    def value_to_json(self):
        # Convert the value attribute to a JSON string
        try:
            return json.dumps(self.value)
        except TypeError as e:
            # Handle the error if value is not serializable
            return str(e)

    def to_dict(self):
        return {
            "headers": self.headers,
            "params": self.params,
            "value": self.value
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_grpc(self):
        headers = {}
        for key, values in self.headers.items():
            headers[key] = StringList(values=values)

        params = {}
        for key, values in self.params.items():
            params[key] = StringList(values=values)

        return ApiReturnVal(
            headers=headers,
            params=params,
            value=self.value
        )

class PluginEndpoint:
    def __init__(self, function, path, action, uses_auth, expected_args=None, expected_body=None, expected_output=None):
        self.function = function
        self.function_name = function.__name__
        self.path = path
        self.action = action
        self.uses_auth = uses_auth
        self.expected_args = expected_args
        self.expected_body = expected_body
        self.expected_output = expected_output

    def to_dict(self):
        return {
            "function_name": self.function_name,
            "path": self.path,
            "action": self.action,
            "uses_auth": self.uses_auth,
            "expected_args": self.expected_args,
            "expected_body": self.expected_body,
            "expected_output": self.expected_output
        }

    def to_json(self):
        return json.dumps(self, default=lambda o: {k: v for k, v in o.__dict__.items() if v is not None and not callable(v)}, indent=4)