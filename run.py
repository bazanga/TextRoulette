from flask import Flask, session, request, redirect
import twilio.twiml

#The session object makes use of a secret key.
app = Flask(__name__)
app.config.from_object(__name__)

#The unpaired phone number
unpaired = 0

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    if(request.values.get('From') in session):   
        if unpaired == 0:
	    unpaired = request.values.get('From')
	    session[request.values.get('From')] = 0	
        else:
   	    session[request.value.get('From')] = unpaired
	    unpaired = 0
    else:
    
    resp = twilio.twiml.Response()
    resp.message("Hello, Monkey")
    return str(resp)

if __name__ == "__main__":
    app.secret_key = "A0zro0!!asdl?,whatthe?'
    app.run(debug=True)
