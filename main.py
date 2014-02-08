import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    resp = twilio.twiml.Response()
    resp.message("Hello, Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)