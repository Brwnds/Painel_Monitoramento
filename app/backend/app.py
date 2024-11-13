from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import urllib3
import os

# Suprimindo os avisos de HTTPS não verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app_root = os.path.dirname(__file__)
static_folder_path = os.path.join(app_root, 'frontend', 'dist')

app = Flask(__name__, static_folder=static_folder_path, static_url_path='')
CORS(app)

def check_links(links):
    result = []
    status_count = {
        "ativo": 0,
        "inválido": 0,
        "erro": 0,
        "falha": 0
    }
    
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
                    status_count["ativo"] += 1

                else:
                    result.append({"link": link, "status": "inválido"})
                    status_count["inválido"] += 1

            else:
                result.append({"link": link, "status": f"erro {response.status_code}"})
                status_count["erro"] += 1
        
        except requests.exceptions.RequestException as e:
            result.append({"link": link, "status": "falha", "error": str(e)})
            status_count["falha"] += 1
    
    return result, status_count

@app.route("/")
def index():
    try:
        print(f"Caminho para o diretório estático: {app.static_folder}")
        files = os.listdir(app.static_folder)
        if 'index.html' in files:
            return send_from_directory(app.static_folder, 'index.html')
        else:
            return "Arquivo index.html não encontrado", 404
    except Exception as e:
        print(f"Erro ao acessar o diretório estático: {str(e)}")
        return "Erro interno do servidor", 500

@app.route("/check_links", methods=['POST'])
def check_links_route():
    try:
        data = request.get_json()
        links = data.get('links', [])
        result, status_count = check_links(links)
        response = {
            "result": result,
            "status_count": status_count
        }
        return jsonify(response)
    except Exception as e:
        print(f"Erro ao processar a requisição: {str(e)}")
        return "Erro interno do servidor", 500

@app.route("/<path:filename>")
def serve_static(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        return "Arquivo não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)

