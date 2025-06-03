from twilio.twiml.messaging_response import MessagingResponse #imports message response 
from flask import Flask, request 
import os
import requests, random
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__) #innitialize the name of the app

@app.route("/", methods=["Post", "Get"])
def chatbot():
    
    inc_msg = request.form.get("Body", "").lower()

    resp = MessagingResponse()
    message= resp.message()
    #print(dir(message))

    if "cat" in inc_msg: 
        message.media("https://cataas.com/cat ")
    elif "quote" in inc_msg:
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        response = requests.get(api_url, headers={
    'X-Api-Key': os.environ.get('API-KEY')
    })
        if response.status_code == requests.codes.ok:
            #print(response.text)

            datalist = response.json()
            data = random.choice(datalist)
            # print(data)
            message.body(f'"Quote: {data["quote"]} - {data["author"]}')
        else:
            print("Error:", response.status_code, response.text)
    else: 
        message.body("I can only provide cat images and famous quotes. Type cat or quote.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True, port=5000)