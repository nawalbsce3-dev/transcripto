<template>
  <div class="analysis-page">
    <section class="analysis-intro">
      <p class="analysis-eyebrow">TRANSCRIPT OVERVIEW</p>
      <h2>Analysis</h2>
      <p>Simple metrics from your locally saved transcript. No extra AI analysis is implied.</p>
    </section>

    <section v-if="transcript" class="analysis-card" aria-labelledby="analysis-transcript-title">
      <div class="analysis-card-header">
        <div>
          <p class="analysis-label">Selected transcript</p>
          <h3 id="analysis-transcript-title">{{ transcript.title }}</h3>
        </div>
        <label class="analysis-select-label">
          <span class="visually-hidden">Choose a saved transcript</span>
          <select :value="transcript.id" @change="$emit('select-history', $event.target.value)">
            <option v-for="item in history" :key="item.id" :value="item.id">{{ item.title }}</option>
          </select>
        </label>
      </div>

      <div class="analysis-metrics">
        <article class="analysis-metric">
          <span class="analysis-metric-icon" aria-hidden="true">Aa</span>
          <p>Word count</p>
          <strong>{{ wordCount.toLocaleString() }}</strong>
        </article>
        <article class="analysis-metric">
          <span class="analysis-metric-icon" aria-hidden="true">≋</span>
          <p>Timestamped segments</p>
          <strong>{{ segmentCount.toLocaleString() }}</strong>
        </article>
        <article class="analysis-metric">
          <span class="analysis-metric-icon" aria-hidden="true">◷</span>
          <p>Transcript duration</p>
          <strong>{{ duration }}</strong>
        </article>
        <article class="analysis-metric">
          <span class="analysis-metric-icon" aria-hidden="true">↗</span>
          <p>Average words per segment</p>
          <strong>{{ averageWords }}</strong>
        </article>
      </div>

      <p class="analysis-disclaimer">
        Duration and segment metrics are calculated from the transcript timestamps. Speaker separation, when shown in the transcript, is estimated from pauses.
      </p>
    </section>

    <section v-else class="analysis-empty">
      <span class="analysis-empty-icon" aria-hidden="true">∑</span>
      <h3>No saved transcript to analyze yet</h3>
      <p>Transcribe an audio file first. Completed transcripts are saved only in this browser.</p>
      <router-link to="/" class="analysis-cta">Start transcribing</router-link>
    </section>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'AnalysisPage',
  props: {
    history: { type: Array, default: () => [] },
    selectedHistory: { type: Object, default: null }
  },
  emits: ['select-history'],
  setup(props) {
    const transcript = computed(() => props.selectedHistory || props.history[0] || null)
    const words = computed(() => transcript.value?.text.trim().split(/\s+/).filter(Boolean) || [])
    const segments = computed(() => transcript.value?.segments || [])
    const wordCount = computed(() => words.value.length)
    const segmentCount = computed(() => segments.value.length)
    const averageWords = computed(() => segmentCount.value
      ? (wordCount.value / segmentCount.value).toFixed(1)
      : '—')
    const duration = computed(() => {
      const lastEnd = segments.value.reduce((latest, segment) =>
        Math.max(latest, Number(segment.end) || 0), 0)
      if (!lastEnd) return '—'
      const minutes = Math.floor(lastEnd / 60)
      const seconds = Math.floor(lastEnd % 60).toString().padStart(2, '0')
      return `${minutes}:${seconds}`
    })

    return { transcript, wordCount, segmentCount, averageWords, duration }
  }
}
</script>
