import logging
from iot.service import IOTService
from iot.message import Message, MessageType
from iot.devices import HueLight, SmartSpeaker, Curtains
import time

# Configure logging
logging.basicConfig(level=logging.INFO)  # Set the logging level to INFO

def main():
    iot_service = IOTService()

    # Generate random IDs for devices
    hue_light_id = iot_service.generate_id(5)
    speaker_id = iot_service.generate_id(5)
    curtains_id = iot_service.generate_id(5)

    # Create instances of available devices
    hue_light = HueLight(hue_light_id)
    smart_speaker = SmartSpeaker(speaker_id)
    curtains = Curtains(curtains_id)

    # Register devices
    iot_service.register_device(hue_light, hue_light_id)
    iot_service.register_device(smart_speaker, speaker_id)
    iot_service.register_device(curtains, curtains_id)

    # Test devices
    iot_service.test_devices()

    # Create programs using dynamically generated IDs
    wake_up_program = [
        Message(device_id=hue_light.device_id, msg_type=MessageType.SWITCH_ON),
        Message(device_id=smart_speaker.device_id, msg_type=MessageType.PLAY_SONG),
        Message(device_id=curtains.device_id, msg_type=MessageType.OPEN)
    ]

    sleep_program = [
        Message(device_id=hue_light.device_id, msg_type=MessageType.SWITCH_OFF),
        Message(device_id=smart_speaker.device_id, msg_type=MessageType.SWITCH_OFF),
        Message(device_id=curtains.device_id, msg_type=MessageType.CLOSE)
    ]

    # Run programs
    iot_service.run_program(wake_up_program)
    time.sleep(2)  # Wait for 2 seconds
    iot_service.run_program(sleep_program)

    # Unregister devices and end the program
    for device_id in [hue_light_id, speaker_id, curtains_id]:
        iot_service.unregister_device(device_id)

if __name__ == "__main__":
    main()
