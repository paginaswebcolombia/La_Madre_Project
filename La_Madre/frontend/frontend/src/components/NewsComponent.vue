<template>
    <div class="container-fluid py-5">
        <div class="container">
            <p class="text-center RalewayFont mb-5 news_title">Novedades</p>
            <div class="mx-auto justify-content-center news_img imagen-levantada" style="border-radius: 20px;">
                <div id="carouselExampleIndicators" class="carousel slide">
                    <div class="carousel-inner">
                        <div class="carousel-item active imagen-levantada" style="border-radius: 20px;">
                            <img 
                            v-lazy="rootUrl + `/media/${news1.imagen}`"
                            class="d-block w-100 imagen-levantada" style="border-radius: 20px;">
                        </div>
                        <div class="carousel-item imagen-levantada" style="border-radius: 20px;" v-for="(item, index) in news2" :key="index">
                            <img 
                            v-lazy="rootUrl + `/media/${item.imagen}`"
                            class="d-block imagen-levantada" style="border-radius: 20px;">
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </div>
            
        </div>
    </div>
</template>
<script>
import { inject } from 'vue';

export default {
    setup() {
        const data = inject('$data');
        const rootUrl = inject('$rootUrl')
        const news1 = data.Novedades[0];
        const news2 = data.Novedades
        news2.shift();

        return { 
            news1,
            news2,
            rootUrl,
        }
    }
}
</script>

<style>

    @media (max-width: 580px) {
        .news_title{
        font-size: 50px;
        padding-top: 10px;
        }
        .news_img{
        width: 80%;
        }

    }

    @media (min-width: 581px) and (max-width: 992px){
        .news_title{
        font-size: 60px;
        margin-top: 30px;
        }
        .news_img{
        width: 60%;
        }
    }
    @media(min-width: 993px){
        .news_title{
        font-size: 75px;
        }
        .news_img{
        width: 40%;
        }
    }
</style>