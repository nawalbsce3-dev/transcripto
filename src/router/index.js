import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutPage.vue'
import FeaturesPage from '../views/FeaturesPage.vue'
import HowItWorksPage from '../views/HowItWorksPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage
  },
  {
    path: '/features',
    name: 'Features',
    component: FeaturesPage
  },
  {
    path: '/how-it-works',
    name: 'HowItWorks',
    component: HowItWorksPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
