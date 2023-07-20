<template>
  <div>
    <slot v-if="isComponentVisible"></slot>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isComponentVisible: false,
    };
  },
  mounted() {
    this.addScrollListener();
  },
  methods: {
    addScrollListener() {
      window.addEventListener('scroll', this.checkVisibility);
      this.checkVisibility();
    },
    checkVisibility() {
      const rect = this.$el.getBoundingClientRect();
      const windowHeight = window.innerHeight || document.documentElement.clientHeight;
      const offset = windowHeight * 0.5;

      // Comprueba si el componente está dentro del área visible de la ventana
      if (rect.top < windowHeight + offset) {
        this.isComponentVisible = true;
        window.removeEventListener('scroll', this.checkVisibility);
      }
    },
  },
};
</script>