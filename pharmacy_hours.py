from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"student_number": 200590967})

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    
    # Extract user query parameters from Dialogflow
    parameters = query_result.get('parameters', {})
    pharmacy_name = parameters.get('pharmacy_name')

    # Dialogflow should provide a response based on its data
    fulfillment_text = query_result.get('fulfillmentText', 'I am not sure how to help with that.')

    return jsonify({'fulfillmentText': fulfillment_text})

if __name__ == '__main__':
    app.run(debug=True)
