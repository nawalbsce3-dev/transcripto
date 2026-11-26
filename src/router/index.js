import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutPage.vue'
import FeaturesPage from '../views/FeaturesPage.vue'
import HowItWorksPage from '../views/HowItWorksPage.vue'
import AnalysisPage from '../views/AnalysisPage.vue'
import LandingPage from '../views/LandingPage.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage,
    meta: { title: 'Audio to Text' }
  },
  {
    path: '/transcribe',
    name: 'Home',
    component: HomePage,
    meta: { title: 'Transcribe' }
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage,
    meta: { title: 'About' }
  },
  {
    path: '/features',
    name: 'Features',
    component: FeaturesPage,
    meta: { title: 'Features' }
  },
  {
    path: '/how-it-works',
    name: 'HowItWorks',
    component: HowItWorksPage,
    meta: { title: 'How It Works' }
  },
  {
    path: '/analysis',
    name: 'Analysis',
    component: AnalysisPage,
    meta: { title: 'Analysis' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth'
      }
    } else {
      return { top: 0 }
    }
  }
})

export default router
