from flask import Flask, session, request, redirect
import twilio.twiml
import send_sms as send

#The session object makes use of a secret key.
app = Flask(__name__)
app.config.from_object(__name__)

#The unpaired phone number
unpaired = []

#Function to make sure at most one person is unpaired
def setPairs()
    for x in range(0, len(unpaired)/2):
	session[unpaired[x * 2]][1] = unpaired[x + 1]
	session[unpaired[x * 2 + 1]][1] = unpaired[x]
	send_initial(unpaired[x*2], unpaired[x*2 + 1])
	unpaired.pop(x)
	unpaired.pop(x + 1)
       
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    if(len(unpaired) > 1):
	setPairs()
    incoming = request.values.get('From')
    #if this is a first-time request
    if(! incoming in session):   
        if len(unpaired) == 0:
	    unpaired.append(incoming)
	    session[incoming] = [request.values.get('Body')]	
        else:
	    outgoing = unpaired.pop()
   	    session[incoming] = [request.values.get('Body'),outgoing]
	    session[outgoing].append(incoming)
	    send_initial(outgoing, incoming)
    #already established partner (sending message)
    else:
    	ans = send.send_message(session[incoming][1], sessionrequest.value.get('Body'))
    #He wants to stop the convo
    if(ans = -1):
	session[incoming].pop()
	unpaired.append(incoming)
    if(ans = -2):

def send_initial(incoming, outgoing):
    msg = 'You have been connected to a partner ('
    send.send_message(incoming, msg + session[outgoing][1] + ')')
    send.send_message(outgoing, msg + session[incoming][1] + ')')

if __name__ == "__main__":
    app.secret_key = "A0zro0!!asdl?,whatthe?'
    app.run(debug=True)
