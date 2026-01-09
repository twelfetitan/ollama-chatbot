import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para guardar la conversación
conversacion = []

def preguntar_ollama(texto):
    result = subprocess.run(
        ["ollama", "run", "llama3", texto],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pregunta = request.form["pregunta"]
        respuesta = preguntar_ollama(pregunta)
        conversacion.append({"usuario": pregunta, "bot": respuesta})
    return render_template("index.html", conversacion=conversacion)

if __name__ == "__main__":
    app.run(debug=True)
