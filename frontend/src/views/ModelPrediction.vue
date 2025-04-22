<template>
    <v-container class="py-10">
      <!-- Page Header -->
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
            <!-- Stepper Header -->
            <v-stepper-header>
              <v-stepper-step :complete="step > 1" step="1">Upload</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step :complete="step > 2" step="2">Confirm</v-stepper-step>
              <v-divider></v-divider>
              <v-stepper-step step="3">Run Prediction</v-stepper-step>
            </v-stepper-header>
  
            <v-stepper-items>
              <!-- Step 1 -->
              <v-stepper-content step="1">
                <v-card class="pa-6" elevation="2">
                  <h2 class="text-h6 font-weight-bold mb-4">Step 1: Upload CSV File</h2>
  
                  <v-alert type="info" variant="tonal" class="mb-4" border="start" density="comfortable">
                    <p class="font-weight-bold mb-2">Upload Format Requirements:</p>
                    <ul class="mb-2 text-body-2">
                      <li><strong>Upload two .csv files</strong> with matching sample IDs.</li>
                      <li>Column order: <code>sampleid, ASV features, Diagnosis, Diagnosis_labeled</code></li>
                      <li>All values must be numeric. No blanks or extra columns.</li>
                      <li><code>Diagnosis_labeled</code> must be <strong>0 or 1</strong>.</li>
                      <li>No slashes in filenames.</li>
                    </ul>
                    <p class="text-caption text-grey-darken-1">See the full format in the <a href="#" class="text-decoration-underline">README</a>.</p>
                  </v-alert>
  
                  <v-file-input
                    v-model="csvFile"
                    label="Select CSV File"
                    accept=".csv"
                    outlined
                    prepend-icon="mdi-upload"
                    @change="handleFileUpload"
                    class="mb-4"
                  ></v-file-input>
  
                  <v-alert v-if="error" type="error" border="start" dense prominent class="mb-4">
                    {{ error }}
                  </v-alert>
  
                  <v-card-actions class="justify-end">
                    <v-btn color="primary" :disabled="!csvFile" @click="nextStep">
                      Continue
                    </v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>
  
              <!-- Step 2 -->
              <v-stepper-content step="2">
                <v-card class="pa-6" elevation="2">
                  <h2 class="text-h6 font-weight-bold mb-4">Step 2: Confirm Details</h2>
  
                  <p class="mb-4">Please confirm that your uploaded file meets the required format and contains valid data:</p>
  
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="primary">mdi-file-check</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>{{ csvFile?.name || 'No file selected' }}</v-list-item-title>
                  </v-list-item>
  
                  <v-card-actions class="justify-space-between mt-4">
                    <v-btn text @click="prevStep">Back</v-btn>
                    <v-btn color="primary" @click="nextStep">Continue</v-btn>
                  </v-card-actions>
                </v-card>
              </v-stepper-content>
  
              <!-- Step 3 -->
              <v-stepper-content step="3">
                <v-card class="pa-6" elevation="2">
                  <h2 class="text-h6 font-weight-bold mb-4">Step 3: Run Prediction</h2>
  
                  <p class="mb-4">Click the button below to start the prediction process. Results will be available shortly.</p>
  
                  <v-alert
                    v-if="successMessage"
                    type="success"
                    border="start"
                    dense
                    prominent
                    class="mb-4"
                  >
                    {{ successMessage }}
                  </v-alert>
  
                  <v-card-actions class="justify-space-between">
                    <v-btn text @click="prevStep">Back</v-btn>
                    <v-btn color="primary" :disabled="!csvFile" @click="submitFile">
                      Run Prediction
                    </v-btn>
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
  export default {
    name: "ModelPrediction",
    data() {
      return {
        step: 1,
        csvFile: null,
        error: "",
        successMessage: "",
      };
    },
    methods: {
      handleFileUpload(file) {
        this.error = "";
        this.successMessage = "";
  
        if (file && file.type !== "text/csv") {
          this.error = "Invalid file format. Please upload a CSV file.";
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
      submitFile() {
        if (!this.csvFile) {
          this.error = "Please upload a file first.";
          return;
        }
  
        console.log("Running prediction on file:", this.csvFile.name);
        setTimeout(() => {
          this.successMessage = "Prediction started. Results will be available shortly.";
        }, 1000);
      },
    },
  };
  </script>
  
  <style scoped>
  .text-decoration-underline {
    text-decoration: underline;
  }
  </style>
  