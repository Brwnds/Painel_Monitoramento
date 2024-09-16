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
export default {
  name: "painel-de-monitoramento",
  data() {
    return {
      onlinePanels: 8,
      offlinePanels: 1
    };
  }
};
</script>

<style scoped>

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
