<template>
    <v-container class="py-10">
      <v-row justify="center" class="mb-10">
        <v-col cols="12" md="10">
          <h1 class="text-h4 font-weight-bold text-center text-primary mb-2">About GatorBiome</h1>
          <p class="text-center text-grey-darken-1">
            Built by UF students, GatorBiome is a modular ML platform to predict disease from microbiome data using 100-run evaluations and state-of-the-art feature engineering.
          </p>
        </v-col>
      </v-row>
  
      <!-- Project Overview -->
      <v-row justify="center" class="mb-8">
        <v-col cols="12" md="10">
          <v-card elevation="3" class="pa-6 hoverable">
            <v-card-title class="text-h6 font-weight-bold mb-2">
              <v-icon class="me-2" color="primary">mdi-information-outline</v-icon> Project Overview
            </v-card-title>
            <v-card-text class="text-body-1">
              GatorBiome is a modular machine learning pipeline built to predict diseases, such as colon cancer, using gut microbiome data. Initially focused on Autism Spectrum Disorder (ASD), the project pivoted to broader disease prediction due to public dataset limitations. Now using advisor-aligned datasets, the system supports flexible feature engineering and rich visualization capabilities.
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
  
      <!-- Team Responsibilities -->
      <v-row justify="center" class="mb-8">
        <v-col cols="12" md="10">
          <v-card elevation="3" class="pa-6 hoverable">
            <v-card-title class="text-h6 font-weight-bold mb-2">
              <v-icon class="me-2" color="primary">mdi-account-group</v-icon> Team Responsibilities
            </v-card-title>
            <v-list dense>
              <v-list-item v-for="(member, index) in team" :key="index">
                <v-list-item-content>
                  <v-list-item-title class="text-body-1">
                    <strong>{{ member.name }}:</strong> {{ member.role }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
  
      <!-- Highlights -->
      <v-row justify="center" class="mb-4">
        <v-col cols="12" md="10">
          <v-card elevation="3" class="pa-6 hoverable">
            <v-card-title class="text-h6 font-weight-bold mb-4">
              <v-icon class="me-2" color="primary">mdi-star-circle-outline</v-icon> Pipeline Highlights
            </v-card-title>
            <v-row dense>
              <v-col cols="12" sm="6" v-for="(item, index) in highlights" :key="index">
                <v-card flat class="pa-4 mb-4 rounded border hoverable" elevation="1">
                  <v-card-title class="text-primary font-weight-medium text-subtitle-1">
                    <v-icon class="me-2" color="primary">mdi-check-circle</v-icon> {{ item.title }}
                  </v-card-title>
                  <v-card-text class="text-body-2">{{ item.description }}</v-card-text>
                </v-card>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "AboutPage",
    data() {
      return {
        team: [
          {
            name: "Nick Rodriguez – Team Lead",
            role: "ML pipeline, system architecture, documentation, and project direction."
          },
          {
            name: "Connor McLoon",
            role: "Model training, hyperparameter tuning, and integration support."
          },
          {
            name: "Lachyn Almazova – Frontend Lead",
            role: "Vue.js dashboard implementation and visualization integration."
          },
          {
            name: "David Alvarez – Backend Lead",
            role: "Django REST API and dashboard endpoint development."
          },
          {
            name: "Advisor – Fatemeh Tavassoli",
            role: "Microbiome data expert and research methodology guidance."
          }
        ],
        highlights: [
          {
            title: "Multi-dataset Support",
            description: "Supports rarefied and CLR-transformed gut microbiome datasets."
          },
          {
            title: "Flexible Feature Engineering",
            description: "Chi², Mutual Information, ANOVA, PCA, UMAP, KPCA."
          },
          {
            title: "Robust Evaluation",
            description: "100-run cross-validation with model selection by AUC."
          },
          {
            title: "Vue 3 Frontend",
            description: "Interactive and modular dashboard built with Composition API."
          },
          {
            title: "Django REST API",
            description: "Scalable backend exposing endpoints for model metrics and datasets."
          }
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  .hoverable {
    transition: 0.3s ease;
  }
  .hoverable:hover {
    transform: scale(1.01);
  }
  </style>
  