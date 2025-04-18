<template>
    <span>{{ animatedValue.toFixed(decimalPlaces) }}</span>
  </template>
  
  <script>
  export default {
    props: {
      endValue: Number,
      decimalPlaces: {
        type: Number,
        default: 3,
      },
      duration: {
        type: Number,
        default: 1500,
      },
    },
    data() {
      return {
        animatedValue: 0,
        started: false,
      };
    },
    methods: {
      start() {
        if (this.started) return;
        this.started = true;
        const startTime = performance.now();
        const animate = (now) => {
          const progress = Math.min((now - startTime) / this.duration, 1);
          this.animatedValue = this.endValue * progress;
          if (progress < 1) requestAnimationFrame(animate);
        };
        requestAnimationFrame(animate);
      },
      reset() {
        this.started = false;
        this.animatedValue = 0;
      }
    },
    expose: ['start', 'reset'] // So the parent can call these
  };
  </script>
  