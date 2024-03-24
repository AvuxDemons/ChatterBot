from flask import Flask, render_template, request, jsonify
from lib.bot import CustomChatBot

app = Flask(__name__) # Bikin Web Server

chatbot = CustomChatBot() # Bikin Object BOT
chatbot.train_default() # Training basic

# https://domain.com
@app.route('/', methods=['GET'])
def chatbot_chatting():
    return render_template('chatbot.html') # Render file html

# https://domain.com/training
@app.route('/training', methods=['GET'])
def chatbot_training():
    return render_template('train.html') # Render file html

# https://domain.com/chat
@app.route('/chat', methods=['POST'])
def chatbot_chat():
    user_input = request.json
    if user_input and 'user_input' in user_input:
        print(user_input['user_input'])
        response_statement = chatbot.chat(user_input['user_input'])
        response = {
            'confidence': response_statement.confidence if hasattr(response_statement, 'confidence') else None,
            'text': response_statement.text,
        }
        return jsonify(response=response)
    else:
        return jsonify(error='Invalid request data'), 400

# https://domain.com/train
@app.route('/train', methods=['POST'])
def chatbot_train():
    train_data = request.json.get('train_data')  # Use .get() method to safely get the value
    if train_data:
        chatbot.train(train_data)
        print("Training completed.")
        return jsonify(success=True)
    else:
        return jsonify(error='Invalid training data'), 400

if __name__ == '__main__':
    app.run(debug=True)