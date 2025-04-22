<template>
    <v-container class="py-10">
      <v-row justify="center">
        <v-col cols="12" md="8">
          <v-card elevation="3">
            <v-card-title class="text-h5 font-weight-bold">
              Run Model Predictions
            </v-card-title>
            <v-card-text>
              <p>
                Upload a CSV file to run predictions using our trained models.
                Ensure your dataset is formatted correctly to match model input requirements.
              </p>
              <v-file-input
                v-model="csvFile"
                label="Upload CSV"
                accept=".csv"
                prepend-icon="mdi-file-upload"
                outlined
                @change="handleFileUpload"
                hide-details
              ></v-file-input>
  
              <v-alert
                v-if="error"
                type="error"
                dense
                class="mt-4"
                border="start"
                prominent
              >
                {{ error }}
              </v-alert>
  
              <v-alert
                v-if="successMessage"
                type="success"
                dense
                class="mt-4"
                border="start"
                prominent
              >
                {{ successMessage }}
              </v-alert>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="primary" :disabled="!csvFile" @click="submitFile">
                Run Prediction
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "ModelPrediction",
    data() {
      return {
        csvFile: null,
        error: "",
        successMessage: ""
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
      submitFile() {
        if (!this.csvFile) {
          this.error = "Please upload a file first.";
          return;
        }
  
        // Placeholder for pipeline/model prediction call
        console.log("Running prediction on file:", this.csvFile.name);
  
        // Simulate success response
        setTimeout(() => {
          this.successMessage = "Prediction started. Results will be available shortly.";
        }, 1000);
      }
    }
  };
  </script>
  