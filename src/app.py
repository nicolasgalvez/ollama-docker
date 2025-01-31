from flask import Flask, request, Response, stream_with_context
import ollama

app = Flask(__name__)

OLLAMA_MODEL = "deepseek-r1:7b"  # Change this to the model you want

def stream_ollama_response(user_message):
    """
    Generator function to stream Ollama's response chunk by chunk.
    """
    response = ollama.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": user_message}], stream=True)

    for chunk in response:
        if "message" in chunk:
            yield chunk["message"]["content"] + "\n"

@app.route("/chat", methods=["POST"])
def chat_with_ollama():
    data = request.get_json()
    if not data or "message" not in data:
        return {"error": "Message is required"}, 400

    user_message = data["message"]

    return Response(stream_with_context(stream_ollama_response(user_message)), content_type="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
