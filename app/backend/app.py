from flask import Flask, send_from_directory
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
            return "Arquivo index.html não encontrado", 404
    except FileNotFoundError as e:
        print(f"Erro ao listar arquivos: {str(e)}")
        return "Erro interno do servidor", 500

@app.route("/<path:filename>")
def serve_static(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        return "Arquivo não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
