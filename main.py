import flask
from flask import request, Flask, jsonify
import logging
from flask_cors import CORS
import os
import json


app = Flask(__name__)
CORS(app)
app = Flask(__name__)

@app.post("/samplewh")
def sample_wh():
  data = request.get_json()
  print(f"data {data}")
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
                                "options": [
                                    { "text": "Option 1" },
                                    { "text": "Option 2" },
                                    { "text": "Option 3" }
                                ]
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
