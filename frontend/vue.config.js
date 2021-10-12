module.exports = {
  outputDir: 'dist',
  assetsDir: 'static', // Django의 STATIC_URL 설정 값
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000'
      }
    }
  }
}
