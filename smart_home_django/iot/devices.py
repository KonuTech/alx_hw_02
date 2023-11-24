import logging
from iot.device import Device
from iot.message import MessageType


logger = logging.getLogger(__name__)

class HueLight(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self):
        logger.info("Connecting Hue Light")

    def disconnect(self):
        logger.info("Disconnecting Hue Light")

    def send_message(self, message_type: MessageType, data: str):
        logger.info(f"Hue light handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "hue_light_status_ok"

class SmartSpeaker(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self):
        print("Connecting Smart Speaker")

    def disconnect(self):
        print("Disconnecting Smart Speaker")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Smart Speaker handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "smart_speaker_status_ok"

class Curtains(Device):
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self):
        print("Connecting Curtains")

    def disconnect(self):
        print("Disconnecting Curtains")

    def send_message(self, message_type: MessageType, data: str):
        print(f"Curtains handling message of type {message_type.name} with data [{data}]")

    def status_update(self) -> str:
        return "curtains_status_ok"
