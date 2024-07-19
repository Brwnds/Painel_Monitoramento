<template>
  <div class="container">
    <h1>Visualização de Painéis</h1>
    <button @click="checkPanels" :disabled="loading">
      <span v-if="!loading">Verificar Painéis</span>
      <span v-else>Verificando...</span>
    </button>
    <ul>
      <li v-for="(status, panel) in panelStatus" :key="panel" :class="statusClass(status)">
        <span class="panel-name">{{ panel }}</span>
        <span class="panel-status">{{ status }}</span>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PanelChecker',
  data() {
    return {
      panelStatus: {},
      loading: false
    };
  },
  methods: {
    async checkPanels() {
      this.loading = true;
      try {
        const response = await axios.get('http://localhost:5000/api/check_panels');
        this.panelStatus = response.data;
      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
    statusClass(status) {
      return status === 'active' ? 'active' : 'offline';
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
</style>
