<template>
  <v-container class="py-10">
    <!-- Hero Section -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <h1 class="text-h4 font-weight-bold text-center text-primary mb-2">About Gator Biome</h1>
        <p class="text-center text-grey-darken-1">
          Built by UF students, GatorBiome is a modular ML platform to predict disease from microbiome data using 100-run evaluations and state-of-the-art feature engineering.
        </p>
      </v-col>
    </v-row>

    <!-- Project Overview -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10">
        <v-sheet class="pa-6 elevation-3 rounded-lg card-highlight">
          <v-row align="center" no-gutters>
            <v-col cols="12">
              <h2 class="text-h6 font-weight-bold mb-3 d-flex align-center">
                <v-icon class="me-2" color="primary">mdi-information-outline</v-icon>
                Project Overview
              </h2>
              <p class="text-body-1">
                GatorBiome is a modular machine learning pipeline built to predict diseases, such as colon cancer, using gut microbiome data.
                The system supports flexible feature engineering and rich visualization capabilities utilizing the datasets.
              </p>
            </v-col>
          </v-row>
        </v-sheet>
      </v-col>
    </v-row>

    <!-- Pipeline Architecture Image -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold mb-4 text-primary">Pipeline Architecture</h2>
        <v-img
          src="/pipeline_rep.png"
          alt="Pipeline Diagram"
          max-width="100%"
          class="rounded elevation-2 hover-zoom"
          @click="dialog = true"
        />
      </v-col>
    </v-row>

    <!-- Fullscreen Dialog for Architecture Image -->
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dense flat color="primary">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title class="white--text">Pipeline Architecture</v-toolbar-title>
        </v-toolbar>
        <v-img src="/pipeline_rep.png" class="fill-height" contain />
      </v-card>
    </v-dialog>

    <!-- Pipeline Highlights -->
    <v-row justify="center" class="mb-12">
      <v-col cols="12" md="10">
        <v-card elevation="3" class="pa-6 card-highlight">
          <v-card-title class="text-h6 font-weight-bold mb-4 d-flex align-center justify-space-between">
            <div>
              <v-icon class="me-2" color="primary">mdi-star-circle-outline</v-icon>
              Pipeline Highlights
            </div>
            <v-btn variant="text" @click="toggleHighlights" class="text-primary">
              {{ showHighlights ? 'Hide' : 'Show' }}
            </v-btn>
          </v-card-title>

          <v-expand-transition>
            <div v-if="showHighlights">
              <v-row dense>
                <v-col
                  cols="12"
                  sm="6"
                  v-for="(item, index) in animatedHighlights"
                  :key="item.title"
                >
                  <v-card
                    flat
                    class="pa-4 mb-4 rounded border fade-in card-highlight"
                    elevation="1"
                    :style="{ animationDelay: `${index * 500}ms` }"
                  >
                    <v-card-title class="text-primary font-weight-medium text-subtitle-1">
                      <v-icon class="me-2" color="primary">mdi-check-circle</v-icon>
                      {{ item.title }}
                    </v-card-title>
                    <v-card-text class="text-body-2">
                      {{ item.description }}
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>

    <!-- Meet the Team -->
    <v-row justify="center" class="mb-12">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold text-center mb-6">Meet the Team</h2>
        <v-row justify="center" align="stretch" dense>
          <v-col
            cols="12"
            sm="6"
            md="4"
            lg="4"
            v-for="(member, index) in team"
            :key="member.name"
          >
            <v-card
              class="pa-5 text-center card-highlight fade-in"
              :style="{ animationDelay: `${index * 150}ms` }"
              elevation="4"
            >
              <v-avatar size="64" class="mx-auto mb-4" color="primary">
                <v-icon size="36" color="white">mdi-account</v-icon>
              </v-avatar>
              <div class="text-subtitle-1 font-weight-bold">{{ member.name }}</div>
              <div class="text-caption text-grey-darken-1 mb-2">{{ member.title }}</div>
              <p class="text-body-2 mt-2">{{ member.role }}</p>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AboutPage",
  data() {
    return {
      dialog: false,
      showHighlights: false,
      animatedHighlights: [],
      highlights: [
        {
          title: "Multi-dataset Support",
          description: "Supports rarefied and CLR-transformed gut microbiome datasets.",
        },
        {
          title: "Flexible Feature Engineering",
          description: "Chi², Mutual Information, ANOVA, PCA, UMAP, KPCA.",
        },
        {
          title: "Robust Evaluation",
          description: "100-run cross-validation with model selection by AUC.",
        },
        {
          title: "Vue 3 Frontend",
          description: "Interactive and modular dashboard built with Composition API.",
        },
        {
          title: "Django REST API",
          description: "Scalable backend exposing endpoints for model metrics and datasets.",
        },
        {
          title: "Interactive Visualizations",
          description: "Includes ROC curves, heatmaps, and dimensionality plots to interpret model performance.",
        },
      ],
      team: [
        {
          name: "Nick Rodriguez",
          title: "Team Lead",
          role: "ML pipeline, system architecture, documentation, and project direction.",
        },
        {
          name: "Connor McLoon",
          title: "ML Engineer",
          role: "Model training, hyperparameter tuning, and integration support.",
        },
        {
          name: "Lachyn Almazova",
          title: "Frontend Lead",
          role: "Vue.js dashboard implementation and visualization integration.",
        },
        {
          name: "David Alvarez",
          title: "Backend Lead",
          role: "Django REST API and dashboard endpoint development.",
        },
        {
          name: "Fatemeh Tavassoli",
          title: "Advisor",
          role: "Microbiome data expert and research methodology guidance.",
        },
      ],
    };
  },
  methods: {
    toggleHighlights() {
      this.showHighlights = !this.showHighlights;
      if (this.showHighlights) this.animateHighlights();
    },
    animateHighlights() {
      this.animatedHighlights = [];
      this.highlights.forEach((item, i) => {
        setTimeout(() => {
          this.animatedHighlights.push(item);
        }, i * 150);
      });
    },
  },
};
</script>

<style scoped>
.fade-in {
  animation: fadeInUp 0.4s ease both;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.card-highlight {
  transition: all 0.3s ease;
  border: 1px solid transparent;
}
.card-highlight:hover {
  transform: scale(1.03);
  box-shadow: 0 8px 18px rgba(33, 150, 243, 0.25);
  border-color: rgba(33, 150, 243, 0.5);
  background-color: rgba(33, 150, 243, 0.03);
}
.hover-zoom {
  cursor: zoom-in;
  transition: transform 0.3s ease;
}
.hover-zoom:hover {
  transform: scale(1.01);
}
</style>
