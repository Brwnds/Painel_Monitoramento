<template>
    <div class="container">
      <div class="panel-monitoring">
        <h1>Painel de Monitoramento</h1>
        <div class="grid">
          <div v-for="panel in panels" :key="panel.link" :class="['card', panel.status === 'erro' || panel.status === 'falha' ? 'offline' : '']">
            {{ panel.painel }}
            <div :class="['circle', panel.status === 'ativo' ? 'blue' : 'red']">{{ panel.status === 'ativo' ? '✔' : '✖' }}</div>
          </div>
        </div>
        <div class="sidebar">
          <img src="./assets/Logo.png" alt="Logo">
          <input type="text" placeholder="Buscar...">
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
        panels: [], // Armazenará os dados dos painéis
        onlinePanels: 0,
        offlinePanels: 0
      };
    },
    methods: {
      fetchPanels() {
        // Fazendo a requisição ao backend
        axios.post('http://localhost:5000/check_links', {
          links: [
            "https://observatorio.aeb.gov.br/politica-espacial/instituicoes-do-setor-espacial-brasileiro",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-da-loa-vigente",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/indicadores-do-orcamento-1",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-pnae-1",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/governanca/programa-nacional-de-atividades-espaciais-2013-pnae-2022-2031",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-orcamentario-do-ppa",
            "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/cooperacao-internacional/acordos-internacionais"
          ]
        }).then(response => {
          this.panels = response.data;
          this.updatePanelCounts();
        }).catch(error => {
          console.error('Erro ao buscar os painéis:', error);
        });
      },
      updatePanelCounts() {
        // Atualiza a contagem de painéis online e offline
        this.onlinePanels = this.panels.filter(panel => panel.status === 'ativo').length;
        this.offlinePanels = this.panels.filter(panel => panel.status !== 'ativo').length;
      }
    },
    mounted() {
      this.fetchPanels();
    }
  };
  </script>
  