from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import os
<<<<<<< Updated upstream
from flask_sqlalchemy import SQLAlchemy
=======
from requests.packages.urllib3.exceptions import InsecureRequestWarning
>>>>>>> Stashed changes

# Ignora avisos de segurança
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Diretório da aplicação Flask e configuração da pasta estática
app_root = os.path.dirname(__file__)
static_folder_path = os.path.join(app_root, '..', 'frontend', 'dist')

app = Flask(__name__, static_folder=static_folder_path, static_url_path='')
CORS(app)

<<<<<<< Updated upstream
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

=======
# Função para verificar os links
>>>>>>> Stashed changes
def check_links(links):
    print(f"Verificando {len(links)} links...")  # Adicionando print para depuração
    result = []
    status_count = {
        "ativo": 0,
        "inativo": 0,
        "erro": 0,
        "falha": 0
    }

    for link in links:
        print(f"Verificando o link: {link}")  # Adicionando print para depuração
        try:
            # Verifica se o link é o problemático e marca como inativo diretamente
            if link == 'https://observatorio.aeb.gov.br/politica-espacial/instituicoes-do-setor-espacial-brasileiro':
                print(f"Link conhecido como inválido: {link}")  # Adicionando print para depuração
                result.append({"link": link, "status": "inativo", "motivo": "Link conhecido como inválido"})
                status_count["inativo"] += 1
                continue

            # Ignora a verificação SSL
            response = requests.get(link, verify=False)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                iframe = soup.find('iframe', {'src': True})

                if iframe and "powerbi" in iframe['src']:
                    print(f"Link ativo: {link}")  # Adicionando print para depuração
                    result.append({"link": link, "status": "ativo"})
                    status_count["ativo"] += 1
<<<<<<< Updated upstream

                    store_link_data(link, "ativo", painel_name, iframe['src'])

=======
>>>>>>> Stashed changes
                else:
                    print(f"Link inativo (sem Power BI): {link}")  # Adicionando print para depuração
                    result.append({"link": link, "status": "inativo"})
                    status_count["inativo"] += 1
            else:
                print(f"Erro ao acessar o link {link}, código de status: {response.status_code}")  # Adicionando print para depuração
                result.append({"link": link, "status": f"erro {response.status_code}"})
                status_count["erro"] += 1
        except requests.exceptions.RequestException as e:
            print(f"Falha ao verificar o link {link}, erro: {e}")  # Adicionando print para depuração
            result.append({"link": link, "status": "falha", "error": str(e)})
            status_count["falha"] += 1

    print("Verificação concluída.")  # Adicionando print para depuração
    return result, status_count

<<<<<<< Updated upstream
def store_link_data(link, status, painel_name, iframe_src):
    novo_resultado = ResultadoLink(link=link, status=status, painel=painel_name, iframe=iframe_src)
    db.session.add(novo_resultado)
    db.session.commit()

=======
# Rota para o index
>>>>>>> Stashed changes
@app.route("/")
def index():
    try:
        return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        print(f"Erro ao acessar o diretório estático: {str(e)}")
        return "Erro interno do servidor", 500

# Rota para verificar links
@app.route('/check_links', methods=['POST'])
def check_links_route():
    data = request.get_json()
    links = data.get('power_bi_links', [])
    
    print(f"Recebido {len(links)} links para verificação.")  # Adicionando print para depuração
    results, status_count = check_links(links)

    print("Resultados da verificação de links:", results)  # Adicionando print para depuração
    return jsonify({"results": results, "status_count": status_count})

# Servir arquivos estáticos
@app.route("/<path:filename>")
def serve_static(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {filename}")  # Adicionando print para depuração
        return "Arquivo não encontrado", 404

if __name__ == "__main__":
<<<<<<< Updated upstream
    with app.app_context():
        db.create_all()
=======
    print("Servidor iniciado...")  # Adicionando print para depuração
>>>>>>> Stashed changes
    app.run(debug=True)
