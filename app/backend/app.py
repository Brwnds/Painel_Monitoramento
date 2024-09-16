from flask import Flask, jsonify, request, flash
import requests
from bs4 import BeautifulSoup
import urllib3
import sqlite3
import re

# Suprimindo os avisos de HTTPS não verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

def conectar_db():
    conectar = squite3.connect('clientes.db')
    return conectar

def check_links(links):
    results = []
    
    for link in links:
        try:
            # ignorando a verificação SSL
            response = requests.get(link, verify=False)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                iframe = soup.find('iframe', {'src': True})
                
                if iframe and "powerbi" in iframe['src']:
                    title_tag = soup.find('title')
                    painel_name = title_tag.text.strip() if title_tag else "Nome do painel não encontrado"
                    results.append({
                        'link': link,
                        'status': 'ativo',
                        'painel': painel_name,
                        'powerbi_link': iframe['src']
                    })
                else:
                    results.append({
                        'link': link,
                        'status': 'erro',
                        'painel': 'Sem link do Power BI encontrado'
                    })
            else:
                results.append({
                    'link': link,
                    'status': f'erro {response.status_code}',
                    'painel': 'Não acessível'
                })
        
        except requests.RequestException as e:
            results.append({
                'link': link,
                'status': 'falha',
                'painel': f'Erro ao acessar: {e}'
            })

    return results

@app.route('/check_links', methods=['POST'])
def api_check_links():
    links = request.json.get('links', [])
    if not links:
        return jsonify({'error': 'Nenhum link fornecido'}), 400

    results = check_links(links)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
