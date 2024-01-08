from flask import Flask, jsonify, request
from flask_cors import CORS
from helper.openai_api import text_completion



app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'OK'


@app.route('/dialogflow/es/receiveMessage', methods=['POST'])
def esReceiveMessage():
    try:
        data = request.get_json()
        query_result = data.get('queryResult')
        query_text = query_result.get('queryText')
        result = text_completion(query_text)
        print(result)

        if result['status'] == 1:
            return jsonify(
                {
                    'fulfillmentText': result['response']
                }
            )
        else:
            return jsonify(
                {
                    'fulfillmentText': "Couldn't fetch response for query: " + query_text
                }
            )
    except:
        print("an error occurred")
        pass
    return jsonify(
        {
            'fulfillmentText': 'Something went wrong.'
        }
    )