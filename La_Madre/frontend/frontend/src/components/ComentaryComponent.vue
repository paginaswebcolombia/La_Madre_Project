<template>

    <swiper

        :pagination="{
        clickable: true,
        }"
        :breakpoints="{
        '768': {
          slidesPerView: 1,
          spaceBetween: 40,
        },
        '992': {
          slidesPerView: 3,
          spaceBetween: 50,
        },
        }"
        :autoplay="{
            delay: 2500,
            disableOnInteraction: false,
        }"
        :modules="modules"
        :navigation="false"
        class="mySwiper comentary_swiper py-5 m-3"
        >
          <swiper-slide v-for="(card,index) in Comentarios" :key="index">
            <div class="card border-0">
              
              <div class="p-2" style="overflow: hidden; display: flex; align-items: center; justify-content: center;">
                <img :src="rootUrl + `/media/` + card.imagen" class="rounded-circle img-fluid" style="width: 200px; height: 200px; object-fit: cover" alt="...">                
              </div>

              <div class="card-body">
                <h5 class="card-title">{{ card.titulo }}</h5>
                <p class="card-text">{{ card.descripcion }}</p>
                <div v-for="rating in card.calificacion" :key="rating">
                  <span v-for="star in getStars(rating)" :key="star" class="star-icon">
                    <i class="bi bi-star-fill" style="color: #F5811C;"></i>
                  </span>
                  <span v-if="hasHalfStar(rating)" class="star-icon" style="color: #F5811C;">
                    <i class="bi bi-star-half"></i>
                  </span>
                  
                </div>
              </div>
            </div>
          </swiper-slide>
    </swiper>
 
</template>

<script>
import { inject, ref } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';

import 'swiper/css';
import 'swiper/css/pagination';

import { Pagination, Autoplay } from 'swiper/modules';


export default {
  
  components: {
      Swiper,
      SwiperSlide,
    },

  setup() {
    const ratings = ref(["4.5", "3.8", "2.9", "5.0"]);
    const rootUrl = inject('$rootUrl')

    const getStars = (rating) => {
      const floatValue = parseFloat(rating);
      const fullStars = Math.floor(floatValue);
      return Array(fullStars).fill();
    };

    const hasHalfStar = (rating) => {
      const floatValue = parseFloat(rating);
      return floatValue % 1 !== 0;
    };

    const data = inject('$data');
    const Comentarios = data.Comentarios.map((comentario) => ({
      ...comentario,
      calificacion: [comentario.calificacion],
    }));

    return {
      Comentarios,
      ratings,
      getStars,
      hasHalfStar,
      modules: [Pagination, Autoplay],
      rootUrl,
    };
  },
};
</script>

<style scoped>
  .star-icon {
  margin-right: 5px;
  }
  
  @media (max-width: 580px) {
    .comentary_title{
    font-size: 40px;
    padding-top: 10px;
    }

    .swiper {
    width: 100%;
    height: 100%;
    }
    .swiper-card-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    font-size: 5px;
    font-weight: bold;
    color: #fff;
    }
    
  }

  @media (min-width: 581px) and (max-width: 992px){
    .comentary_title{
      font-size: 60px;
      margin-top: 30px;
      }

    .swiper {
    width: 100%;
    height: 100%;
    }
    .swiper-slide {
    text-align: center;
    font-size: 18px;
    background: #fff;
    /* Center slide text vertically */
    display: flex;
    justify-content: center;
    align-items: center;
    }
  }

  @media(min-width: 993px){
    .comentary_title{
    font-size: 75px;
    }

    .swiper {
    width: 100%;
    height: 100%;
    }
    .swiper-slide {
    text-align: center;
    font-size: 18px;
    background: #fff;
    /* Center slide text vertically */
    display: flex;
    justify-content: center;
    align-items: center;
    }
    .swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    }
  }
</style>
  