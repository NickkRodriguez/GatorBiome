<template>
    <v-container>
      <h2>Prediction Results</h2>
  
      <v-alert type="success" class="mb-4">
        {{ resultData.prediction }}
      </v-alert>
  
      <MicrobiomeChart :inputData="resultData.microbiome_data" />
    </v-container>
  </template>
  
  <script>
  import MicrobiomeChart from '@/components/MicrobiomeChart.vue'
  
  export default {
    name: 'ResultsView',
    components: { MicrobiomeChart },
    data() {
      return {
        resultData: {
          prediction: 'ASD risk: Medium',
          microbiome_data: {
            Lactobacillus: 32,
            Bifidobacterium: 21,
            Clostridia: 10,
            Ruminococcus: 12,
            Desulfovibrio: 7,
            Prevotella: 18
          }
        }
      }
    }
  }
  </script>
  