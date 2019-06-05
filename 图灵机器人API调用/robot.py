import requests
import json

session =requests.session()

def robot(question):

    data_code = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": question
            },
        },
        "userInfo": {
            "apiKey": "f23f15871d604eed85de6ab42c4cec09",
            "userId": '454359'
        }
    }

    jsondata = json.dumps(data_code)

    url = 'http://openapi.tuling123.com/openapi/api/v2'

    connect_json = session.post(url,data=jsondata)

    connect = connect_json.json()

    print('R:'+ connect["results"][0]["values"]["text"])

while True:
    question = input('M：')
    robot(question)
    if question == 'bye':
        break


