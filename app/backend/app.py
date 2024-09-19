from flask import Flask, send_from_directory, request, jsonify
import requests
from bs4 import BeautifulSoup
import urllib3
import os

# Suprimindo os avisos de HTTPS não verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'frontend', 'dist'), static_url_path='')

def check_links(links):
    result = []
    for link in links:
        try:
            response = requests.get(link, verify=False)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                iframe = soup.find('iframe', {'src': True})
                if iframe and "powerbi" in iframe['src']:
                    title_tag = soup.find('title')
                    painel_name = title_tag.text.strip() if title_tag else "Nome do painel não encontrado"
                    result.append({"link": link, "status": "ativo", "painel": painel_name, "iframe": iframe['src']})
                else:
                    result.append({"link": link, "status": "inválido"})
            else:
                result.append({"link": link, "status": f"erro {response.status_code}"})
        except requests.exceptions.RequestException as e:
            result.append({"link": link, "status": "falha", "error": str(e)})
    return result

@app.route("/")
def index():
    try:
        # Corrigindo o caminho para listar os arquivos no diretório estático
        files = os.listdir(app.static_folder)
        print(f"Conteúdo do diretório estático: {files}")  # Lista arquivos no diretório estático
        if 'index.html' in files:
            return send_from_directory(app.static_folder, 'index.html')
        else:
            print("Arquivo index.html não encontrado.")
            return "Arquivo index.html não encontrado", 404
    except Exception as e:
        print(f"Erro ao acessar o diretório estático: {str(e)}")
        return "Erro interno do servidor", 500

@app.route("/<path:filename>")
def serve_static(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filename}")
        return "Arquivo não encontrado", 404

@app.route("/check_links", methods=['POST'])
def check_links_route():
    data = request.get_json()
    links = data.get('links', [])
    if not links:
        return jsonify({"error": "Nenhum link fornecido"}), 400

    results = check_links(links)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
