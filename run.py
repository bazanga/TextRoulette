from flask import Flask, session, request, redirect
import twilio.twiml
import send_sms as send

#The session object makes use of a secret key.
app = Flask(__name__)
app.config.from_object(__name__)

#The unpaired phone number
unpaired = 0

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    incoming = request.values.get('From')
    #if this is a first-time request
    if(! incoming in session):   
        if unpaired == 0:
	    unpaired = incoming
	    session[incoming] = [request.values.get('Body')]	
        else:
   	    session[incoming] = [request.values.get('Body'),unpaired]
	    session[unpaired].append(incoming)
	    send_message(unpaired, 'You have been connected to a partner (session[incoming][1])')
	    send_message(incoming, 'You have been connected to a partner (session[unpaired][1])')
	    unpaired = 0
    #already established partner (sending message)
    else:
    	send_message(session[incoming][1], sessionrequest.value.get('Body'))
    resp = twilio.twiml.Response()
    resp.message("Hello, Monkey")
    return str(resp)

def send_message():
    

if __name__ == "__main__":
    app.secret_key = "A0zro0!!asdl?,whatthe?'
    app.run(debug=True)
