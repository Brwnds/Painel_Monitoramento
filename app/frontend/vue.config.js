const path = require('path');

module.exports = {
  // Define o diretório de saída para os arquivos construídos
  outputDir: path.resolve(__dirname, '../backend/frontend/dist'),

  // Configuração do servidor de desenvolvimento
  devServer: {
    // Define um proxy para redirecionar as requisições para o backend Flask
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // Endereço do seu servidor Flask
        changeOrigin: true,
        pathRewrite: { '^/api': '' }, // Remove /api da URL
      },
    },
    // Mantém o histórico da API ao navegar
    historyApiFallback: true,
  },

  configureWebpack: {
    // Configurações adicionais do Webpack, se necessário
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'), // Define um alias para o diretório src
      },
    },
  },
};
