from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Obtenha o parâmetro "news" da URL
    news_param = request.args.get('news')

    # Verifique se o parâmetro "news" foi fornecido na URL
    if not news_param:
        return 'Por favor, forneça a URL do site como um parâmetro "news" na URL.'

    # Obtenha a chave de API da URL
    api_key = request.args.get('api_key', 'e3tkb21pbmlvOmxvY2FsaG9zdC5jb219fS17e2tleV91bml2ZXJzYWw6Y29udmVyc2FfZmlhZGF9fQ==')

    # Crie o corpo da solicitação com a chave de API
    data = {'api_key': api_key}

    # Faça a solicitação HTTP para a URL especificada, enviando a chave de API no corpo da solicitação
    response = requests.post(news_param, data=data)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Renderize o conteúdo da página na resposta do Flask
        return response.text
    else:
        return f'Erro ao fazer a solicitação: {response.status_code}'

if __name__ == '__main__':
    # Execute o aplicativo Flask na porta 777
    app.run(port=777)

