import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
// import bootstrap
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css'
import axios from 'axios'

const pinia = createPinia()
axios.defaults.baseURL = 'http://localhost:7000';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');


createApp(App).use(pinia).use(router).mount('#app')
