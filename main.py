import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


from flask import Flask, request, redirect
import twilio.twiml
import send_sms as send
session = {}
#The session object makes use of a secret key.
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "A0b1C3d4E5f6G7h8I9"
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
        if(body == 'PEACE'): 
            send.send_message(incoming, 'You quit.')
            if(incoming in unpaired):
                unpaired.remove(incoming)
                return
            elif (len(unpaired) == 0):
                send.send_message(outgoing, 'Your partner quit.')
                unpaired.append(outgoing)
	    else:
                send.send_message(outgoing, 'Your partner quit.')
                set_partner(outgoing, unpaired.pop(0))
            del session[incoming]
        elif(body == 'NEXT'):
	    if(incoming in unpaired):
		return
	    if(len(unpaired) == 0):
		unpaired.append(incoming)
		unpaired.append(outgoing)
                send.send_message(incoming, 'Waiting for next...')
                send.send_message(outgoing, 'Your partner moved on. Waiting for next...')
	    elif(len(unpaired) == 1):
                send.send_message(outgoing, 'Your partner moved on.')
		set_partner(outgoing, unpaired.pop())
		unpaired.append(incoming)
                send.send_message(incoming, 'Waiting for next...')
	    elif(len(unpaired) == 2):
                send.send_message(incoming, 'You left.')
                send.send_message(outgoing, 'Your partner left.')
		set_partner(outgoing, unpaired.pop())
		set_partner(incoming, unpaired.pop())
        
	elif not (incoming in unpaired):
	    send.send_message(outgoing, body)
    else:
	session[incoming] = [request.values.get('Body'), '']
        send.send_message(incoming, 'Welcome ' + request.values.get('Body') + ' to roulettechat. Please wait for the next available person.')
        if len(unpaired) == 0:
	    unpaired.append(incoming)
        else:
   	    set_partner(incoming, unpaired.pop(0))
    return ''
 
def set_partner(a, b):
    session[a][1] = b
    session[b][1] = a
    send_initial(a, b)

def send_partnerquit(outgoing):
    msg = 'Your partner has disconnected. Waiting for a new partner...'
    send.send_message(outgoing, msg)

def send_initial(incoming, outgoing):
    msg = 'You have been connected to a partner: '
    end = '.If you want to talk to someone else text NEXT. If you want to quit chatroulette type PEACE.'
    send.send_message(incoming, msg + session[outgoing][0] + end)
    send.send_message(outgoing, msg + session[incoming][0] + end)

if __name__ == "__main__": 
    app.run(debug=True)
