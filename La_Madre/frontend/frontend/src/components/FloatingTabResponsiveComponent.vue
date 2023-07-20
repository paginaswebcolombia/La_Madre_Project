<template>
    <div class="botones-cuadrados">
        <div class="d-inline-block ms-1 py-2 px-3 mx-md-3 mb-3 py-md-2 px-md-3" style="background-color: #F5811C; border-radius: 50px;">
            <i class="bi bi-telephone-outbound-fill" ></i>
        </div>
        <div class="d-inline-block ms-1 py-2 px-3 mx-md-3 mb-3 py-md-2 px-md-3" style="background-color: #F5811C; border-radius: 50px;">
            <i class="bi bi-whatsapp" ></i>
        </div>
        <div class="d-inline-block ms-1 py-2 px-3 mx-md-3 mb-3 py-md-2 px-md-3" style="background-color: #F5811C; border-radius: 50px;">
            <i class="bi bi-file-text" ></i>
        </div>
    </div>
  </template>
  
  
  <style>
  .botones-cuadrados {
    position: fixed;
    bottom: 20px;
    right: 20px;
  }
  
  .boton-cuadrado {
    width: 100px;
    height: 100px;
    background-color: #ccc;
    border: none;
    border-radius: 5px;
    margin-right: 10px;
    margin-bottom: 10px;
    color: #fff;
  }

@media (max-width: 576px) {
  /* Estilos para pantallas más pequeñas (hasta 576px) */
  .botones-cuadrados i {
    font-size: 30px;
  }
}

@media (min-width: 577px) and (max-width: 991px) {
  /* Estilos para pantallas de tamaño mediano (de 577px a 991px) */
  .botones-cuadrados i {
    font-size: 35px;
  }
}
  </style>
  