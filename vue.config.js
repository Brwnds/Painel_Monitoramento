const path = require('path');

module.exports = {
    configureWebpack: {
        resolve: {
            alias: {
                '@': path.resolve(__dirname, 'frontend/src'),
            },
        },
    },
    devServer: {
        contentBase: path.resolve(__dirname, 'frontend/dist'),
    },
};
