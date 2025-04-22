<template>
  <v-container class="py-10">
    <!-- Header -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <h1 class="text-h4 font-weight-bold text-center text-primary mb-2">Model Comparison</h1>
        <p class="text-center text-grey-darken-1">
          Compare the best performing models across CLR and Rarefied transformations. Metrics include AUC, Accuracy, Precision, Recall, and F1 Score.
        </p>
      </v-col>
    </v-row>

    <!-- Best Models -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <v-row>
          <v-col cols="12" md="6">
            <v-card class="pa-4 elevation-3 hover-zoom">
              <h3 class="text-subtitle-1 font-weight-bold mb-2 text-primary">Best Model - CLR</h3>
              <div class="mb-3">{{ bestModels.clr.best_model }}</div>
              <v-list dense>
                <v-list-item v-for="(val, key) in bestModels.clr.metrics" :key="key">
                  <v-list-item-title class="text-body-2">
                    {{ key.toUpperCase() }}: <strong>{{ val.toFixed(3) }}</strong>
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
          <v-col cols="12" md="6">
            <v-card class="pa-4 elevation-3 hover-zoom">
              <h3 class="text-subtitle-1 font-weight-bold mb-2 text-primary">Best Model - Rarefied</h3>
              <div class="mb-3">{{ bestModels.rarefied.best_model }}</div>
              <v-list dense>
                <v-list-item v-for="(val, key) in bestModels.rarefied.metrics" :key="key">
                  <v-list-item-title class="text-body-2">
                    {{ key.toUpperCase() }}: <strong>{{ val.toFixed(3) }}</strong>
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Chart Comparison -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <ModelAucComparisonChart
          :clrData="clrTable"
          :rarefiedData="rarefiedTable"
        />
      </v-col>
    </v-row>

    <!-- Full Table Comparison -->
    <v-row justify="center" class="mb-12">
      <v-col cols="12" md="10">
        <!-- All Models - CLR -->
        <h2 class="text-h5 font-weight-bold mb-4 text-primary">All Models - CLR</h2>
        <v-data-table
          :headers="headers"
          :items="clrTable"
          class="elevation-1 mb-12"
          dense
          items-per-page="10"
          fixed-header
          height="500px"
          :search="searchClr"
          :sort-by="['auc']"
          :sort-desc="[true]"
        >
          <template #top>
            <v-text-field
              v-model="searchClr"
              label="Search CLR Models..."
              dense
              hide-details
              clearable
            />
          </template>

          <!-- Highlight row if best -->
          <template #item="{ item }">
            <tr :class="{ 'highlight-row': item.auc === bestClrAuc }">
              <td>{{ item.method }}</td>
              <td>{{ item.type }}</td>
              <td class="text-center">{{ item.features }}</td>
              <td class="text-center">{{ item.auc.toFixed(3) }}</td>
              <td class="text-center">{{ item.accuracy.toFixed(3) }}</td>
              <td class="text-center">{{ item.precision.toFixed(3) }}</td>
              <td class="text-center">{{ item.recall.toFixed(3) }}</td>
              <td class="text-center">{{ item.f1.toFixed(3) }}</td>
            </tr>
          </template>
        </v-data-table>


        <!-- All Models - Rarefied -->
        <h2 class="text-h5 font-weight-bold mb-4 text-primary">All Models - Rarefied</h2>
        <v-data-table
          :headers="headers"
          :items="rarefiedTable"
          class="elevation-1"
          dense
          items-per-page="10"
          fixed-header
          height="500px"
          :search="searchRarefied"
          :sort-by="['auc']"
          :sort-desc="[true]"
        >
          <template #top>
            <v-text-field
              v-model="searchRarefied"
              label="Search Rarefied Models..."
              dense
              hide-details
              clearable
            />
          </template>

          <template #headers="props">
            <tr>
              <th v-for="header in props.headers" :key="header.value">
                {{ header.text }}
              </th>
            </tr>
          </template>

          <template #item="{ item }">
            <tr :class="{ 'highlight-row': item.auc === bestRarefiedAuc }">
              <td>{{ item.method }}</td>
              <td>{{ item.type }}</td>
              <td>{{ item.features }}</td>
              <td>{{ item.auc.toFixed(3) }}</td>
              <td>{{ item.accuracy.toFixed(3) }}</td>
              <td>{{ item.precision.toFixed(3) }}</td>
              <td>{{ item.recall.toFixed(3) }}</td>
              <td>{{ item.f1.toFixed(3) }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Papa from "papaparse";
import ModelAucComparisonChart from "@/components/ModelAucComparisonChart.vue";

export default {
  name: "ModelComparisonPage",
  components: {
    ModelAucComparisonChart,
  },
  data() {
    return {
      bestModels: {
        clr: { best_model: "", metrics: {} },
        rarefied: { best_model: "", metrics: {} },
      },
      clrTable: [],
      rarefiedTable: [],
      bestClrAuc: 0,
      bestRarefiedAuc: 0,
      searchClr: "",
      searchRarefied: "",
      headers: [
        { text: "Method", value: "method" },
        { text: "Type", value: "type" },
        { text: "# Features", value: "features" },
        { text: "AUC", value: "auc" },
        { text: "Accuracy", value: "accuracy" },
        { text: "Precision", value: "precision" },
        { text: "Recall", value: "recall" },
        { text: "F1", value: "f1" },
      ],
    };
  },
  mounted() {
    this.loadBestModels();
    this.loadCsv("/results/summaries/feature_eng_results_clr.csv", "clrTable", "bestClrAuc");
    this.loadCsv("/results/summaries/feature_eng_results_rarefied.csv", "rarefiedTable", "bestRarefiedAuc");
  },
  methods: {
    async loadBestModels() {
      const res = await fetch("/results/summaries/best_models.json");
      const json = await res.json();
      this.bestModels = json;
    },
    loadCsv(path, targetKey, aucKey) {
      Papa.parse(path, {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: (results) => {
          const parsed = results.data
            .filter((row) => row.Method && row.AUC)
            .map((row) => ({
              method: row.Method,
              type: row.Type,
              features: row["# Features"],
              auc: +row.AUC,
              accuracy: +row.Accuracy,
              precision: +row.Precision,
              recall: +row.Recall,
              f1: +row.F1,
            }));
          this[targetKey] = parsed;
          this[aucKey] = Math.max(...parsed.map((row) => row.auc));
        },
      });
    },
  },
};
</script>

<style scoped>
.hover-zoom {
  transition: transform 0.3s ease;
}
.hover-zoom:hover {
  transform: scale(1.02);
  box-shadow: 0 10px 24px rgba(33, 150, 243, 0.25);
}
.highlight-row {
  background-color: rgba(33, 150, 243, 0.1) !important;
}
</style>
