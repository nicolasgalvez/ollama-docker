from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

# Define the Ollama model to use
OLLAMA_MODEL = "llama3.2"  # Change this to the model you want to use

@app.route("/chat", methods=["POST"])
def chat_with_ollama():
    data = request.get_json()
    
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400
    
    user_message = data["message"]
    
    # Send the user message to Ollama
    response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": user_message}])
    
    return response.message.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
