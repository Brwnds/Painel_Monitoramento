import requests
from bs4 import BeautifulSoup

def check_link_status(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', href=True)
    
    status = {}
    for link in links:
        url = link['href']
        try:
            resp = requests.head(url)
            status[url] = resp.status_code
        except requests.RequestException:
            status[url] = 'Failed'

    return status
