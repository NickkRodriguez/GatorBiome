<template>
    <span>{{ animatedValue.toFixed(decimalPlaces) }}</span>
  </template>
  
  <script>
  export default {
    props: {
      endValue: {
        type: Number,
        required: true,
      },
      decimalPlaces: {
        type: Number,
        default: 3,
      },
      duration: {
        type: Number,
        default: 1500, // in ms
      }
    },
    data() {
      return {
        animatedValue: 0,
      };
    },
    mounted() {
      const startTime = performance.now();
      const animate = (now) => {
        const progress = Math.min((now - startTime) / this.duration, 1);
        this.animatedValue = this.endValue * progress;
        if (progress < 1) requestAnimationFrame(animate);
      };
      requestAnimationFrame(animate);
    },
  };
  </script>
  