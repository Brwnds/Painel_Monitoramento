from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import urllib3
import os
from flask_sqlalchemy import SQLAlchemy

# Suprimindo os avisos de HTTPS não verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app_root = os.path.dirname(__file__)
static_folder_path = os.path.join(app_root, 'frontend', 'dist')

app = Flask(__name__, static_folder=static_folder_path, static_url_path='')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://localhost/seu_banco_de_dados?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ResultadoLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    painel = db.Column(db.String(255))
    iframe = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

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

                    store_link_data(link, "ativo", painel_name, iframe['src'])

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

def store_link_data(link, status, painel_name, iframe_src):
    novo_resultado = ResultadoLink(link=link, status=status, painel=painel_name, iframe=iframe_src)
    db.session.add(novo_resultado)
    db.session.commit()

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
