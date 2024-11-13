# Painel de Monitoramento

Este projeto é uma aplicação web para monitoramento de painéis do PowerBI, construída com **Flask** no backend e **Vue.js/Vite** no frontend.

## Visão Geral

A aplicação permite monitorar o status de diversos painéis PowerBI, exibindo se os painéis estão "ativos" ou "inativos" e retornando informações detalhadas sobre cada um deles.

## Estrutura do Projeto

- `backend/`: contém o código da API em Flask, responsável por processar as requisições e verificar os links dos painéis.
- `frontend/`: contém o código do frontend desenvolvido com Vue.js e Vite, responsável pela interface do usuário.

## Funcionalidades

- Checagem de status dos painéis PowerBI
- Exibição de painéis "ativos" e "inativos" em uma interface amigável
- Contador de painéis ativos e inativos
- Busca e filtragem de painéis

## Pré-Requisitos

- Python 3.7 ou superior
- Node.js e npm
- Bibliotecas Python: `Flask`, `Flask-CORS`, `requests`, `BeautifulSoup4`

## Configuração e Execução

### Backend (API Flask)

1. Navegue até o diretório do backend.
2. Instale as dependências do Python:

   ```bash
   pip install flask flask-cors requests beautifulsoup4
## Inicie o servidor Flask:

    python <nome_do_arquivo.py
    

## Frontend (Vue/Vite)

1. Navegue até o diretório do frontend.

2. Instale as dependências:
   ```bash
    npm install
3. Compile o frontend para produção:
    ```bash 
    npm run build
