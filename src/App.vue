<template>
  <div class="app-frame" @keydown.esc="drawerOpen = false">
    <div class="app-shell">
      <AppSidebar
        :history="history"
        :active-history-id="activeHistoryId"
        :search="historySearch"
        :drawer-open="drawerOpen"
        :storage-error="storageError"
        @close="drawerOpen = false"
        @new-transcription="startNewTranscription"
        @select-history="selectHistory"
      />

      <div class="app-main">
        <AppHeader
          :page-title="pageTitle"
          :current-title="currentTitle"
          :search="historySearch"
          :menu-open="drawerOpen"
          @update:search="historySearch = $event"
          @open-menu="drawerOpen = true"
        />

        <main id="main-content" class="app-content">
          <router-view v-slot="{ Component }">
            <component
              :is="Component"
              v-if="route.name === 'Home'"
              :key="homeInstanceKey"
              :history-selection="selectedHistory"
              :history-search="historySearch"
              @transcription-completed="saveTranscription"
              @title-change="updateCurrentTitle"
              @clear-history-selection="activeHistoryId = ''"
            />
            <component
              :is="Component"
              v-else-if="route.name === 'Analysis'"
              :key="route.name"
              :history="history"
              :selected-history="selectedHistory"
              @select-history="selectHistoryForAnalysis"
            />
            <component v-else :is="Component" :key="route.name" />
          </router-view>
        </main>

        <footer class="site-footer">
          <div class="footer-inner">
            <div class="footer-brand-block">
              <BrandLink />
              <p>Clear words from the audio that matters.</p>
            </div>
            <nav class="footer-nav" aria-label="Footer navigation">
              <router-link to="/features">Features</router-link>
              <router-link to="/how-it-works">How it works</router-link>
              <router-link to="/about">About</router-link>
            </nav>
            <div class="footer-note">
              <span class="footer-note-dot" aria-hidden="true"></span>
              <span>Uploads are removed after processing.</span>
            </div>
          </div>
          <div class="footer-bottom">
            <span>© 2026 Transcripto · Portfolio project</span>
            <span>Built with Vue, Flask &amp; OpenAI Whisper</span>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppHeader from './components/AppHeader.vue'
import AppSidebar from './components/AppSidebar.vue'
import BrandLink from './components/BrandLink.vue'

const HISTORY_STORAGE_KEY = 'transcripto.transcription-history.v1'
const route = useRoute()
const router = useRouter()
const storageError = ref('')
const history = ref([])
const historySearch = ref('')
const activeHistoryId = ref('')
const currentTitle = ref('')
const drawerOpen = ref(false)
const homeInstanceKey = ref(0)

const readHistory = () => {
  try {
    const saved = localStorage.getItem(HISTORY_STORAGE_KEY)
    if (!saved) return []
    const parsed = JSON.parse(saved)
    if (!Array.isArray(parsed)) throw new TypeError('History data must be a list.')
    return parsed.filter(item =>
      item &&
      typeof item.id === 'string' &&
      typeof item.title === 'string' &&
      typeof item.createdAt === 'string' &&
      typeof item.text === 'string' &&
      Array.isArray(item.segments)
    )
  } catch (error) {
    console.warn('Could not read saved transcription history:', error)
    storageError.value = 'Saved history could not be read from this browser.'
    return []
  }
}

history.value = readHistory()

watch(history, (items) => {
  try {
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(items))
    storageError.value = ''
  } catch (error) {
    console.error('Could not save transcription history:', error)
    storageError.value = 'History could not be saved in this browser.'
  }
}, { deep: true })

const pageTitles = {
  Home: 'Transcribe',
  Analysis: 'Analysis',
  Features: 'Features',
  HowItWorks: 'How It Works',
  About: 'About'
}
const pageTitle = computed(() => pageTitles[route.name] || 'Transcripto')
const selectedHistory = computed(() =>
  history.value.find(item => item.id === activeHistoryId.value) || null
)

const saveTranscription = ({ title, text, segments }) => {
  const item = {
    id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    title: title || 'Untitled transcription',
    createdAt: new Date().toISOString(),
    text,
    segments
  }
  history.value = [item, ...history.value.filter(saved => saved.title !== item.title)].slice(0, 20)
  activeHistoryId.value = item.id
  currentTitle.value = item.title
}

const updateCurrentTitle = (title) => {
  currentTitle.value = title
  const saved = history.value.find(item => item.id === activeHistoryId.value)
  if (saved) saved.title = title
}

const selectHistory = async (item) => {
  activeHistoryId.value = item.id
  currentTitle.value = item.title
  drawerOpen.value = false
  if (route.name !== 'Home') await router.push('/')
}

const selectHistoryForAnalysis = (id) => {
  const item = history.value.find(saved => saved.id === id)
  if (!item) return
  activeHistoryId.value = item.id
  currentTitle.value = item.title
}

const startNewTranscription = async () => {
  activeHistoryId.value = ''
  currentTitle.value = 'New Transcription'
  historySearch.value = ''
  drawerOpen.value = false
  homeInstanceKey.value += 1
  if (route.name !== 'Home' || route.hash) await router.push('/')
}
</script>
