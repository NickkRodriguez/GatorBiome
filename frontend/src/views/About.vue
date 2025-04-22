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

<!-- Architecture Diagram -->
<v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <h2 class="text-h5 font-weight-bold mb-4 text-primary">Pipeline Architecture</h2>
        <div class="diagram-wrapper">
          <svg viewBox="0 0 1200 600" xmlns="http://www.w3.org/2000/svg">
            <!-- Background -->
            <rect x="10" y="10" width="850" height="500" fill="none" stroke="#bbb" stroke-dasharray="5,5"/>
            <text x="15" y="30" font-size="16" fill="#555">Back End</text>

            <rect x="880" y="10" width="300" height="500" fill="none" stroke="#bbb" stroke-dasharray="5,5"/>
            <text x="885" y="30" font-size="16" fill="#555">Front End</text>

            <!-- Boxes -->
            <g v-for="(box, i) in boxes" :key="i">
              <rect :x="box.x" :y="box.y" :width="box.width" :height="box.height" :fill="box.fill"
                    stroke="#000" stroke-width="1.5" rx="6"/>
              <text :x="box.x + box.width / 2" :y="box.y + 25" dominant-baseline="middle" text-anchor="middle"
                    font-weight="bold" font-size="14">
                {{ box.title }}
              </text>
              <text v-if="box.subtitle" :x="box.x + box.width / 2" :y="box.y + 45" text-anchor="middle"
                    font-size="12" fill="#333">
                {{ box.subtitle }}
              </text>
            </g>

            <!-- Arrows -->
            <g v-for="(arrow, i) in arrows" :key="i">
              <line :x1="arrow.x1" :y1="arrow.y1" :x2="arrow.x2" :y2="arrow.y2" stroke="#000" stroke-width="2"
                    marker-end="url(#arrowhead)"/>
              <text v-if="arrow.label" :x="(arrow.x1 + arrow.x2) / 2" :y="(arrow.y1 + arrow.y2) / 2 - 5"
                    text-anchor="middle" font-size="12" fill="#000">
                {{ arrow.label }}
              </text>
            </g>

            <!-- Arrowhead -->
            <defs>
              <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#000"/>
              </marker>
            </defs>
          </svg>
        </div>
      </v-col>
    </v-row>

    <!-- Expandable Pipeline Highlights -->
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
      boxes: [
        { title: "Gut Microbiome Dataset", x: 130, y: 100, width: 180, height: 60, fill: "#42A5F5" },
        { title: "Training Loop", subtitle: "ML Libraries", x: 350, y: 100, width: 200, height: 80, fill: "#42A5F5" },
        { title: "Trained Model", x: 580, y: 110, width: 140, height: 60, fill: "#66BB6A" },
        { title: "Testing Data", x: 350, y: 240, width: 160, height: 60, fill: "#42A5F5" },
        { title: "Model Prediction", x: 530, y: 240, width: 180, height: 60, fill: "#66BB6A" },
        { title: "User Input", subtitle: "Testing Data", x: 1020, y: 180, width: 160, height: 60, fill: "#EF5350" },
        { title: "Results Displayed", subtitle: "Matplotlib", x: 550, y: 360, width: 160, height: 60, fill: "#42A5F5" },
      ],

      arrows: [
        { x1: 310, y1: 130, x2: 350, y2: 130},
        { x1: 550, y1: 130, x2: 580, y2: 130 },
        { x1: 420, y1: 180, x2: 420, y2: 240},
        { x1: 510, y1: 270, x2: 530, y2: 270 },
        { x1: 710, y1: 270, x2: 1020, y2: 210},
        { x1: 620, y1: 300, x2: 630, y2: 360},
        { x1: 350, y1: 100, x2: 350, y2: 90 },
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
</style>
