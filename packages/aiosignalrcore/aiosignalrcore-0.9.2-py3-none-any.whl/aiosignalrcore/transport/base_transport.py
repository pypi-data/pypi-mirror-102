from ..protocol.json_hub_protocol import JsonHubProtocol
from ..helpers import Helpers


class BaseTransport:
    def __init__(self, protocol=JsonHubProtocol(), on_message=None):
        self.protocol = protocol
        self._on_message = on_message
        self.logger = Helpers.get_logger()
        self._on_open = None
        self._on_close = None

    def on_open_callback(self, callback):
        self._on_open = callback
    
    def on_close_callback(self, callback):
        self._on_close = callback

    def start(self): # pragma: no cover
        raise NotImplementedError()

    def stop(self): # pragma: no cover
        raise NotImplementedError()
    
    def is_running(self): # pragma: no cover
        raise NotImplementedError()

    def send(self, message, on_invocation=None):  # pragma: no cover
        raise NotImplementedError()
