import logging
import random
from iot.device import Device
from iot.diagnostics import collect_diagnostics 
# from iot.devices import HueLight, SmartSpeaker, Curtains

logger = logging.getLogger(__name__)

class IOTService:
    def __init__(self):
        self.devices = {}
        logger.info("IOTService instance created")

    def generate_id(self, length: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letters) for _ in range(length))
    
    def register_device(self, device: Device, device_id: str):
        device.connect()
        self.devices[device_id] = device
        logger.info(f"Device registered: ID - {device_id}")

    def unregister_device(self, device_id: str):
        if device_id in self.devices:
            self.devices[device_id].disconnect()
            del self.devices[device_id]
            logger.info(f"Device unregistered: ID - {device_id}")
        else:
            logger.warning(f"Device ID {device_id} not found for unregistering")

    def get_device(self, device_id: str):
        if device_id in self.devices:
            return self.devices[device_id]

    def run_program(self, messages):
        logger.info("=====RUNNING PROGRAM======")
        for message in messages:
            device = self.get_device(message.device_id)
            if device:
                logger.info(f"Current device status for ID {message.device_id}: {device.status_update()}")
                device.send_message(message.msg_type, message.data)
        logger.info("=====END OF PROGRAM======")

    def test_devices(self):
        logger.info("Start test devices")
        for device in self.devices.values():
            collect_diagnostics(device)
