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
from transformers import pipeline
print("Running!")
pipe = pipeline("text-generation", model="gpt2")
app = Flask(__name__)

@app.route('/sendMessage', methods=['POST'])
def post_function():
    data = request.json  # Parse the incoming JSON request
    user_message = data.get('userMessage')  # Extract the user message from the JSON data
    generated_text = pipe(user_message, max_length=100)
    print(generated_text)
    response = {
        'message': 'Data received',
        'data': 'response: ' + generated_text
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

while True:
    cli_response = input("Enter command:\n")
    if cli_response.lower() == "exit" or cli_response.lower() == "quit":
        print("Exiting the program.")
        break