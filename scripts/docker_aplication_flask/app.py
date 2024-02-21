from flask import Flask

# instância do Flask
app = Flask(__name__)

# Definindo rota simples
@app.route("/")
def hello():
    return "Olá, mundo! Esta é a resposta da aplicação Flask."

if __name__ == "__main__":
    # Inicia a aplicação Flask
    app.run(debug=True)



