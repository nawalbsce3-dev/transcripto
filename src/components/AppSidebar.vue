<template>
  <div v-if="drawerOpen" class="sidebar-backdrop" @click="$emit('close')"></div>
  <aside id="app-sidebar" class="app-sidebar" :class="{ 'is-open': drawerOpen }" aria-label="Application sidebar">
    <div class="sidebar-brand-row">
      <BrandLink />
      <button ref="closeButton" class="sidebar-close" type="button" aria-label="Close navigation" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg>
      </button>
    </div>

    <nav class="sidebar-nav" aria-label="Main navigation">
      <p class="sidebar-label">Menu</p>
      <router-link to="/about" class="sidebar-link" active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM8 9h8M8 13h5" /></svg>
        Letters
      </router-link>
      <router-link to="/" class="sidebar-link" exact-active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM8 9h8M8 13h5" /></svg>
        Transcribe
      </router-link>
      <router-link to="/features" class="sidebar-link" active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM8 9h8M8 13h5" /></svg>
        Features
      </router-link>
      <router-link to="/analysis" class="sidebar-link" active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19V5m0 14h16" /><path d="m7 15 3-4 3 2 5-7" /></svg>
        Analysis
      </router-link>
      <router-link to="/how-it-works" class="sidebar-link" active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="m10 8 6 4-6 4z" /></svg>
        How It Works
      </router-link>
      <router-link to="/about" class="sidebar-link" active-class="is-active" @click="$emit('close')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="M12 11v5m0-8h.01" /></svg>
        About
      </router-link>
    </nav>

    <section class="sidebar-history" aria-labelledby="history-heading">
      <div class="sidebar-history-heading">
        <h2 id="history-heading" class="sidebar-label">Transcribe List</h2>
        <span>{{ filteredHistory.length }}</span>
      </div>
      <div v-if="filteredHistory.length" class="history-list">
        <button
          v-for="item in filteredHistory"
          :key="item.id"
          class="history-item"
          :class="{ 'is-active': item.id === activeHistoryId }"
          type="button"
          :aria-current="item.id === activeHistoryId ? 'page' : undefined"
          @click="$emit('select-history', item)"
        >
          <span class="history-item-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24"><path d="M9 18V5l11-2v13" /><circle cx="6" cy="18" r="3" /><circle cx="17" cy="16" r="3" /></svg>
          </span>
          <span class="history-item-title">{{ item.title }}</span>
          <span class="history-item-date">{{ formatDate(item.createdAt) }}</span>
        </button>
      </div>
      <p v-else class="history-empty">
        {{ search ? 'No saved transcripts match your search.' : 'Completed transcripts you save in this browser will appear here.' }}
      </p>
      <p v-if="storageError" class="history-storage-error" role="status">{{ storageError }}</p>
      <button class="new-transcription" type="button" @click="$emit('new-transcription')">
        <span aria-hidden="true">＋</span> New Transcribe
      </button>
      <p class="history-local-note">Saved only in this browser</p>
    </section>

    <div class="sidebar-spacer"></div>

    <nav class="sidebar-utilities" aria-label="Help and settings">
      <a class="sidebar-utility" href="https://github.com/nawalbsce3-dev/transcripto/issues" target="_blank" rel="noreferrer">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="M9.6 9a2.5 2.5 0 1 1 4.2 1.8c-1.2 1-1.8 1.3-1.8 2.7m0 3h.01" /></svg>
        Help &amp; Support
      </a>
      <router-link class="sidebar-utility" to="/about">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="M12 11v5m0-8h.01" /></svg>
        About &amp; privacy
      </router-link>
    </nav>
  </aside>
</template>

<script>
import { computed, nextTick, ref, watch } from 'vue'
import BrandLink from './BrandLink.vue'

export default {
  name: 'AppSidebar',
  components: { BrandLink },
  props: {
    history: { type: Array, default: () => [] },
    activeHistoryId: { type: String, default: '' },
    search: { type: String, default: '' },
    drawerOpen: { type: Boolean, default: false },
    storageError: { type: String, default: '' }
  },
  emits: ['close', 'new-transcription', 'select-history'],
  setup(props) {
    const closeButton = ref(null)
    const filteredHistory = computed(() => {
      const query = props.search.trim().toLocaleLowerCase()
      if (!query) return props.history
      return props.history.filter(item =>
        item.title.toLocaleLowerCase().includes(query) ||
        item.text.toLocaleLowerCase().includes(query)
      )
    })

    const formatDate = (value) => {
      const date = new Date(value)
      const today = new Date()
      const yesterday = new Date()
      yesterday.setDate(today.getDate() - 1)
      if (date.toDateString() === today.toDateString()) return 'Today'
      if (date.toDateString() === yesterday.toDateString()) return 'Yesterday'
      return new Intl.DateTimeFormat(undefined, { month: '2-digit', day: '2-digit' }).format(date)
    }

    watch(() => props.drawerOpen, async (open) => {
      if (open) {
        await nextTick()
        closeButton.value?.focus()
      }
    })

    return { closeButton, filteredHistory, formatDate }
  }
}
</script>
