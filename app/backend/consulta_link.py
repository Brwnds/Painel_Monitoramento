import requests

def check_links(links):
    for link in links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                print(f"[OK] {link} está ativo.")
            else:
                print(f"[ERRO] {link} retornou status {response.status_code}.")
        except requests.exceptions.RequestException as e:
            print(f"[FALHA] Não foi possível acessar {link}: {e}")

if __name__ == "__main__":
    power_bi_links = [
        "https://app.powerbi.com/view?r=eyJrIjoiODA5MTQ5NDItNTAxMi00ZWQxLTkzOTctNTJkODczODczZDhjIiwidCI6IjU4Yjc0YTc1LTAwM2ItNDViZi04ZjQzLTgxMzNmNjE2NTBlMCJ9",
        "https://github.com/Brwnds/Painel_Monitoramento"
    ]
    
    check_links(power_bi_links)
