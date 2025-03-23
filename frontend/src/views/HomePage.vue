<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <h1 class="text-center">GatorBiome Project</h1>
        <p>
          GatorBiome is a research project that leverages **machine learning** to analyze
          gut microbiomes for **early Autism Spectrum Disorder (ASD) detection**. Our goal
          is to provide non-invasive, early biomarkers for ASD diagnosis.
        </p>

        <v-card class="mt-5" outlined>
          <v-card-title>Why This Matters?</v-card-title>
          <v-card-text>
            - **Delayed ASD Diagnosis:** Current methods lack early, non-invasive biomarkers.<br>
            - **Gut-Brain Connection:** Research shows gut microbiome differences in ASD cases.<br>
            - **Machine Learning Advantage:** Can detect microbial patterns linked to ASD risk.<br>
            - **Impact on Healthcare:** Enables early intervention and personalized treatment.<br>
          </v-card-text>
        </v-card>

        <v-btn class="mt-5" color="primary" to="/dashboard">Go to Dashboard</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

