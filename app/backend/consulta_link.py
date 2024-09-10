import requests
from bs4 import BeautifulSoup
import urllib3

# Suprimindo os avisos de HTTPS não verificados
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_links(links):
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
                    
                    print(f"[OK] {link} está ativo. Painel: {painel_name}. Link do Power BI encontrado: {iframe['src']}")
                else:
                    print(f"[ERRO] {link} não contém um link válido de Power BI ou está com problemas.")
            else:
                print(f"[ERRO] {link} retornou status {response.status_code}.")
        
        except requests.exceptions.RequestException as e:
            print(f"[FALHA] Não foi possível acessar {link}: {e}")

if __name__ == "__main__":
    power_bi_links = [
        "https://observatorio.aeb.gov.br/politica-espacial/instituicoes-do-setor-espacial-brasileiro",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-da-loa-vigente",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/indicadores-do-orcamento-1",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-pnae-1",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-ppa",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/governanca/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/cooperacao-internacional/acordos-internacionais",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/licenciamento-e-normatizacao/indicadores-e-dados-do-licenciamento-e-normatizacao",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-capital-humano/explorador-de-dados-de-capital-humano",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/sistemas-espaciais/satelites/registro-de-satelites-brasileiros",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-desenvolvimento-tecnologico/tema-mapeamento-tecnologico/mapeamento-de-tecnologias-espaciais",
        "https://observatorio.aeb.gov.br/prosame/carteira-de-admissao",
        "https://observatorio.aeb.gov.br/prosame/carteira-de-qualificacao",
        "https://observatorio.aeb.gov.br/prosame/carteira-de-execucao",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/governanca/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031"
    ]
    check_links(power_bi_links)
