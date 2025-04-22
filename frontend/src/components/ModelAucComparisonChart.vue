<template>
  <v-card class="pa-4 elevation-3">
    <h3 class="text-subtitle-1 font-weight-bold mb-4 text-primary">Best Models Performance Comparison</h3>
    <Bar :data="chartData" :options="chartOptions" />
  </v-card>
</template>

<script>
import { Bar } from 'vue-chartjs';
import {
  Chart,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from 'chart.js';

Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export default {
  name: "ModelAucComparisonChart",
  components: { Bar },
  props: {
    clrData: Array,
    rarefiedData: Array,
  },
  computed: {
    chartData() {
      return {
        labels: ['AUC', 'Accuracy', 'Precision', 'Recall', 'F1'],
        datasets: [
          {
            label: 'CLR: Logistic Regression',
            backgroundColor: '#1976d2',
            data: [
              0.772, 0.711, 0.715, 0.711, 0.709 // From best_models.json for CLR
            ],
          },
          {
            label: 'Rarefied: LGBM',
            backgroundColor: '#4caf50',
            data: [
              0.785, 0.706, 0.717, 0.706, 0.702 // From best_models.json for Rarefied
            ],
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        plugins: {
          legend: { position: 'top' },
          tooltip: { enabled: true },
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 1,
          },
        },
      };
    },
  },
};
</script>

<style scoped>
</style>
