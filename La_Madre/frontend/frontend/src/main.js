
import VueLazyload from 'vue-lazyload';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap';
import axios from 'axios';
import { createApp } from 'vue';

import App from './App.vue'

var rootUrl = window.location.origin;


axios.get(rootUrl + '/data/api/')
    .then(response => {
        const data = response.data;
        const app = createApp(App);
        app.use(VueLazyload, {
            preLoad: 0.5, // Carga anticipada (ejemplo: 1.3 veces la altura de la ventana)
            error: `${rootUrl}/media/utilities/Error.webp`, // Ruta de una imagen de reemplazo en caso de error
            loading: `${rootUrl}/media/utilities/Charge.webp`, // Ruta de una imagen de carga mientras se espera la carga perezosa
            attempt: 1 // Número de intentos para cargar la imagen
          });
        app.provide('$rootUrl', rootUrl)
        app.provide('$data', data);
        app.mount('#app');
    })
    .catch(error => {
        console.error(error);
      });
