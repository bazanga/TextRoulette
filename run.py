from flask import Flask, session, request, redirect
import twilio.twiml
import send_sms as send

#The session object makes use of a secret key.
app = Flask(__name__)
app.config.from_object(__name__)

#The unpaired phone number
unpaired = []
       
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    incoming = request.values.get('From')
    #if this is not a first time request
    if(incoming in session):   
	outgoing = session[incoming][1]
	body = request.values.get('Body')
        #He wants to move to next convo
        if(body == 'END'):
	    del session[incoming]
	    if(len(unpaired) == 0):
		unpaired.append(outgoing)
	    else:
		set_partner(outgoing, unpaired.pop(0))
        else if(body = 'NEXT'):
	    if(len(unpaired) == 0):
		remove_partner(incoming)
		remove_partner(outgoing)
		unpaired.append(incoming)
		unpaired.append(outgoing)
	    else if(len(unpaired) == 1):
		remove_partner(incoming)
		set_partner(outgoing, unpaired.pop())
		unpaired.append(incoming)
	    else if(len(unpaired) == 2):
		set_partner(outgoing, unpaired.pop())
		set_partner(incoming, unpaired.pop())
	else:
	    send.send_message(outgoing, body)
    else:
	session[incoming] = [request.values.get('Body')]
        if len(unpaired) == 0:
	    unpaired.append(incoming)	
        else:
	    outgoing = unpaired.pop()
   	    set_partner(incoming, outgoing)
 
def set_partner(a, b):
    session[a][1] = b
    session[b][1] = a
    send_initial(a, b)

def remove_partner(a):
    session[a].pop()

def send_partnerquit(outgoing):
    msg = 'Your partner has disconnected. Waiting for a new partner...'
    send.send_message(outgoing, msg)

def send_initial(incoming, outgoing):
    msg = 'You have been connected to a partner ('
    send.send_message(incoming, msg + session[outgoing][1] + ')')
    send.send_message(outgoing, msg + session[incoming][1] + ')')

if __name__ == "__main__":
    app.secret_key = "A0zro0!!asdl?,whatthe?'
    app.run(debug=True)
