from twilio.rest import TwilioRestClient

account_sid = "AC00e3ac5173e7bd97b486deeb151b9eb9"
auth_token = "53df96318d6c0d49d9bd32e826a6"
client = TwilioRestClient(account_sid, auth_token)

def send_message(number, message):
    message = client.sms.messages.create(body=message, to=number, from_="+13473216937")
    print message.sid
