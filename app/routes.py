from flask import render_template, jsonify
from app import app
from .utils import check_link_status

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check_links')
def check_links():
    site_url = "http://example.com"
    results = check_link_status(site_url)
    return jsonify(results)
