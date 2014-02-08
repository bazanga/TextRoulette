from twilio.rest import TwilioRestClient

##from_="+13473216937"
#account_sid = "AC00e3ac5173e7bd97b486deeb151b9eb9"
#auth_token = "53df96318d6c0d493c49d9bd32e826a6"
account_sid = "AC194d442b38cb4ff37c8516106d092d90"
auth_token = "105ec4bc266c188259ea6669338ef0de"
client = TwilioRestClient(account_sid, auth_token)

def send_message(number, message):
    message = client.messages.create(to=number,from_="+18458759296", body=message)


