import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Dashboard from '../views/Dashboard.vue'
import AboutPage from '../views/About.vue'
import VisualizationsPage from '../views/Visualizations.vue'
import ModelsPage from '../views/Models.vue'
import DatasetsPage from '../views/Datasets.vue'
import ModelPrediction from '../views/ModelPrediction.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/dashboard', name: 'dashboard', component: Dashboard },
  { path: '/about', name: 'about', component: AboutPage },
  { path: '/visualizations', name: 'visualizations', component: VisualizationsPage },
  { path: '/models', name: 'models', component: ModelsPage },
  { path: '/datasets', name: 'datasets', component: DatasetsPage },
  { path: '/model-prediction', name: 'model-prediction', component: ModelPrediction }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
