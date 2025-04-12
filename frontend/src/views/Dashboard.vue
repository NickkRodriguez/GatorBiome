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
import API from "@/api";
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
onMounted(() => {
  console.log("Component mounted - about to make API request");

  // Wrap in setTimeout to ensure it runs after mounting
  setTimeout(async () => {
    try {
      console.log("Making API request to feature-engineering endpoint"); // was previously using native fetch function as opposed to api.get
      const response = await API.get('feature-engineering/', {
        params: { dataset_name: 'rarefied' }
      });
      console.log("API response received:", response);
    } catch (error) {
      console.error("Error making API request:", error);
      if (error.response) {
        console.error("Error response:", error.response.data);
        console.error("Error status:", error.response.status);
      } else if (error.request) {
        console.error("No response received:", error.request);
      } else {
        console.error("Error message:", error.message);
      }
    }
  }, 100);
});

    return { chartData, chartOptions };
  }
});
</script>

<style scoped>
/* Add any additional styling here */
</style>
