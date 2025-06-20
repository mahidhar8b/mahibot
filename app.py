from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Route to serve the HTML UI
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': '⚠️ Please enter a message.'}), 400

    # Change to your working local model (e.g., "tinyllama")
    model_name = "tinyllama"

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            headers={"Content-Type": "application/json"},
            json={
                "model": model_name,
                "messages": [{"role": "user", "content": user_message}],
                "stream": False
            }
        )
        data = response.json()

        # Extract assistant response properly
        messages = data.get("messages", [])
        for msg in reversed(messages):
            if msg.get("role") == "assistant":
                return jsonify({'response': msg.get("content", "🤖 (No reply)")})
        return jsonify({'response': "🤖 (No assistant reply found)"})

    except Exception as e:
        return jsonify({'response': f"⚠️ Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
