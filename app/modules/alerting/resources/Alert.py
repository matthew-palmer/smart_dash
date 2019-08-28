from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello from the dashboard",
                     from_='+',
                     to='+'
                 )

print(message.sid)
print(message)

