#!/bin/sh
set -e  # Exit immediately if a command fails

# Start Ollama in the background
ollama serve &

# Wait a few seconds to ensure Ollama is running
sleep 2

# Start Flask app
exec python src/app.py