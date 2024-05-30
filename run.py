# from transformers import pipeline
# from flask import Flask, request, jsonify

# pipe = pipeline("text-generation", model="gpt2")

# app = Flask(__name__)

# @app.route('/post', methods=['POST'])
# def post_function():
#     data = request.json
#     generated_text = pipe(data.userMessage, max_length=100)
#     response = {
#         'message': 'Data received',
#         'data': generated_text
#     }
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sendMessage', methods=['POST'])
def post_function():
    data = request.json  # Parse the incoming JSON request
    user_message = data.get('userMessage')  # Extract the user message from the JSON data
    
    # Example response
    response = {
        'message': 'Data received',
        'data': 'userMessage123: ' + user_message  # Just echoing the received message for simplicity
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
