import json
import queue
import traceback

from pydantic import BaseModel
from typing import TypeVar, Type
from ..host.helpers.debug_sender import DebugSender
from .types import LoggingLevel, LogMessage
from ..host.plugin_pb2 import LogField as apiLogField, LogLevel as apiLogLevel, LogMessage as apiLogMessage

# Base Config class, this is used to help deserialize configuration options for plugins
class BaseConfig(BaseModel):
    pass


class PluginShared:
    @staticmethod
    def name() -> str:
        return "UnnamedPlugin"
    
    @staticmethod
    def root_path() -> str:
        return ""
    
    @staticmethod
    def serialize(v: object) -> str:
        return json.dumps(v)

class PluginBase(PluginShared):

    T = TypeVar("T", bound=BaseConfig)
    log_channel: queue.Queue = None

    def enable_debugging(self):
        self.debug_sender = DebugSender(5678)
        self.debug(f"Plugin debugging enabled on port {5678}")
        self.debug(f"Plugin Name: {self.name()}")

    def debug(self, message):
        if hasattr(self, "debug_sender") and self.debug_sender is not None:
            self.debug_sender.write(message + "\n")

    def load_config(self, config_json: str, config_class: Type[T]) -> T:
        return config_class.parse_raw(config_json)

    def register(self, args):
        raise NotImplementedError("this method must be implemented")

    def log(self, log_level: LoggingLevel, message: str, fields: dict):
        try:
            if self.log_channel is None:
                self.log_channel = queue.Queue(maxsize=4096)

            msg_fields = []
            for k, v in fields.items():
                msg_fields.append(apiLogField(key=k, value=v))

            log_message = apiLogMessage(level=log_level.to_api_level(), message=message, fields=msg_fields)
            self.log_channel.put(log_message)
        except Exception as ex:
            self.debug(f"Exception: {ex}")
            self.debug(traceback.format_exc())


    def name(self) -> str:
        return self.__class__.__name__