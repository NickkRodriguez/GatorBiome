<template>
  <v-container>
    <h1 class="text-center">GatorBiome Dashboard</h1>

    <v-row>
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="mb-2">Mock Microbiome Summary</h3>
          <ul>
            <li><strong>Bifidobacterium</strong>: 30%</li>
            <li><strong>Clostridia</strong>: 20%</li>
            <li><strong>Lactobacillus</strong>: 10%</li>
          </ul>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="mb-2">Coming Soon</h3>
          <p>Interactive charts and ML insights will appear here.</p>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "DashboardPage"
}
</script>
