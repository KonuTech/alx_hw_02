import logging
from iot.device import Device


logger = logging.getLogger(__name__)

def collect_diagnostics(device):
    logger.info("Connecting to diagnostics server.")
    status = device.status_update()
    logger.info(f"Sending status update {status} to server.")
