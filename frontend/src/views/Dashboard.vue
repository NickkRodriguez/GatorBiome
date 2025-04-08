<template>
  <v-container>
    <h1 class="text-center">GatorBiome Dashboard</h1>

    <v-row>
      <!-- Chart Section -->
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="mb-2">Feature Engineering Results</h3>
          <BarChart :data="chartData" :options="chartOptions" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// Import necessary components
import { Bar } from 'vue-chartjs';
import { reactive, onMounted } from 'vue';
import { defineComponent } from 'vue';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';

// Register the necessary components with Chart.js
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default defineComponent({
  name: "DashboardPage",
  components: {
    BarChart: Bar
  },
  setup() {
    const chartData = reactive({
      labels: [],
      datasets: [
        {
          label: 'AUC Scores',
          data: [],
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }
      ]
    });

    const chartOptions = reactive({
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'AUC Scores for Feature Engineering'
        }
      }
    });

    // Fetch feature engineering data from the backend
    onMounted(async () => {
      try {
        const response = await fetch('http://localhost:8000/api/feature-engineering/?dataset_name=rarefied');
        const data = await response.json();

        // Log the data to the console to check the structure
        console.log(data);

        // Assuming the data contains `# Features` and `AUC`
        chartData.labels = data.map(row => row['# Features']);
        chartData.datasets[0].data = data.map(row => row['AUC']);
      } catch (error) {
        console.error("Error fetching feature engineering data:", error);
      }
    });

    return { chartData, chartOptions };
  }
});
</script>

<style scoped>
/* Add any additional styling here */
</style>
