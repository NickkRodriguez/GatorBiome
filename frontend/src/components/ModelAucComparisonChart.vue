<template>
  <div>
    <h2 class="text-h6 font-weight-bold text-primary mb-4">AUC Difference Chart</h2>

    <!-- Filter -->
    <v-select
      v-model="selectedMethods"
      :items="availableMethods"
      label="Filter by Method"
      multiple
      chips
      clearable
      class="mb-6"
    />

    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: "ModelAucComparisonChart",
  components: {
    Bar,
  },
  props: {
    clrData: {
      type: Array,
      default: () => [],
    },
    rarefiedData: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      selectedMethods: [],
    };
  },
  computed: {
    availableMethods() {
      const methods = new Set(this.clrData.map((row) => row.method));
      return Array.from(methods).sort();
    },
    chartData() {
      if (!this.clrData.length || !this.rarefiedData.length) return null;

      const labels = [];
      const aucDifferences = [];

      this.clrData.forEach((clrModel) => {
        const match = this.rarefiedData.find(
          (r) =>
            r.method === clrModel.method &&
            r.type === clrModel.type &&
            r.features === clrModel.features
        );

        const shouldInclude =
          !this.selectedMethods.length || this.selectedMethods.includes(clrModel.method);

        if (match && shouldInclude) {
          labels.push(clrModel.method);
          aucDifferences.push(clrModel.auc - match.auc);
        }
      });

      return {
        labels,
        datasets: [
          {
            label: "CLR AUC - Rarefied AUC",
            data: aucDifferences,
            backgroundColor: "#42a5f5",
          },
        ],
      };
    },
    chartOptions() {
      return {
        responsive: true,
        plugins: {
          legend: {
            display: false,
          },
          title: {
            display: false,
          },
        },
        scales: {
          y: {
            title: {
              display: true,
              text: "Δ AUC",
            },
          },
        },
      };
    },
  },
};
</script>

<style scoped>
h2 {
  margin-bottom: 1rem;
}
</style>
