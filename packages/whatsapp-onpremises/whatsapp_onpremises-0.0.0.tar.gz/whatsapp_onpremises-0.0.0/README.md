whatsapp_onpremises Python Module Documentation
Introduction

The whatsapp_onpremises Python module provides a simplified interface for interacting with the WhatsApp Cloud API. This module abstracts away the complexity of API calls, allowing users to easily send various types of messages, including text, images, audio, videos, documents, and media messages. It also includes methods for user authentication, media upload, and URL retrieval.
Installation

You can install the module using pip:

bash

pip install whatsapp-cloud-api

Usage

To use the module, import it into your Python script and create an instance of the Whatsapp class by providing the required parameters: stack_ip, username, and password.

python

from whatsapp_onpremises import Whatsapp

stack_ip = "your_whatsapp_stack_ip"
username = "your_username"
password = "your_password"

whatsapp = Whatsapp(stack_ip, username, password)

User Authentication

The module provides a method for user authentication and retrieving the bearer token.

python

bearer_token = whatsapp._authToken(username, password)

Uploading Media

You can upload media files using the uploadMedia method.

python

file_name = "example_image.jpg"
file_binary = b"binary_data"
mime_type = "image/jpeg"

media_id = whatsapp.uploadMedia(file_name, file_binary, mime_type)

Getting Media URL

Retrieve the URL of a media file using the get_media_url method.

python

media_id = "media_id"
media_url = whatsapp.get_media_url(media_id)

Sending Text Messages

Send text messages using the sendTextMessage method.

python

to = "recipient_phone_number"
message = "Hello, this is a text message."

response = whatsapp.sendTextMessage(to, message)

Sending Images

Send images using the sendImageMessage method.

python

to = "recipient_phone_number"
image_id_or_url = "image_id_or_url"

response = whatsapp.sendImageMessage(to, image_id_or_url)

Sending Audio Messages

Send audio messages using the sendAudioMessage method.

python

to = "recipient_phone_number"
audio_id_or_url = "audio_id_or_url"

response = whatsapp.sendAudioMessage(to, audio_id_or_url)

Sending Video Messages

Send video messages using the sendVideoMessage method.

python

to = "recipient_phone_number"
video_id_or_url = "video_id_or_url"

response = whatsapp.sendVideoMessage(to, video_id_or_url)

Sending Document Messages

Send document messages using the sendDocumentMessage method.

python

to = "recipient_phone_number"
document_id_or_url = "document_id_or_url"

response = whatsapp.sendDocumentMessage(to, document_id_or_url)

Sending Media Messages

Send media messages (images, audio, videos, and documents) using the sendMediaMessage method.

python

to = "recipient_phone_number"
media_type = "image"  # Replace with the desired media type
media_id_or_url = "media_id_or_url"

response = whatsapp.sendMediaMessage(to, media_type, media_id_or_url)

Sending Reactions

Send reactions to specific messages using the send_react_to_message method.

python

to = "recipient_phone_number"
reply_to_message_id = "message_id"
emoji = "👍"  # Replace with the desired emoji

response = whatsapp.send_react_to_message(to, reply_to_message_id, emoji)

Contribution

If you'd like to contribute or report issues, please submit a pull request or create an issue on the GitHub repository.
License

This module is released under the MIT License.
Disclaimer

This module is not officially affiliated with WhatsApp or Facebook. It's an independent project developed by @your_username. Please replace placeholders (your_whatsapp_stack_ip, your_username, your_password, etc.) with actual values when using the module.