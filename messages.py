import requests
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()

AUTHORIZATION = os.getenv('AUTHORIZATION') #CHANGE THE AUTHORIZATION OF YOUR DISCORD ACCOUN. CHANGE ALL OS.WHATEVER
COOKIE = os.getenv('COOKIE') # YOUR COOKIES FROM YOUR DISCORD ACCOUNT
URL = os.getenv('URL') # THE URL OF THE CHANNEL. MAKE SURE THAT IT INCLUDES THE CHANNEL ID

# URL to make the request to
url = URL

# Headers including Authorization and Cookie
headers = {
    "Authorization": AUTHORIZATION,
    "Cookie":  COOKIE,
    "Content-Type": "application/json"
}


# JSON payload
# Corrected payload
for i in range(1):

    payload = {
        "mobile_network_type": "unknown ",
        "content": ":skull: :moai: TOILET "+ str(i),
        "tts": False,
        "flags": 0
    }

        # Making a GET request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

            # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
