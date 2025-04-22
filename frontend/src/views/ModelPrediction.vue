<template>
    <v-container class="py-10">
      <!-- Header -->
      <v-row justify="center" class="mb-10">
        <v-col cols="12" md="8" class="text-center">
          <h1 class="text-h4 font-weight-bold text-primary mb-2">Run Model Predictions</h1>
          <p class="text-grey-darken-1">
            Follow the steps below to upload your dataset and run predictions using our trained models.
          </p>
        </v-col>
      </v-row>
  
      <!-- Stepper -->
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-stepper v-model="step" elevation="1" flat>
            <v-stepper-items>
              <!-- Step 1 -->
              <v-stepper-content step="1">
                <v-card class="pa-6" elevation="2">
                  <h2 class="text-h6 font-weight-bold mb-4">Step 1: Upload CSV File</h2>
  
                  <v-alert type="info" variant="tonal" class="mb-4" border="start" density="comfortable">
                    <p class="font-weight-bold mb-2">Upload Format Requirements:</p>
                    <ul class="mb-2 text-body-2">
                      <li><strong>Upload a .csv file</strong> with matching sample IDs.</li>
                      <li>Column order: <code>sampleid, ASV features, Diagnosis, Diagnosis_labeled</code></li>
                      <li>All values must be numeric. No blanks or extra columns.</li>
                      <li><code>Diagnosis_labeled</code> must be <strong>0 or 1</strong>.</li>
                      <li>No slashes in filenames.</li>
                    </ul>
                    <p class="text-caption text-grey-darken-1">
                      See the full format in the
                      <a href="https://github.com/NickkRodriguez/GatorBiome/blob/main/README.md"
                         class="text-decoration-underline" target="_blank" rel="noopener noreferrer">README</a>.
                    </p>
                  </v-alert>
  
                  <v-file-input
                    v-model="csvFile"
                    label="Select CSV File"
                    accept=".csv"
                    outlined
                    prepend-icon="mdi-upload"
                    @change="handleFileUpload"
                    class="mb-4"
                  />
  
                  <v-alert v-if="error" type="error" border="start" dense prominent class="mb-4">
                    {{ error }}
                  </v-alert>
  
                  <v-card-actions class="justify-end">
                    <v-btn color="primary" :disabled="!csvFile" @click="nextStep">Continue</v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>
  
              <!-- Step 2 -->
              <v-stepper-content step="2">
                <v-card class="pa-6" elevation="2">
                  <h2 class="text-h6 font-weight-bold mb-4">Step 2: Run Prediction</h2>
  
                  <p class="mb-4">Click the button below to start the prediction process. Results will be available shortly.</p>
  
                  <v-alert v-if="successMessage" type="success" border="start" dense prominent class="mb-4">
                    {{ successMessage }}
                  </v-alert>
  
                  <v-alert v-if="error" type="error" border="start" dense prominent class="mb-4">
                    {{ error }}
                  </v-alert>
  
                  <v-card-actions class="justify-space-between">
                    <v-btn text @click="prevStep">Back</v-btn>
                    <v-btn color="primary" :disabled="!csvFile" @click="submitFile">Run Prediction</v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>
  
            <!-- Step 3: View Results -->
            <v-stepper-content step="3">
            <v-card class="pa-6" elevation="2">
                <h2 class="text-h6 font-weight-bold mb-4">Step 3: View Results</h2>

                <v-row class="mb-6" align="center" justify="space-between">
                <v-col cols="12" sm="6">
                    <v-switch v-model="filterCancerOnly" label="Show Only Cancer Cases" inset />
                </v-col>
                <v-col cols="12" sm="6" class="text-end">
                    <v-btn @click="downloadCSV" color="primary" prepend-icon="mdi-download">
                    Export CSV
                    </v-btn>
                </v-col>
                </v-row>

                <v-btn
                variant="text"
                color="primary"
                class="mb-2"
                @click="showChart = !showChart"
                >
                {{ showChart ? 'Hide Chart' : 'Show Chart' }}
                </v-btn>

                <canvas
                v-show="showChart"
                ref="chartRef"
                class="mb-6"
                height="100"
                ></canvas>

                <v-table dense class="mb-6 prediction-table">
                <thead>
                    <tr>
                    <th class="text-left">Sample ID</th>
                    <th class="text-center">Prediction</th>
                    <th class="text-left">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(entry, index) in filteredPredictions" :key="index">
                    <td>{{ entry.id }}</td>
                    <td class="text-center">
                        <v-chip :color="entry.pred === 1 ? 'red lighten-4' : 'green lighten-4'" class="font-weight-bold">
                        {{ entry.pred }}
                        </v-chip>
                    </td>
                    <td :class="entry.pred === 1 ? 'text-error font-weight-medium' : 'text-success font-weight-medium'">
                        {{ entry.pred === 1 ? 'Cancer Detected' : 'No Cancer' }}
                    </td>
                    </tr>
                </tbody>
                </v-table>

                <v-card-actions class="justify-space-between">
                <v-btn text @click="prevStep">Back</v-btn>
                <v-btn color="primary" @click="$router.push('/')">Return to Home</v-btn>
                </v-card-actions>
            </v-card>
            </v-stepper-content>
            </v-stepper-items>
          </v-stepper>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { Chart, BarElement, CategoryScale, LinearScale, Tooltip, Legend } from "chart.js";
  Chart.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);
  
  export default {
    name: "ModelPrediction",
    data() {
      return {
        step: 1,
        csvFile: null,
        error: "",
        successMessage: "",
        predictions: [],
        showChart: true,
        filterCancerOnly: false,
        chartInstance: null,
      };
    },
    computed: {
      filteredPredictions() {
        return this.filterCancerOnly
          ? this.predictions.filter(p => p.pred === 1)
          : this.predictions;
      }
    },
    methods: {
      handleFileUpload() {
        this.error = "";
        this.successMessage = "";
        if (!this.csvFile || !this.csvFile.name.toLowerCase().endsWith(".csv")) {
          this.error = "Invalid file format. Please upload a .csv file.";
          this.csvFile = null;
        }
      },
      nextStep() {
        if (this.step === 1 && !this.csvFile) {
          this.error = "Please upload a CSV file before proceeding.";
          return;
        }
        this.error = "";
        this.step++;
      },
      prevStep() {
        if (this.step > 1) this.step--;
      },
      async submitFile() {
        if (!this.csvFile) {
          this.error = "Please upload a file first.";
          return;
        }
  
        this.successMessage = "";
        this.error = "";
  
        try {
          const formData = new FormData();
          formData.append("file", this.csvFile);
  
          const response = await fetch("http://127.0.0.1:8000/api/upload/", {
            method: "POST",
            body: formData,
          });
  
          if (!response.ok) throw new Error("Failed to start prediction.");
  
          const result = await response.json();
          this.successMessage = result.message || "Prediction started successfully.";
          
          // Transform into array of { id, pred }
          this.predictions = result.predictions.map((pred, i) => ({
            id: result.sample_ids?.[i] || `Sample ${i + 1}`,
            pred: pred
          }));
  
          this.$nextTick(() => this.renderChart());
          this.step++;
        } catch (err) {
          this.error = err.message || "Something went wrong while starting prediction.";
        }
      },
      renderChart() {
        if (this.chartInstance) this.chartInstance.destroy();
  
        const cancerCount = this.predictions.filter(p => p.pred === 1).length;
        const noCancerCount = this.predictions.length - cancerCount;
  
        const ctx = this.$refs.chartRef.getContext("2d");
        this.chartInstance = new Chart(ctx, {
          type: "bar",
          data: {
            labels: ["Cancer", "No Cancer"],
            datasets: [{
              label: "Sample Count",
              data: [cancerCount, noCancerCount],
              backgroundColor: ["#e53935", "#43a047"],
            }]
          },
          options: {
            responsive: true,
            plugins: { legend: { display: false } },
          }
        });
      },
      downloadCSV() {
        const headers = "Sample ID,Prediction\n";
        const rows = this.predictions.map(p => `${p.id},${p.pred}`).join("\n");
        const csvContent = headers + rows;
        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
        const link = document.createElement("a");
        const timestamp = new Date().toISOString().split("T")[0];
        link.href = URL.createObjectURL(blob);
        link.setAttribute("download", `GatorBiome_Predictions_${timestamp}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    }
  };
  </script>
  
  <style scoped>
  .text-decoration-underline {
    text-decoration: underline;
  }
  .text-success {
    color: #388e3c;
  }
  .text-error {
    color: #d32f2f;
  }
  </style>
  