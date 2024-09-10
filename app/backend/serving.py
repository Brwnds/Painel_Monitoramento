from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/check_links', methods=['POST'])
def check_links():
    links = request.json.get('links', [])
    results = []

    for link in links:
        try:
            response = requests.get(link)
            status = 'active' if response.status_code == 200 else 'inactive'
        except requests.RequestException:
            status = 'inactive'
        results.append({'link': link, 'status': status})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
