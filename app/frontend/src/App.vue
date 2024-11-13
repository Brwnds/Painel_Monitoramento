<template>
  <div class="container">
    <div class="panel-monitoring">
      <h1>Painel de Monitoramento</h1>
      <div class="grid">
        <div v-for="panel in panels" :key="panel.link" class="card" :class="{ offline: panel.status === 'inactive' }">
          {{ panel.name }}
          <div class="circle" :class="{ blue: panel.status === 'active', red: panel.status === 'inactive' }">
            {{ panel.status === 'active' ? '✔' : '✖' }}
          </div>
        </div>
      </div>
      <div class="sidebar">
        <img src="./assets/Logo.png" alt="Logo">
        <input v-model="searchQuery" type="text" placeholder="Buscar...">
        <div class="status">
          <button class="online">
            Painéis Online
            <span class="status-count">{{ onlinePanels }}</span>
          </button>
          <button class="offline">
            Painéis Offlines
            <span class="status-count">{{ offlinePanels }}</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "painel-de-monitoramento",
  data() {
    return {
      panels: [],  // Armazena informações sobre os painéis
      onlinePanels: 0,
      offlinePanels: 0,
      searchQuery: ''
    };
  },
  methods: {
    async fetchPanelData() {
      try {
        const response = await axios.post('http://localhost:5000/check_links', {
          power_bi_links: [
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
            // Adicione mais links aqui
          ]
        });
        
        const results = response.data;
        this.panels = results.map(result => ({
          link: result.link,
          name: this.getPanelName(result.link),
          status: result.status
        }));
        this.updatePanelCounts();
      } catch (error) {
        console.error("Erro ao buscar dados dos painéis:", error);
      }
    },
    getPanelName(link) {
      const panelNames = {
        "https://observatorio.aeb.gov.br/politica-espacial/instituicoes-do-setor-espacial-brasileiro": "Indicadores do Orçamento",
        "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-da-loa-vigente": "Acompanhamento Orçamentário (PNAE)",
        // Adicione mais mapeamentos de link para nomes de painéis aqui
      };
      return panelNames[link] || "Painel Desconhecido";
    },
    updatePanelCounts() {
      this.onlinePanels = this.panels.filter(panel => panel.status === 'active').length;
      this.offlinePanels = this.panels.filter(panel => panel.status === 'inactive').length;
    }
  },
  mounted() {
    this.fetchPanelData(); // Fetch panel data when the component is mounted
  }
};
</script>

<style scoped>
/* Seu estilo aqui */
</style>


<style scoped>

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #1443a0;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
  background-color: #021147;
}

.panel-monitoring {
  width: 80%;
  max-width: 1200px;
  background-color: #fdfdfd;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
  grid-column: span 2;
  font-size: 28px;
  font-weight: bold;
  color: #333;
  border-bottom: 2px solid #ffea8a;
  padding-bottom: 10px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}

.card {
  padding: 20px;
  border: 2px solid #ffea8a;
  border-radius: 8px;
  text-align: center;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: normal;
  color: #000;
  min-height: 120px;
  transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: scale(1.03);
  border-color: #ffda47;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.card.offline {
  background-color: #ffe5e5;
  color: #d9534f;
}

.circle {
  display: inline-block;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  line-height: 30px;
  text-align: center;
  font-size: 16px;
  font-weight: bold;
  color: white;
  margin-top: 10px;
}

.blue {
  background-color: #5cb85c;
}

.red {
  background-color: #FF0000;
}

.sidebar {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sidebar img {
  max-width: 255px;
  margin-bottom: 20px;
}

.sidebar input[type="text"] {
  padding: 10px;
  width: 100%;
  border-radius: 5px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
}

.status {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 10px;
}

.status button {
  padding: 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
}

.status .online {
  background-color: #5cb85c;
  color: #fff;
}

.status .offline {
  background-color: #d9534f;
  color: #fff;
}

.circle-status {
  display: inline-block;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  line-height: 25px;
  text-align: center;
  font-size: 14px;
  font-weight: bold;
  color: white;
}

.status-count {
  font-size: 24px;
  font-weight: bold;
  background-color: rgba(255, 255, 255, 0.2);
  padding: 5px 10px;
  border-radius: 10px;
  color: #fff;
  margin-left: 10px;
}

@media (max-width: 768px) {
  .panel-monitoring {
    grid-template-columns: 1fr;
  }

  .grid {
    grid-template-columns: 1fr;
  }

  .sidebar img {
    max-width: 120px;
  }

  .status button {
    font-size: 14px;
  }

  .status-count {
    font-size: 18px;
  }
}

@media (max-width: 480px) {
  .card {
    font-size: 12px;
    min-height: 100px;
  }

  .circle {
    width: 25px;
    height: 25px;
    font-size: 14px;
  }

  .status button {
    font-size: 12px;
  }

  .status-count {
    font-size: 16px;
  }
}
</style>