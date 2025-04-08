<template>
  <v-container class="py-10 pt-6">
    <!-- Hero Section -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10" class="text-center">
        <h1 class="text-h3 font-weight-bold mb-4">Welcome to Gator Biome</h1>
        <p class="text-subtitle-1 text-grey-darken-2">
          Built by UF students, GatorBiome is a modular ML platform to predict disease from microbiome data using 100-run evaluations and state-of-the-art feature engineering.
        </p>
      </v-col>
    </v-row>

    <!-- Why This Matters -->
    <v-row justify="center" class="mb-8">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold mb-4 text-center">Why This Matters</h2>
        <v-row dense>
          <v-col cols="12" sm="6" md="6" v-for="(point, i) in reasons" :key="i">
            <v-sheet
              class="pa-4 d-flex align-center elevation-2 why-card"
              color="blue-lighten-5"
              rounded
            >
              <v-icon size="36" color="primary" class="mr-4">{{ point.icon }}</v-icon>
              <div>
                <div class="font-weight-bold mb-1">{{ point.title }}</div>
                <div class="text-body-2">{{ point.text }}</div>
              </div>
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Feature Engineering Stats Section -->
    <v-row justify="center" class="mt-8 mb-12">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold mb-6 text-center">Feature Engineering Highlights</h2>
        <v-row justify="center" align="center">
          <v-col
            cols="12"
            md="3"
            class="text-center"
            v-for="(stat, index) in stats"
            :key="index"
          >
            <v-sheet
              elevation="4"
              rounded
              class="pa-6"
              color="blue-lighten-5"
              @click="stat.revealed = true"
              style="cursor: pointer;"
            >
              <v-icon size="36" color="primary">{{ stat.icon }}</v-icon>
              <h3 class="text-h6 font-weight-medium mt-2">{{ stat.title }}</h3>
              <h2 class="text-h4 font-weight-bold mt-1">
                <template v-if="stat.revealed">
                  <template v-if="stat.animate">
                    <StatCounter
                      :endValue="stat.value"
                      :decimalPlaces="stat.decimals"
                      :startOnMount="true"
                    />
                  </template>
                  <template v-else>
                    {{ stat.value }}
                  </template>
                </template>
                <template v-else>
                  <span class="text-subtitle-1 font-italic font-weight-bold">Click to Discover Results</span>
                </template>
              </h2>
              <p class="text-caption">{{ stat.caption }}</p>
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- Flip Cards -->
    <v-row justify="center" align="stretch" dense class="mb-8">
      <v-col cols="12" md="4" v-for="card in cards" :key="card.title">
        <v-hover v-slot="{ isHovering, props }">
          <div class="flip-card" v-bind="props">
            <div class="flip-card-inner" :class="{ flipped: isHovering }">
              <div class="flip-card-front">
                <v-card class="pa-4 text-center" elevation="4">
                  <v-icon size="48" color="primary">{{ card.icon }}</v-icon>
                  <h3 class="text-h6 font-weight-medium mt-3 mb-2">{{ card.title }}</h3>
                  <p class="text-body-2">{{ card.desc }}</p>
                </v-card>
              </div>
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
  </v-container>
</template>

<script>
import StatCounter from "@/components/StatCounter.vue";

export default {
  name: "HomePage",
  components: {
    StatCounter,
  },
  data() {
    return {
      cards: [
        {
          title: "Pipeline Overview",
          desc: "Learn how our modular ML system works.",
          icon: "mdi-cogs",
          details: "View architecture, stages, and evaluation workflows.",
          link: "/about",
        },
        {
          title: "Compare Model Results",
          desc: "Explore model performance across datasets.",
          icon: "mdi-database",
          details: "Get metrics like AUC and F1 across rarefied and CLR data.",
          link: "/models",
        },
        {
          title: "Compare Feature Engineering",
          desc: "Selection vs. extraction methods.",
          icon: "mdi-chart-bar",
          details: "Analyze PCA, UMAP, Chi² and others side-by-side.",
          link: "/visualizations",
        },
      ],
      stats: [
        {
          icon: "mdi-star-circle",
          title: "Top AUC (CLR)",
          value: 0.783,
          decimals: 3,
          animate: true,
          revealed: false,
          caption: "ANOVA F-Value (100 features)",
        },
        {
          icon: "mdi-trending-up",
          title: "Best Gain",
          value: 0.270,
          decimals: 3,
          animate: true,
          revealed: false,
          caption: "UMAP improved from 0.51 to 0.78",
        },
        {
          icon: "mdi-filter-variant",
          title: "CLR vs Rarefied",
          value: "CLR Wins",
          animate: false,
          revealed: false,
          caption: "Higher AUC in 5 of 6 methods",
        },
        {
          icon: "mdi-select-search",
          title: "Best Method Type",
          value: "Selection",
          animate: false,
          revealed: false,
          caption: "Outperformed extraction methods",
        },
      ],
      reasons: [
        {
          icon: "mdi-magnify",
          title: "Early Detection",
          text: "Gut microbiome composition can offer non-invasive markers for early cancer diagnosis.",
        },
        {
          icon: "mdi-cogs",
          title: "Pipeline Modularity",
          text: "Our system supports interchangeable datasets and ML models to generalize across diseases.",
        },
        {
          icon: "mdi-chart-line",
          title: "Interpretability",
          text: "ROC curves, heatmaps, and trend plots make results transparent and actionable.",
        },
        {
          icon: "mdi-web",
          title: "Accessible Interface",
          text: "A user-friendly dashboard enables researchers to explore performance metrics interactively.",
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

.why-card {
  transition: 0.3s ease;
}
.why-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 20px rgba(30, 136, 229, 0.15);
}

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
