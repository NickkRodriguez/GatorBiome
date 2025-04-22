<template>
  <v-container class="py-10">
    <!-- Page Header -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="10">
        <h1 class="text-h4 font-weight-bold text-center text-primary mb-2">
          Model Evaluation Visualizations
        </h1>
        <p class="text-center text-grey-darken-1">
          These visualizations compare CLR vs Rarefied Preprocessing using heatmaps, ROC curves, and metric trend plots for AUC and F1 scores.
        </p>
      </v-col>
    </v-row>

    <!-- Ensemble ROC Curve -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10">
        <v-expand-transition>
          <div>
            <div class="d-flex justify-space-between align-center mb-4">
              <h2 class="text-h5 font-weight-bold text-primary">Ensemble ROC Curve</h2>
              <v-btn text color="primary" @click="showEnsemble = !showEnsemble">
                {{ showEnsemble ? 'Hide' : 'Show' }}
              </v-btn>
            </div>
            <v-row dense v-show="showEnsemble">
              <v-col
                v-for="(img, i) in ensembleImages"
                :key="'ensemble-' + i"
                cols="12"
                md="6"
                class="mb-6"
              >
                <v-card class="overflow-hidden hover-zoom" elevation="3" @click="openImage(img)">
                  <v-img :src="img.path" :alt="img.label" height="300px" />
                  <v-card-title class="font-weight-bold">{{ img.label }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-expand-transition>
      </v-col>
    </v-row>

    <!-- Combined ROC Curve for CLR + Rarefied -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10">
        <v-expand-transition>
          <div>
            <div class="d-flex justify-space-between align-center mb-4">
              <h2 class="text-h5 font-weight-bold text-primary">ROC Curve – All Models</h2>
              <v-btn text color="primary" @click="showCombinedRoc = !showCombinedRoc">
                {{ showCombinedRoc ? 'Hide' : 'Show' }}
              </v-btn>
            </div>
            <v-row dense v-show="showCombinedRoc">
              <v-col
                v-for="(img, i) in combinedRocImages"
                :key="'combined-roc-' + i"
                cols="12"
                md="6"
                class="mb-6"
              >
                <v-card class="overflow-hidden hover-zoom" elevation="3" @click="openImage(img)">
                  <v-img :src="img.path" :alt="img.label" height="300px" />
                  <v-card-title class="font-weight-bold">{{ img.label }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-expand-transition>
      </v-col>
    </v-row>

    <!-- CLR Section -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10">
        <v-expand-transition>
          <div>
            <div class="d-flex justify-space-between align-center mb-4">
              <h2 class="text-h5 font-weight-bold text-primary">CLR Preprocessing</h2>
              <v-btn text color="primary" @click="showClr = !showClr">
                {{ showClr ? 'Hide' : 'Show' }}
              </v-btn>
            </div>
            <v-row dense v-show="showClr">
              <v-col
                v-for="(img, i) in clrImages"
                :key="'clr-' + i"
                cols="12"
                md="6"
                class="mb-6"
              >
                <v-card class="overflow-hidden hover-zoom" elevation="3" @click="openImage(img)">
                  <v-img :src="img.path" :alt="img.label" height="300px" />
                  <v-card-title class="font-weight-bold">{{ img.label }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-expand-transition>
      </v-col>
    </v-row>

    <!-- Rarefied Section -->
    <v-row justify="center" class="mb-6">
      <v-col cols="12" md="10">
        <v-expand-transition>
          <div>
            <div class="d-flex justify-space-between align-center mb-4">
              <h2 class="text-h5 font-weight-bold text-primary">Rarefied Preprocessing</h2>
              <v-btn text color="primary" @click="showRarefied = !showRarefied">
                {{ showRarefied ? 'Hide' : 'Show' }}
              </v-btn>
            </div>
            <v-row dense v-show="showRarefied">
              <v-col
                v-for="(img, i) in rarefiedImages"
                :key="'rarefied-' + i"
                cols="12"
                md="6"
                class="mb-6"
              >
                <v-card class="overflow-hidden hover-zoom" elevation="3" @click="openImage(img)">
                  <v-img :src="img.path" :alt="img.label" height="300px" />
                  <v-card-title class="font-weight-bold">{{ img.label }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </v-expand-transition>
      </v-col>
    </v-row>

    <!-- Fullscreen Zoom Dialog -->
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card>
        <v-toolbar dense flat color="primary">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title class="white--text">{{ selectedImage.label }}</v-toolbar-title>
        </v-toolbar>
        <v-img :src="selectedImage.path" class="fill-height" contain />
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: "VisualizationPage",
  data() {
    return {
      dialog: false,
      selectedImage: { label: "", path: "" },
      showClr: true,
      showRarefied: true,
      showEnsemble: true,
      showCombinedRoc: true,
      ensembleImages: [
        {
          label: "Ensemble ROC Curve",
          path: "/visuals/ensemble/ensemble_roc_curves.png",
        },
      ],
      combinedRocImages: [
        {
          label: "ROC Curve - All Models (CLR)",
          path: "/visuals/training/roc_all_models_clr.png",
        },
        {
          label: "ROC Curve - All Models (Rarefied)",
          path: "/visuals/training/roc_all_models_rarefied.png",
        },
      ],
      clrImages: [
        {
          label: "CLR - Heatmap AUC",
          path: "/visuals/clr/clr_heatmap_auc.png",
        },
        {
          label: "CLR - Heatmap F1",
          path: "/visuals/clr/clr_heatmap_f1.png",
        },
        {
          label: "CLR - ROC Curve",
          path: "/visuals/clr/clr_roc_curve.png",
        },
        {
          label: "CLR - Trend AUC",
          path: "/visuals/clr/clr_trend_auc.png",
        },
      ],
      rarefiedImages: [
        {
          label: "Rarefied - Heatmap AUC",
          path: "/visuals/rarefied/rarefied_heatmap_auc.png",
        },
        {
          label: "Rarefied - Heatmap F1",
          path: "/visuals/rarefied/rarefied_heatmap_f1.png",
        },
        {
          label: "Rarefied - ROC Curve",
          path: "/visuals/rarefied/rarefied_roc_curve.png",
        },
        {
          label: "Rarefied - Trend AUC",
          path: "/visuals/rarefied/rarefied_trend_auc.png",
        },
      ],
    };
  },
  methods: {
    openImage(img) {
      this.selectedImage = img;
      this.dialog = true;
    },
  },
};
</script>

<style scoped>
.hover-zoom {
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.hover-zoom:hover {
  transform: scale(1.03);
  box-shadow: 0 10px 24px rgba(33, 150, 243, 0.25);
}
</style>
