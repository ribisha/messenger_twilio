

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from twilio.rest import Client
import pywhatkit as kit
import os
from django.conf import settings

#----------------------------------------------------------------------#
ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
TWILIO_WHATSAPP_NUMBER = settings.TWILIO_WHATSAPP_NUMBER

#-----------------------Main---------------------------------------------#

def index(request):
    if request.method == 'POST':
        message_content = request.POST.get('message', '').strip()
        message_type = request.POST.get('message_type', '').strip()

        if not message_content:
            return HttpResponse("Message content cannot be empty.")

        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        if message_type == 'person':
            recipient_number = request.POST.get('phone_number', '').strip()

            if not recipient_number:
                return HttpResponse("Recipient phone number is required.")

            try:
                template_message = "Helo, {}"
                message = client.messages.create(
                    from_=TWILIO_WHATSAPP_NUMBER,
                    body=f"{template_message.format(message_content)}",
                    to=f'whatsapp:{recipient_number}'
                )
                return HttpResponse(f"Message to person sent successfully! SID: {message.sid}")
            except Exception as e:
                return HttpResponse(f"Failed to send message to person: {str(e)}")

        elif message_type == 'group':
            group_id = request.POST.get('group_id', '').strip()

            if not group_id:
                return HttpResponse("Group ID is required.")

            try:
                now = datetime.now()
                kit.sendwhatmsg_to_group(
                    group_id,
                    message_content,
                    now.hour,
                    now.minute + 1
                )
                return HttpResponse("Message to group sent successfully!")
            except Exception as e:
                return HttpResponse(f"Failed to send message to group: {str(e)}")

        else:
            return HttpResponse("Invalid message type selected.")

    return render(request, 'messenger.html')

def need_help(request):
    return render(request, 'need_help.html')