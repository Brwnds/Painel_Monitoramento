import requests
import certifi

def check_power_bi_links(url):
    try:
        response = requests.get(url, verify=certifi.where())
        soup = BeautifulSoup(response.text, 'html.parser')

        power_bi_links = soup.find_all('a', class_='powerbi-link')
        results = []

        if not power_bi_links:
            return f'Nenhum link do Power BI encontrado em: {url}'

        for link in power_bi_links:
            href = link.get('href')
            try:
                link_response = requests.get(href, verify=certifi.where())
                if link_response.status_code == 200:
                    results.append({'link': href, 'status': 'ativo'})
                else:
                    results.append({'link': href, 'status': 'inativo'})
            except requests.RequestException:
                results.append({'link': href, 'status': 'erro ao acessar'})

        return results

    except requests.RequestException as e:
        return f'Erro ao acessar a página: {url} - {str(e)}'
