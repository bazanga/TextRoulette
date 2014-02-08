from twilio.rest import TwilioRestClient

account_sid = "AC194d442b38cb4ff37c8516106d092d90"
auth_token = "105ec4bc266c188259ea6669338ef0de"
client = TwilioRestClient(account_sid, auth_token)

def send_message(number, message):
    message = client.sms.messages.create(body=message, to=number, from_="18458759296")
    print message.sid
