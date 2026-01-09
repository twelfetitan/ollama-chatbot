# Ollama Chatbot UI

Small web project that implements a **chatbot interface** powered by Ollama (Llama 3) and served with Flask.

## Features

- Chat-style interface rendered in `index.html`.
- Backend built with Flask (`app.py`).
- Stores the full conversation in memory and shows both user and bot messages.
- Uses Ollama with the `llama3` model to generate responses.

## Requirements

- Python 3.10+ installed.
- Ollama installed and running, with the `llama3` model pulled.
- Flask installed in your Python environment.

## How to set it up

1. **Install Python**
   - Download Python 3 from: https://www.python.org/downloads/ and install it (check “Add Python to PATH” during installation).

2. **Install Ollama and the Llama 3 model**
   - Download and install Ollama from: https://ollama.com/download
   - Open a terminal and pull the model:
     ```bash
     ollama pull llama3
     ```

3. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/ollama-chatbot-ui.git
   cd ollama-chatbot-ui
