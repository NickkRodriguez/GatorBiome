import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import UploadView from '../views/UploadView.vue'
import ResultsView from '../views/ResultsView.vue'
import Dashboard from '../views/Dashboard.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/upload', name: 'upload', component: UploadView },
  {
    path: '/results',
    name: 'results',
    component: ResultsView,
    props: route => ({ resultData: route.params.data })
  },
  { path: '/dashboard', name: 'dashboard', component: Dashboard }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
