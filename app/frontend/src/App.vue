<template>
  <div id="app">
    <PainelMonitoramento />
  </div>
</template>

<script>
import PainelMonitoramento from './components/PainelMonitoramento.vue';

export default {
  name: 'App',
  components: {
    PainelMonitoramento
  }
};
</script>

<style>
/* estilos globais se necessário */
</style>

<template>
  <div class="container">
    <div class="panel-monitoring">
      <h1>Painel de Monitoramento</h1>
      <div class="grid">
<<<<<<< Updated upstream
        <div class="card">
          Indicadores do Orçamento
          <div class="circle blue">✔</div>
        </div>
        <div class="card offline">
          Acompanhamento Orçamentário (PNAE)
          <div class="circle red">✖</div>
        </div>
        <div class="card">
          Acompanhamento Orçamentário (PPA)
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          PNAE 2022-2031 Dimensão Setorial
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          Acordos Internacionais
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          Cursos de Capacitação na Área Aeroespacial
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          Registro de Objetos Espaciais Brasileiros
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          Painel de Mapeamento de Tecnologias Espaciais
          <div class="circle blue">✔</div>
        </div>
        <div class="card">
          Dados e Indicadores
          <div class="circle blue">✔</div>
=======
        <div v-for="panel in filteredPanels" :key="panel.link" class="card" :class="{ offline: panel.status === 'inactive' }">
          <div class="panel-name">{{ panel.name }}</div>
          <div class="circle" :class="{ blue: panel.status === 'active', red: panel.status === 'inactive' }">
            {{ panel.status === 'active' ? '✔' : '✖' }}
          </div>
>>>>>>> Stashed changes
        </div>
      </div>
      <div class="sidebar">
        <img src="./assets/Logo.png" alt="Logo">
        
        <input type="text" placeholder="Buscar...">
        <div class="status">
          <button class="online" @click="filterStatus('active')">
            Painéis Online
            <span class="status-count">{{ onlinePanels }}</span>
          </button>
          <button class="offline" @click="filterStatus('inactive')">
            Painéis Offline
            <span class="status-count">{{ offlinePanels }}</span>
          </button>
          <button class="check-panels" @click="fetchPanelData">
            Verificar Painéis
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "painel-de-monitoramento",
  data() {
    return {
<<<<<<< Updated upstream
      onlinePanels: 8,
      offlinePanels: 1
    };
=======
      panels: [],  // Armazena informações sobre os painéis
      onlinePanels: 0,
      offlinePanels: 0,
      searchQuery: '',
      statusFilter: null, // Armazenar o filtro de status
    };
  },
  computed: {
    filteredPanels() {
      return this.panels
        .filter(panel => panel.name.toLowerCase().includes(this.searchQuery.toLowerCase()))
        .filter(panel => !this.statusFilter || panel.status === this.statusFilter); // Aplicar o filtro de status
    }
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
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-pnae-1",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-ppa",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/cooperacao-internacional/acordos-internacionais",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/licenciamento-e-normatizacao",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/governanca/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-capital-humano/explorador-de-dados-de-capital-humano",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/sistemas-espaciais/satelites/registro-de-satelites-brasileiros",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-desenvolvimento-tecnologico/tema-mapeamento-tecnologico/mapeamento-de-tecnologias-espaciais",
          "https://observatorio.aeb.gov.br/prosame/carteira-de-admissao",
          "https://observatorio.aeb.gov.br/prosame/carteira-de-qualificacao",
          "https://observatorio.aeb.gov.br/prosame/carteira-de-execucao",
          "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/governanca/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031"  
          ]
        }, {
          headers: {
            'Content-Type': 'application/json' 
          }
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
      
      };
      return panelNames[link] || "Painel Desconhecido";
    },
    updatePanelCounts() {
      this.onlinePanels = this.panels.filter(panel => panel.status === 'active').length;
      this.offlinePanels = this.panels.filter(panel => panel.status === 'inactive').length;
    },
    filterStatus(status) {
      this.statusFilter = status; // Atualiza o filtro de status
    }
  },
  mounted() {
    this.fetchPanelData(); // Busca dados dos painéis quando o componente é montado
>>>>>>> Stashed changes
  }
};
</script>

<style scoped>
<<<<<<< Updated upstream

=======
/* Seu estilo aqui */
>>>>>>> Stashed changes
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #e3e5e9;
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
  justify-content: space-between;
  width: 100%;
}

.status button {
  background-color: #007bff;
  border: none;
  color: white;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  flex: 1;
  margin: 0 5px;
  font-size: 14px;
  position: relative;
}

.status-count {
  background-color: #ffffff;
  border-radius: 12px;
  padding: 4px 8px;
  position: absolute;
  top: -5px;
  right: -5px;
  font-size: 12px;
  color: #007bff;
}

.status button:hover {
  background-color: #0056b3;
}

.check-panels {
  background-color: #5cb85c;
}

.check-panels:hover {
  background-color: #4cae4c;
}
</style>
