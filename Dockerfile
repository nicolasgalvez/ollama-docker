# Use the official Ollama Docker image as the base image
FROM ollama/ollama:latest

# Install Python and dependencies
RUN apt-get update && apt-get install -y python3 python3-pip \
    && ln -s /usr/bin/python3 /usr/bin/python

# Override Ollama's default ENTRYPOINT
ENTRYPOINT ["/app/entrypoint.sh"]

# Set the working directory
WORKDIR /app

# Copy the application files (default behavior for deployment)
COPY src/ ./src/

# Define an optional volume (used only if mounted at runtime)
VOLUME ["/app/src"]

COPY entrypoint.sh /app/entrypoint.sh

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port
EXPOSE 5000

# Start the Ollama server in the background and pull the model
RUN ollama serve & sleep 2 && ollama pull ollama pull deepseek-r1:7b

# Expose the port for Flask
EXPOSE 5000

