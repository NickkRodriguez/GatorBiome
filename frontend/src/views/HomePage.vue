<template>
  <v-container class="py-10 pt-6">
    <!-- Hero Section -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10" class="text-center">
        <h1 class="text-h3 font-weight-bold mb-4 text-primary">Welcome to Gator Biome</h1>
        <p :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : 'text-grey-darken-2'" class="text-subtitle-1">
          Built by UF students, GatorBiome is a modular ML platform to predict disease from microbiome data using 100-run evaluations and state-of-the-art feature engineering.
        </p>
      </v-col>
    </v-row>

    <!-- Why This Matters -->
    <v-row justify="center" class="mb-8">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold mb-4 text-center">Why This Matters</h2>
        <v-row dense>
          <v-col cols="12" sm="6" v-for="(point, i) in reasons" :key="i">
            <v-sheet
              class="pa-4 d-flex align-center why-card"
              :color="$vuetify.theme.dark ? '#1e1e1e' : 'blue-lighten-5'"
              elevation="4"
              rounded
            >
              <v-icon size="36" color="primary" class="mr-4">{{ point.icon }}</v-icon>
              <div>
                <div class="font-weight-bold mb-1" :class="$vuetify.theme.dark ? 'text-white' : ''">{{ point.title }}</div>
                <div class="text-body-2" :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : ''">{{ point.text }}</div>
              </div>
            </v-sheet>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- CTA Section -->
    <v-row justify="center" class="my-10">
      <v-col cols="12" md="10" class="text-center">
        <v-sheet elevation="3" rounded class="pa-8" :color="$vuetify.theme.dark ? '#1e1e1e' : 'blue-lighten-5'">
          <h2 class="text-h5 font-weight-bold mb-4 text-primary">Ready to test your dataset with our best model?</h2>
          <p class="text-subtitle-1 mb-4" :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : 'text-grey-darken-2'">
            Upload your microbiome CSV file and run predictions instantly using our highest-performing model pipeline.
          </p>
          <v-btn color="primary" large to="/model-prediction">
            Try It Now
          </v-btn>
        </v-sheet>
      </v-col>
    </v-row>

    <!-- Feature Engineering Stats -->
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
              class="pa-6 stat-card"
              :color="$vuetify.theme.dark ? '#1e1e1e' : 'blue-lighten-5'"
              @click="revealStat(index)"
              style="cursor: pointer;"
            >
              <v-icon size="36" color="primary">{{ stat.icon }}</v-icon>
              <h3 class="text-h6 font-weight-medium mt-2" :class="$vuetify.theme.dark ? 'text-white' : ''">{{ stat.title }}</h3>
              <h2 class="text-h4 font-weight-bold mt-1" :class="$vuetify.theme.dark ? 'text-white' : ''">
                <template v-if="stat.revealed">
                  <template v-if="stat.animate">
                    <span>{{ animatedValues[index].toFixed(stat.decimals) }}</span>
                  </template>
                  <template v-else>
                    {{ stat.value }}
                  </template>
                </template>
                <template v-else>
                  <span class="text-subtitle-1 font-italic font-weight-bold">Click to Discover Results</span>
                </template>
              </h2>
              <p class="text-caption" :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : ''">{{ stat.caption }}</p>
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
                <v-card
                  class="pa-4 text-center flip-card-style"
                  elevation="4"
                  :color="$vuetify.theme.dark ? '#1e1e1e' : 'white'"
                >
                  <v-icon size="48" color="primary">{{ card.icon }}</v-icon>
                  <h3 class="text-h6 font-weight-medium mt-3 mb-2" :class="$vuetify.theme.dark ? 'text-white' : ''">{{ card.title }}</h3>
                  <p class="text-body-2" :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : ''">{{ card.desc }}</p>
                </v-card>
              </div>
              <div class="flip-card-back">
                <v-card
                  class="pa-4 text-center d-flex flex-column justify-center flip-card-style"
                  elevation="4"
                  :color="$vuetify.theme.dark ? '#1e1e1e' : 'white'"
                >
                  <p class="text-body-1 mb-4" :class="$vuetify.theme.dark ? 'text-grey-lighten-1' : ''">{{ card.details }}</p>
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
export default {
  name: "HomePage",
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
          title: "Discover Feature Engineering",
          desc: "Selection vs. extraction methods.",
          icon: "mdi-chart-bar",
          details: "Analyze PCA, UMAP, Chi² and others side-by-side.",
          link: "/visualizations",
        },
      ],
      stats: [
        {
          icon: "mdi-star-circle",
          title: "Best Performing Preprocessing",
          value: "Rarefied",
          animate: false,
          revealed: false,
          caption: "Rarefied data achieved 0.785 AUC vs. CLR's 0.772",
        },
        {
          icon: "mdi-shield-check",
          title: "Best Ensemble Strategy",
          value: "Stacking",
          animate: false,
          revealed: false,
          caption: "Stacked model reached 0.815 AUC, outperforming all individual models",
        },
        {
          icon: "mdi-format-list-bulleted",
          title: "Best Feature Selection",
          value: "ANOVA F-Value",
          animate: false,
          revealed: false,
          caption: "ANOVA F-Value (100 features) gave the highest AUC",
        },
        {
          icon: "mdi-trending-up",
          title: "Top AUC Model",
          value: "LightGBM",
          animate: false,
          revealed: false,
          caption: "Rarefied + LightGBM achieved the highest AUC of 0.85",
        },
      ],
      animatedValues: [0, 0],
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
  methods: {
    revealStat(index) {
      const stat = this.stats[index];
      if (!stat.revealed) {
        stat.revealed = true;
        if (stat.animate) {
          const start = 0;
          const end = stat.value;
          const duration = 1000;
          const startTime = performance.now();

          const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            this.animatedValues[index] = start + (end - start) * progress;
            if (progress < 1) {
              requestAnimationFrame(animate);
            }
          };
          requestAnimationFrame(animate);
        }
      }
    },
  },
};
</script>

<style scoped>
.why-card:hover,
.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 14px rgba(30, 136, 229, 0.25);
  transition: all 0.3s ease;
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
.flip-card-style {
  transition: all 0.3s ease;
}
</style>
