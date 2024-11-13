<template>
  <div class="container">
    <h1>Visualização de Painéis e Links</h1>
    <button @click="checkLinks" :disabled="loading">
      <span v-if="!loading">Verificar Links</span>
      <span v-else>Verificando...</span>
    </button>
    <ul>
      <li v-for="(status, panel) in panelStatus" :key="panel" :class="statusClass(status)">
        <span class="panel-name">{{ panel }}</span>
        <span class="panel-status">{{ status }}</span>
      </li>
    </ul>

    <div class="link-status">
      <h2>Status dos Links</h2>
      <p>Ativos: {{ statusCount.ativo }}</p>
      <p>Inválidos: {{ statusCount.inválido }}</p>
      <p>Erros: {{ statusCount.erro }}</p>
      <p>Falhas: {{ statusCount.falha }}</p>
    </div>

    <div class="link-results">
      <h3>Resultados dos Links</h3>
      <ul>
        <li v-for="(link, index) in links" :key="index">
          {{ link.link }} - {{ link.status }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LinkChecker',
  data() {
    return {
      panelStatus: {}, // Status dos painéis
      loading: false,
      links: [], // Resultados dos links
      statusCount: { ativo: 0, inválido: 0, erro: 0, falha: 0 } // Contagem dos status dos links
    };
  },
  methods: {
    async checkLinks() {
      this.loading = true;
      try {
        const response = await axios.post('http://localhost:5000/check_links', {
          links: ["https://observatorio.aeb.gov.br/politica-espacial/instituicoes-do-setor-espacial-brasileiro", "https://observatorio.aeb.gov.br/dados-e-indicadores/tema-governo/tema-orcamento/acompanhamento-da-loa-vigente"] // Adicione seus links aqui
        });
        this.links = response.data.result; // Armazena os resultados dos links
        this.statusCount = response.data.status_count; // Armazena a contagem de status
      } catch (error) {
        console.error("Erro ao verificar links:", error);
      } finally {
        this.loading = false;
      }
    },
    statusClass(status) {
      return status === 'active' ? 'active' : 'offline'; // Adicione outras classes conforme necessário
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  font-family: Arial, sans-serif;
}

h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
  color: #333;
}

button {
  margin: 20px;
  padding: 10px 20px;
  font-size: 1.2em;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

ul {
  list-style-type: none;
  padding: 0;
  margin-top: 20px;
}

li {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  margin: 5px 0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.active {
  background-color: #d4edda;
  color: #155724;
}

.offline {
  background-color: #f8d7da;
  color: #721c24;
}

.panel-name {
  font-weight: bold;
}

.panel-status {
  font-style: italic;
}

.link-status {
  margin-top: 30px;
}

.link-results {
  margin-top: 20px;
}
</style>
