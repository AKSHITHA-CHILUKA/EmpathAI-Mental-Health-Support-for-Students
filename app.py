from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Gemini API key and endpoint
GEMINI_API_KEY= ""

GEMINI_ENDPOINT = 'https://api.gemini.com/v1/chat'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = get_gemini_response(user_input)
    return jsonify({'response': response})

def get_gemini_response(user_input):
    headers = {
        'Authorization': f'Bearer {GEMINI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'input': user_input
    }
    response = requests.post(GEMINI_ENDPOINT, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json().get('response', 'I am here to help!')
    else:
        return 'Sorry, I couldn’t process that.'

if __name__ == '__main__':
    app.run(debug=True)
