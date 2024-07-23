import flask
from flask import request, Flask, jsonify
import logging
from flask_cors import CORS
import os
import json
import requests



app = Flask(__name__)
CORS(app)
app = Flask(__name__)
base_url = os.environ.get('ACCOUNTS_URL')

@app.post("/samplewh")
def sample_wh():
  data = request.get_json()
  print(f"data {data}")
  tag = data['fulfillmentInfo']['tag']
  if tag == "get-accounts":
    url = base_url + "/getAccounts?type=3"
    print(url)
    response = requests.get(url)
    getAccountsResponse = response.json()
    accounts = getAccountsResponse['accounts']

    options_array = []
    for account in accounts:
      print('0')
      options_array.append({"text": account['number']})
      print(account['number'])





  output = {
    'sessionInfo': {
      'parameters': {
        'userAuthenticated': 'y',
        }
      },
    "fulfillment_response": {
      "messages": [
        {
          "text": {
            "text": ["test"]
            }
        },
        {
          "payload": {
            "richContent": [
                        [
                            {
                                "type": "chips",
                                "options": options_array
                            }
                        ]
                    ]

          }

        }
      ]
    }
  }
  response_json = json.dumps(output)
  return response_json
  # return flask.jsonify({"results": "output"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
