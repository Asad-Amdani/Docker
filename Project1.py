from flask import Flask

app = Flask(__name__)

@app.route('/chatbot-services')
def chatbot_services():
    return "Chatbot Services is running"

@app.route('/chatbot-backend')
def chatbot_backend():
    return "Chatbot Services is running on Backend"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
