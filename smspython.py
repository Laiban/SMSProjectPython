import os
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC6c8d7b97cba45dbf7a9835318b6f8d12"
# Your Auth Token from twilio.com/console
auth_token  = "06a56e6f8703a49b8224312c88552aab"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12082169689",
    from_="+19034946697",
    body="Hello, Oya lets go!")

print(message.sid)