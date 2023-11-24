# iot_control/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from django.template import TemplateDoesNotExist

from .models import Device
from iot.service import IOTService
from iot.message import Message, MessageType

iot_service = IOTService()  # Initialize IOTService instance

def register_device(request):
    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        device_type = request.POST.get('device_type')
        device = Device(device_id=device_id, device_type=device_type)
        device.save()
        iot_service.register_device(device, device_id)
        return HttpResponse('Device registered successfully')

    return render(request, 'register_device.html')  # Render the register_device.html template

def send_message(request, device_id):
    if request.method == 'POST':
        message_type = request.POST.get('message_type')
        data = request.POST.get('data')
        message = Message(device_id=device_id, msg_type=message_type, data=data)
        device = Device.objects.get(device_id=device_id)
        iot_service.send_message(device, message)
        return HttpResponse('Message sent successfully')

    return render(request, 'send_message.html')  # Render the send_message.html template

def device_status(request, device_id):
    try:
        device = get_object_or_404(Device, device_id=device_id)
        iot_service = IOTService()  # Initialize IOTService instance here or globally as needed
        status = iot_service.get_device_status(device)
        return render(request, 'device_status.html', {'status': status})
    except Device.DoesNotExist:
        return HttpResponseServerError('Device does not exist')  # Handle Device.DoesNotExist exception
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template does not exist')  # Handle TemplateDoesNotExist exception
    except Exception as e:
        return HttpResponseServerError(f'An error occurred: {str(e)}')  # Handle other exceptions
