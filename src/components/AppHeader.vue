<template>
  <header class="workspace-header">
    <div class="workspace-header-title">
      <button ref="menuButton" class="mobile-menu-button" type="button" aria-label="Open navigation" aria-controls="app-sidebar" :aria-expanded="menuOpen" @click="$emit('open-menu')">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
      </button>
      <div class="workspace-heading-copy">
        <p v-if="pageTitle === 'Transcribe'" class="workspace-breadcrumb">
          <span>Transcribe</span><span aria-hidden="true">/</span><span>Transcribe List</span>
          <span aria-hidden="true">/</span><strong>{{ currentTitle || pageTitle }}</strong>
        </p>
        <p v-else class="workspace-breadcrumb">
          <span>Transcripto</span><span aria-hidden="true">/</span><strong>{{ pageTitle }}</strong>
        </p>
        <h1>{{ pageTitle === 'Transcribe' ? (currentTitle || 'New Transcription') : pageTitle }}</h1>
      </div>
    </div>
    <div class="workspace-header-actions">
      <label class="history-search">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.8" cy="10.8" r="6.8" /><path d="m16 16 4.5 4.5" /></svg>
        <input :value="search" type="search" placeholder="Search transcriptions" aria-label="Search saved transcriptions" @input="$emit('update:search', $event.target.value)" />
      </label>
      <button class="header-icon-button notification-button" type="button" aria-label="Notifications: no new notifications" title="No new notifications">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 9a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M10 21h4" /></svg>
        <span aria-hidden="true"></span>
      </button>
      <div class="user-avatar" aria-label="Transcripto workspace" title="Transcripto workspace">T</div>
    </div>
  </header>
</template>

<script>
import { nextTick, ref, watch } from 'vue'

export default {
  name: 'AppHeader',
  props: {
    pageTitle: { type: String, default: 'Transcripto' },
    currentTitle: { type: String, default: '' },
    search: { type: String, default: '' },
    menuOpen: { type: Boolean, default: false }
  },
  emits: ['open-menu', 'update:search'],
  setup(props) {
    const menuButton = ref(null)
    watch(() => props.menuOpen, async (open, wasOpen) => {
      if (!open && wasOpen) {
        await nextTick()
        menuButton.value?.focus()
      }
    })
    return { menuButton }
  }
}
</script>
