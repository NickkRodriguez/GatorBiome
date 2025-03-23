import { createRouter, createWebHistory } from 'vue-router'
import UploadView from '../views/UploadView.vue'
import ResultsView from '../views/ResultsView.vue'

const routes = [
  { path: '/', name: 'upload', component: UploadView },
  {
    path: '/results',
    name: 'results',
    component: ResultsView,
    props: route => ({ resultData: route.params.data })
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

