from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/check-links', methods=['GET'])
def check_links():
    urls = [
        'https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-da-loa-vigente',
        
        
    ]

    resultado = []

    for url in urls:
        result = check_power_bi_links(url)
        resultado.append({'url': url, 'result': result})

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
