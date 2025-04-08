<template>
  <v-container class="py-10">
    <!-- Hero Section -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10" class="text-center">
        <h1 class="text-h3 font-weight-bold mb-4">Welcome to Gator Biome</h1>
        <p class="text-subtitle-1 text-grey-darken-2">
          Built by UF students, GatorBiome is a modular ML platform to predict disease from microbiome data using 100-run evaluations and state-of-the-art feature engineering.
        </p>
      </v-col>
    </v-row>

    <!-- Flip Cards -->
    <v-row justify="center" align="stretch" dense>
      <v-col cols="12" md="4" v-for="card in cards" :key="card.title">
        <v-hover v-slot="{ isHovering, props }">
          <div class="flip-card" v-bind="props">
            <div class="flip-card-inner" :class="{ flipped: isHovering }">
              <!-- Front -->
              <div class="flip-card-front">
                <v-card class="pa-4 text-center" elevation="4">
                  <v-icon size="48" color="primary">{{ card.icon }}</v-icon>
                  <h3 class="text-h6 font-weight-medium mt-3 mb-2">{{ card.title }}</h3>
                  <p class="text-body-2">{{ card.desc }}</p>
                </v-card>
              </div>
              <!-- Back -->
              <div class="flip-card-back">
                <v-card class="pa-4 text-center d-flex flex-column justify-center" elevation="4">
                  <p class="text-body-1 mb-4">{{ card.details }}</p>
                  <v-btn color="primary" :to="card.link">Explore</v-btn>
                </v-card>
              </div>
            </div>
          </div>
        </v-hover>
      </v-col>
    </v-row>

    <!-- Why This Matters -->
    <v-row justify="center" class="mt-12">
      <v-col cols="12" md="8">
        <v-card elevation="2">
          <v-card-item>
            <v-card-title class="text-h5 font-weight-medium mb-2">Why This Matters</v-card-title>
            <v-card-text class="text-body-1">
              <v-list lines="one" density="comfortable">
                <v-list-item prepend-icon="mdi-magnify">
                  <v-list-item-title>
                    <strong>Early Detection</strong>: Gut microbiome composition can offer non-invasive markers for early cancer diagnosis.
                  </v-list-item-title>
                </v-list-item>
                <v-list-item prepend-icon="mdi-cogs">
                  <v-list-item-title>
                    <strong>Pipeline Modularity</strong>: Our system supports interchangeable datasets and ML models to generalize across diseases.
                  </v-list-item-title>
                </v-list-item>
                <v-list-item prepend-icon="mdi-chart-line">
                  <v-list-item-title>
                    <strong>Interpretability</strong>: ROC curves, heatmaps, and trend plots make results transparent and actionable.
                  </v-list-item-title>
                </v-list-item>
                <v-list-item prepend-icon="mdi-web">
                  <v-list-item-title>
                    <strong>Accessible Interface</strong>: A user-friendly dashboard enables researchers to explore performance metrics interactively.
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card-item>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomePage",
  data() {
    return {
      cards: [
        {
          title: "Rarefied Dataset Results",
          desc: "Explore model metrics and visualizations.",
          icon: "mdi-database",
          details: "Get metrics like AUC and F1 for rarefied microbiome data.",
          link: "/dashboard?dataset=rarefied",
        },
        {
          title: "Compare Feature Engineering",
          desc: "Selection vs. extraction methods.",
          icon: "mdi-chart-bar",
          details: "Analyze PCA, UMAP, Chi² and others side-by-side.",
          link: "/feature-engineering",
        },
        {
          title: "Pipeline Overview",
          desc: "Learn how our modular ML system works.",
          icon: "mdi-cogs",
          details: "View architecture, stages, and evaluation workflows.",
          link: "/about",
        },
      ],
    };
  },
};
</script>

<style scoped>
h1 {
  color: #1e88e5;
}

.text-grey-darken-2 {
  color: #616161 !important;
}

/* Flip card styles */
.flip-card {
  perspective: 1000px;
}
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 300px;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.flip-card-inner.flipped {
  transform: rotateY(180deg);
}
.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}
.flip-card-back {
  transform: rotateY(180deg);
}
</style>
