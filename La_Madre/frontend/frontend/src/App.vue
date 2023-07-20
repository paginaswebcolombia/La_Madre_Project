<template>
  <div class="app-container">
    <NavbarComponent></NavbarComponent>
    <MultimediaPrincipalComponent></MultimediaPrincipalComponent>
    <FloatingTabComponent class="computer_tab"></FloatingTabComponent>
    <FloatingTabResponsiveComponent class="mobile_tab" style="z-index: 999;"></FloatingTabResponsiveComponent>
    <MainTextComponent></MainTextComponent>
    <LazyLoader>
      <PromoComponent></PromoComponent>
      <MenuComponent></MenuComponent>
      <NewsComponent></NewsComponent>
      <MapComponent></MapComponent>
      <ComentaryComponent></ComentaryComponent>
      <FooterComponent></FooterComponent>
    </LazyLoader>
  </div>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import MultimediaPrincipalComponent from './components/MultimediaPrincipalComponent.vue'
import FloatingTabComponent from './components/FloatingTabComponent.vue';
import FloatingTabResponsiveComponent from './components/FloatingTabResponsiveComponent.vue';
import MainTextComponent from './components/MainTextComponent.vue';
import PromoComponent from './components/PromoComponent.vue';
import MenuComponent from './components/MenuComponent.vue';
import NewsComponent from './components/NewsComponent.vue';
import MapComponent from './components/MapComponent.vue';
import ComentaryComponent from './components/ComentaryComponent.vue';
import FooterComponent from './components/FooterComponent.vue';

import LazyLoader from './components/LazyLoader.vue';

export default {
  components: {
    NavbarComponent,
    MultimediaPrincipalComponent,
    FloatingTabComponent,
    FloatingTabResponsiveComponent,
    MainTextComponent,
    PromoComponent,
    MenuComponent,
    NewsComponent,
    MapComponent,
    ComentaryComponent,
    FooterComponent,
    LazyLoader,
  }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@700&family=Satisfy&display=swap');

html, body {
  overflow-x: hidden;
}

/* Estilos para la barra de desplazamiento */
::-webkit-scrollbar {
  width: 10px; /* Ancho de la barra de desplazamiento */
}

::-webkit-scrollbar-track {
  background-color: #212529; /* Color del fondo de la barra de desplazamiento */
}

::-webkit-scrollbar-thumb {
  background-color: #F5811C; /* Color del pulgar de la barra de desplazamiento */
  border-radius: 5px; /* Radio de borde del pulgar */
}

::-webkit-scrollbar-thumb:hover {
  background-color: #F5811C; /* Color del pulgar de la barra de desplazamiento al pasar el cursor */
}

.app-container {
  position: relative;
}

.NavbarComponent {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 999; /* Asegura que el navbar esté en la capa superior */
}
.RalewayFont {
  font-family: 'Raleway', sans-serif;
  font-weight: 700;
}
.SatisfyFont {
  font-family: 'Satisfy', cursive;
  font-weight: 400;
}

@media (max-width: 576px) {
  /* Estilos para pantallas más pequeñas (hasta 576px) */
  .computer_tab{
    display: none;
  }
}

@media (min-width: 577px) and (max-width: 991px) {
  /* Estilos para pantallas de tamaño mediano (de 577px a 991px) */
  .computer_tab{
    display: none;
  }
}

@media (min-width: 992px) {
  /* Estilos para pantallas más grandes (a partir de 992px) */
  .mobile_tab{
    display: none;
  }
}
</style>

