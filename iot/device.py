from abc import ABC, abstractmethod
from iot.message import MessageType

class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str):
        pass

    def status_update(self) -> str:
        return "Device status is okay"
