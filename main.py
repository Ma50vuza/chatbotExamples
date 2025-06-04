from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request 
import os
import requests
import random
from dotenv import load_dotenv

#usrDict = {}
#load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["POST"])
def chatbot():
        #user input 
    user_msg = request.values.get("Body", "").lower

        #creating an object of MessagingResponse
    response = MessagingResponse()

     #user query 
    q = user_msg

     #list to store 
    result = [1,2,3]
    i = 0
     # searching and storing 
    for i in result:
        
        result.append(i+1)

    #display results 
    msg = response.message("Welcome to the Pothole Reporter! Please describe where the pothole is located (e.g., street name, nearest intersection, landmark).")

    if result[i] == 0:
        msg = response.message("Welcome to the Pothole Reporter! Please describe where the pothole is located (e.g., street name, nearest intersection, landmark).")

    elif result[i] == 1:
        msg = response.message("Thank you! Now, please share your location by using WhatsApp's location sharing feature.")  

    elif result[i] == 2:
        msg = response.message("Got your location! Finally, please take and send a photo of the pothole.")
     
    else:
        msg = response.message("Thank you for reporting the pothole! Your report has been received and saved.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)