from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
# Flask(__name__): cria a aplicação.
# request.get_json(): middleware interno do Flask que faz o parsing do corpo JSON.
# jsonify(): garante que a resposta seja enviada em formato JSON.
# app.run(...): inicia o servidor na porta 5000, acessível em http://127.0.0.1:5000/.