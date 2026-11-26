<template>
  <div class="an-page">
    <!-- Intro -->
    <section class="an-intro">
      <p class="an-eyebrow">TRANSCRIPT OVERVIEW</p>
      <h2>Analysis</h2>
      <p>
        Metrics calculated locally from your saved transcript and its timestamps.
        Nothing is sent anywhere and no extra AI analysis is implied.
      </p>
    </section>

    <template v-if="transcript">
      <!-- Header card: selector + actions -->
      <section class="an-card an-header" aria-labelledby="an-title">
        <div class="an-header-main">
          <p class="an-label">Selected transcript</p>
          <h3 id="an-title">{{ transcript.title }}</h3>
          <ul class="an-meta">
            <li v-if="createdLabel">
              <span aria-hidden="true">🗓</span> {{ createdLabel }}
            </li>
            <li v-if="transcript.language">
              <span aria-hidden="true">🌐</span> {{ String(transcript.language).toUpperCase() }}
            </li>
            <li><span aria-hidden="true">⏱</span> {{ readingTime }} read</li>
            <li>
              <span class="an-pill" :class="`an-pill--${paceTone}`">{{ paceLabel }}</span>
            </li>
          </ul>
        </div>

        <div class="an-header-actions">
          <label class="an-select-label">
            <span class="an-visually-hidden">Choose a saved transcript</span>
            <select :value="transcript.id" @change="$emit('select-history', $event.target.value)">
              <option v-for="item in history" :key="item.id" :value="item.id">{{ item.title }}</option>
            </select>
          </label>
          <div class="an-btn-row">
            <button type="button" class="an-btn" @click="copySummary">Copy summary</button>
            <button type="button" class="an-btn" :disabled="!segmentCount" @click="downloadCsv">
              Export CSV
            </button>
            <button type="button" class="an-btn an-btn--primary" @click="downloadJson">
              Export JSON
            </button>
          </div>
        </div>
      </section>

      <p class="an-toast" role="status" aria-live="polite">{{ toast }}</p>

      <!-- KPI grid -->
      <section class="an-metrics" aria-label="Key metrics">
        <article v-for="metric in metrics" :key="metric.label" class="an-metric">
          <div class="an-metric-top">
            <span class="an-metric-icon" aria-hidden="true">{{ metric.icon }}</span>
            <p>{{ metric.label }}</p>
          </div>
          <strong>{{ metric.value }}</strong>
          <span class="an-metric-hint">{{ metric.hint }}</span>
        </article>
      </section>

      <div class="an-grid">
        <!-- Pacing chart -->
        <section class="an-card an-span-2" aria-labelledby="an-pacing-title">
          <div class="an-card-head">
            <div>
              <h4 id="an-pacing-title">Speaking pace over time</h4>
              <p class="an-sub">Words per minute, segment by segment (average {{ wpm }} WPM)</p>
            </div>
          </div>

          <div v-if="bars.length" class="an-chart">
            <svg
              :viewBox="`0 0 ${chart.width} ${chart.height}`"
              preserveAspectRatio="none"
              role="img"
              :aria-label="`Bar chart of speaking pace. Average ${wpm} words per minute, peak ${peakWpm}.`"
            >
              <line
                class="an-chart-avg"
                x1="0"
                :x2="chart.width"
                :y1="avgLineY"
                :y2="avgLineY"
              />
              <rect
                v-for="bar in bars"
                :key="bar.index"
                class="an-chart-bar"
                :x="bar.x"
                :y="bar.y"
                :width="bar.w"
                :height="bar.h"
                rx="2"
              >
                <title>{{ bar.label }}</title>
              </rect>
            </svg>
            <div class="an-chart-axis">
              <span>0:00</span>
              <span>{{ formatTime(totalSeconds / 2) }}</span>
              <span>{{ duration }}</span>
            </div>
          </div>
          <p v-else class="an-muted">Timestamped segments are needed to draw this chart.</p>
        </section>

        <!-- Insights -->
        <section class="an-card" aria-labelledby="an-insights-title">
          <h4 id="an-insights-title">Highlights</h4>
          <ul class="an-insights">
            <li v-for="line in insights" :key="line">{{ line }}</li>
          </ul>
        </section>

        <!-- Keywords -->
        <section class="an-card" aria-labelledby="an-keywords-title">
          <h4 id="an-keywords-title">Most frequent terms</h4>
          <p class="an-sub">Common filler words are ignored</p>
          <ul v-if="keywords.length" class="an-keywords">
            <li v-for="word in keywords" :key="word.term">
              <span class="an-keyword-term">{{ word.term }}</span>
              <span class="an-keyword-bar" aria-hidden="true">
                <span :style="{ width: word.percent + '%' }"></span>
              </span>
              <span class="an-keyword-count">{{ word.count }}</span>
            </li>
          </ul>
          <p v-else class="an-muted">Not enough text to find repeated terms.</p>
        </section>

        <!-- Pauses -->
        <section class="an-card" aria-labelledby="an-pauses-title">
          <h4 id="an-pauses-title">Talk vs. silence</h4>
          <div class="an-split" role="img" :aria-label="`${talkPercent}% speech, ${100 - talkPercent}% silence`">
            <span class="an-split-talk" :style="{ width: talkPercent + '%' }"></span>
          </div>
          <dl class="an-stats">
            <div><dt>Speech time</dt><dd>{{ formatTime(speechSeconds) }}</dd></div>
            <div><dt>Silence</dt><dd>{{ formatTime(silenceSeconds) }}</dd></div>
            <div><dt>Longest pause</dt><dd>{{ longestPause ? formatTime(longestPause.length) : '—' }}</dd></div>
          </dl>
          <ul v-if="topPauses.length" class="an-pauses">
            <li v-for="pause in topPauses" :key="pause.at">
              <span>at {{ formatTime(pause.at) }}</span>
              <strong>{{ pause.length.toFixed(1) }}s</strong>
            </li>
          </ul>
        </section>

        <!-- Segment length distribution -->
        <section class="an-card" aria-labelledby="an-dist-title">
          <h4 id="an-dist-title">Segment length</h4>
          <p class="an-sub">How long each timestamped segment runs</p>
          <ul v-if="segmentCount" class="an-dist">
            <li v-for="bucket in distribution" :key="bucket.label">
              <span>{{ bucket.label }}</span>
              <span class="an-keyword-bar" aria-hidden="true">
                <span :style="{ width: bucket.percent + '%' }"></span>
              </span>
              <span class="an-keyword-count">{{ bucket.count }}</span>
            </li>
          </ul>
          <p v-else class="an-muted">No segments available.</p>
        </section>

        <!-- Segment table -->
        <section class="an-card an-span-3" aria-labelledby="an-table-title">
          <div class="an-card-head">
            <div>
              <h4 id="an-table-title">Segment breakdown</h4>
              <p class="an-sub">{{ segmentCount.toLocaleString() }} segments in order</p>
            </div>
            <div class="an-btn-row">
              <button
                type="button"
                class="an-btn"
                :class="{ 'an-btn--active': sortMode === 'time' }"
                @click="sortMode = 'time'"
              >
                By time
              </button>
              <button
                type="button"
                class="an-btn"
                :class="{ 'an-btn--active': sortMode === 'words' }"
                @click="sortMode = 'words'"
              >
                By length
              </button>
            </div>
          </div>

          <div v-if="visibleRows.length" class="an-table-wrap">
            <table class="an-table">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Time</th>
                  <th scope="col">Words</th>
                  <th scope="col">WPM</th>
                  <th scope="col">Text</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="row in visibleRows" :key="row.index">
                  <td>{{ row.index + 1 }}</td>
                  <td class="an-nowrap">{{ formatTime(row.start) }} – {{ formatTime(row.end) }}</td>
                  <td>{{ row.words }}</td>
                  <td>{{ row.wpm || '—' }}</td>
                  <td class="an-snippet">{{ row.text }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p v-else class="an-muted">No timestamped segments for this transcript.</p>

          <button
            v-if="rows.length > 8"
            type="button"
            class="an-btn an-btn--ghost"
            @click="showAll = !showAll"
          >
            {{ showAll ? 'Show fewer' : `Show all ${rows.length} segments` }}
          </button>
        </section>
      </div>

      <p class="an-disclaimer">
        Duration, pace and pause metrics come from the transcript timestamps. Word counts use simple
        whitespace splitting, and speaker separation, when shown in the transcript, is estimated from
        pauses. Treat all values as approximate.
      </p>
    </template>

    <!-- Empty -->
    <section v-else class="an-empty">
      <span class="an-empty-icon" aria-hidden="true">∑</span>
      <h3>No saved transcript to analyze yet</h3>
      <p>Transcribe an audio file first. Completed transcripts are saved only in this browser.</p>
      <router-link to="/transcribe" class="an-cta">Start transcribing</router-link>
    </section>
  </div>
</template>

<script>
import { computed, ref } from 'vue'

const STOPWORDS = new Set(
  (
    'a about above after again all also am an and any are as at be because been before being below between ' +
    'both but by can could did do does doing down during each few for from further had has have having he her ' +
    'here hers him his how i if in into is it its just like me more most my no nor not now of off on once only ' +
    'or other our out over own same she should so some such than that the their them then there these they ' +
    'this those through to too under until up very was we were what when where which while who whom why will ' +
    'with would you your yours yeah okay um uh gonna got get going know think really right well one two'
  ).split(' ')
)

const WORDS_PER_MINUTE_READING = 238
const MAX_BARS = 60

const countWords = (text) => (text || '').trim().split(/\s+/).filter(Boolean).length

export default {
  name: 'AnalysisPage',
  props: {
    history: { type: Array, default: () => [] },
    selectedHistory: { type: Object, default: null }
  },
  emits: ['select-history'],
  setup(props) {
    const toast = ref('')
    const sortMode = ref('time')
    const showAll = ref(false)
    let toastTimer = null

    /* ---------- Base data ---------- */
    const transcript = computed(() => props.selectedHistory || props.history[0] || null)
    const text = computed(() => transcript.value?.text || '')
    const words = computed(() => text.value.trim().split(/\s+/).filter(Boolean))
    const segments = computed(() =>
      (transcript.value?.segments || [])
        .map((segment) => ({
          start: Number(segment.start) || 0,
          end: Number(segment.end) || 0,
          text: (segment.text || '').trim()
        }))
        .sort((a, b) => a.start - b.start)
    )

    const wordCount = computed(() => words.value.length)
    const segmentCount = computed(() => segments.value.length)
    const totalSeconds = computed(() =>
      segments.value.reduce((latest, segment) => Math.max(latest, segment.end), 0)
    )

    /* ---------- Formatting ---------- */
    const formatTime = (value) => {
      const total = Math.max(0, Math.floor(Number(value) || 0))
      const hours = Math.floor(total / 3600)
      const minutes = Math.floor((total % 3600) / 60)
      const seconds = (total % 60).toString().padStart(2, '0')
      return hours
        ? `${hours}:${minutes.toString().padStart(2, '0')}:${seconds}`
        : `${minutes}:${seconds}`
    }

    const duration = computed(() => (totalSeconds.value ? formatTime(totalSeconds.value) : '—'))

    const createdLabel = computed(() => {
      const raw = transcript.value?.createdAt || transcript.value?.date
      if (!raw) return ''
      const date = new Date(raw)
      return Number.isNaN(date.getTime())
        ? ''
        : date.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' })
    })

    /* ---------- Core metrics ---------- */
    const averageWords = computed(() =>
      segmentCount.value ? (wordCount.value / segmentCount.value).toFixed(1) : '—'
    )

    const wpm = computed(() =>
      totalSeconds.value ? Math.round(wordCount.value / (totalSeconds.value / 60)) : 0
    )

    const readingTime = computed(() => {
      const minutes = wordCount.value / WORDS_PER_MINUTE_READING
      if (minutes < 1) return '< 1 min'
      return `${Math.round(minutes)} min`
    })

    const uniqueWords = computed(() => {
      const set = new Set(
        words.value.map((word) => word.toLowerCase().replace(/[^\p{L}\p{N}'-]/gu, '')).filter(Boolean)
      )
      return set.size
    })

    const vocabularyRichness = computed(() =>
      wordCount.value ? Math.round((uniqueWords.value / wordCount.value) * 100) : 0
    )

    const sentenceCount = computed(
      () => (text.value.match(/[^.!?]+[.!?]+/g) || []).length || (wordCount.value ? 1 : 0)
    )

    const averageSentenceLength = computed(() =>
      sentenceCount.value ? (wordCount.value / sentenceCount.value).toFixed(1) : '—'
    )

    /* ---------- Pace label ---------- */
    const paceLabel = computed(() => {
      if (!wpm.value) return 'Pace unavailable'
      if (wpm.value < 110) return 'Slow pace'
      if (wpm.value <= 160) return 'Conversational pace'
      return 'Fast pace'
    })
    const paceTone = computed(() => {
      if (!wpm.value) return 'neutral'
      if (wpm.value < 110) return 'warn'
      if (wpm.value <= 160) return 'good'
      return 'info'
    })

    /* ---------- Segment rows ---------- */
    const rows = computed(() => {
      const mapped = segments.value.map((segment, index) => {
        const length = Math.max(segment.end - segment.start, 0)
        const segWords = countWords(segment.text)
        return {
          index,
          start: segment.start,
          end: segment.end,
          length,
          words: segWords,
          wpm: length > 0 ? Math.round(segWords / (length / 60)) : 0,
          text: segment.text
        }
      })
      return sortMode.value === 'words' ? [...mapped].sort((a, b) => b.words - a.words) : mapped
    })

    const visibleRows = computed(() => (showAll.value ? rows.value : rows.value.slice(0, 8)))

    /* ---------- Speech vs. silence ---------- */
    const speechSeconds = computed(() =>
      segments.value.reduce((sum, segment) => sum + Math.max(segment.end - segment.start, 0), 0)
    )
    const silenceSeconds = computed(() => Math.max(totalSeconds.value - speechSeconds.value, 0))
    const talkPercent = computed(() =>
      totalSeconds.value
        ? Math.min(100, Math.round((speechSeconds.value / totalSeconds.value) * 100))
        : 0
    )

    const pauses = computed(() => {
      const found = []
      for (let i = 1; i < segments.value.length; i += 1) {
        const gap = segments.value[i].start - segments.value[i - 1].end
        if (gap > 0.5) found.push({ at: segments.value[i - 1].end, length: gap })
      }
      return found
    })
    const topPauses = computed(() => [...pauses.value].sort((a, b) => b.length - a.length).slice(0, 3))
    const longestPause = computed(() => topPauses.value[0] || null)

    /* ---------- Keywords ---------- */
    const keywords = computed(() => {
      const counts = new Map()
      words.value.forEach((word) => {
        const term = word.toLowerCase().replace(/[^\p{L}\p{N}'-]/gu, '')
        if (term.length < 3 || STOPWORDS.has(term) || /^\d+$/.test(term)) return
        counts.set(term, (counts.get(term) || 0) + 1)
      })
      const top = [...counts.entries()]
        .filter(([, count]) => count > 1)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 8)
      const max = top[0]?.[1] || 1
      return top.map(([term, count]) => ({ term, count, percent: Math.round((count / max) * 100) }))
    })

    /* ---------- Segment length distribution ---------- */
    const distribution = computed(() => {
      const buckets = [
        { label: '< 3s', test: (s) => s < 3, count: 0 },
        { label: '3 – 6s', test: (s) => s >= 3 && s < 6, count: 0 },
        { label: '6 – 10s', test: (s) => s >= 6 && s < 10, count: 0 },
        { label: '10s +', test: (s) => s >= 10, count: 0 }
      ]
      rows.value.forEach((row) => {
        const bucket = buckets.find((item) => item.test(row.length))
        if (bucket) bucket.count += 1
      })
      const max = Math.max(...buckets.map((bucket) => bucket.count), 1)
      return buckets.map(({ label, count }) => ({
        label,
        count,
        percent: Math.round((count / max) * 100)
      }))
    })

    /* ---------- Pacing chart ---------- */
    const chart = { width: 600, height: 140 }

    const bars = computed(() => {
      const source = [...rows.value].sort((a, b) => a.index - b.index).filter((row) => row.length > 0)
      if (!source.length) return []

      const bucketSize = Math.ceil(source.length / MAX_BARS)
      const grouped = []
      for (let i = 0; i < source.length; i += bucketSize) {
        const slice = source.slice(i, i + bucketSize)
        const sliceWords = slice.reduce((sum, row) => sum + row.words, 0)
        const sliceSeconds = slice.reduce((sum, row) => sum + row.length, 0)
        grouped.push({
          start: slice[0].start,
          end: slice[slice.length - 1].end,
          wpm: sliceSeconds ? Math.round(sliceWords / (sliceSeconds / 60)) : 0
        })
      }

      const max = Math.max(...grouped.map((item) => item.wpm), wpm.value, 1)
      const slot = chart.width / grouped.length
      const gap = Math.min(3, slot * 0.2)
      return grouped.map((item, index) => {
        const h = Math.max((item.wpm / max) * (chart.height - 8), 2)
        return {
          index,
          x: index * slot + gap / 2,
          w: Math.max(slot - gap, 1),
          h,
          y: chart.height - h,
          label: `${formatTime(item.start)} – ${formatTime(item.end)}: ${item.wpm} WPM`,
          wpm: item.wpm
        }
      })
    })

    const peakWpm = computed(() => Math.max(...bars.value.map((bar) => bar.wpm), 0))
    const avgLineY = computed(() => {
      const max = Math.max(peakWpm.value, wpm.value, 1)
      return chart.height - (wpm.value / max) * (chart.height - 8)
    })

    /* ---------- KPI cards + highlights ---------- */
    const metrics = computed(() => [
      { icon: 'Aa', label: 'Word count', value: wordCount.value.toLocaleString(), hint: `${uniqueWords.value.toLocaleString()} unique words` },
      { icon: '≋', label: 'Timestamped segments', value: segmentCount.value.toLocaleString(), hint: 'From saved timestamps' },
      { icon: '◷', label: 'Transcript duration', value: duration.value, hint: `${formatTime(speechSeconds.value)} of speech` },
      { icon: '↗', label: 'Avg. words per segment', value: averageWords.value, hint: `${averageSentenceLength.value} words per sentence` },
      { icon: '⚡', label: 'Speaking rate', value: wpm.value ? `${wpm.value} WPM` : '—', hint: paceLabel.value },
      { icon: '◐', label: 'Vocabulary variety', value: wordCount.value ? `${vocabularyRichness.value}%` : '—', hint: 'Unique ÷ total words' },
      { icon: '¶', label: 'Sentences', value: sentenceCount.value.toLocaleString(), hint: 'Estimated from punctuation' },
      { icon: '⏸', label: 'Pauses over 0.5s', value: pauses.value.length.toLocaleString(), hint: longestPause.value ? `Longest ${longestPause.value.length.toFixed(1)}s` : 'None detected' }
    ])

    const insights = computed(() => {
      const lines = []
      if (wpm.value) lines.push(`Average speaking rate is ${wpm.value} words per minute (${paceLabel.value.toLowerCase()}).`)
      if (totalSeconds.value) lines.push(`${talkPercent.value}% of the recording contains speech; ${formatTime(silenceSeconds.value)} is silence between segments.`)
      if (keywords.value[0]) lines.push(`"${keywords.value[0].term}" is the most repeated term, used ${keywords.value[0].count} times.`)
      if (longestPause.value) lines.push(`The longest pause is ${longestPause.value.length.toFixed(1)}s, starting at ${formatTime(longestPause.value.at)}.`)
      if (peakWpm.value && bars.value.length > 1) lines.push(`Pace peaks at about ${peakWpm.value} WPM in the fastest section.`)
      if (!lines.length) lines.push('Add more transcript content or timestamps to see highlights.')
      return lines
    })

    /* ---------- Export + copy ---------- */
    const showToast = (message) => {
      toast.value = message
      clearTimeout(toastTimer)
      toastTimer = setTimeout(() => { toast.value = '' }, 2500)
    }

    const safeName = () =>
      (transcript.value?.title || 'transcript').replace(/[^\w-]+/g, '_').slice(0, 60) || 'transcript'

    const download = (content, type, extension) => {
      const blob = new Blob([content], { type })
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = `${safeName()}-analysis.${extension}`
      document.body.appendChild(link)
      link.click()
      link.remove()
      URL.revokeObjectURL(url)
      showToast(`Downloaded .${extension} file`)
    }

    const downloadJson = () => {
      const payload = {
        title: transcript.value?.title,
        generatedAt: new Date().toISOString(),
        summary: {
          wordCount: wordCount.value,
          uniqueWords: uniqueWords.value,
          segmentCount: segmentCount.value,
          durationSeconds: Math.round(totalSeconds.value),
          wordsPerMinute: wpm.value,
          speechSeconds: Math.round(speechSeconds.value),
          silenceSeconds: Math.round(silenceSeconds.value),
          pausesOverHalfSecond: pauses.value.length
        },
        topTerms: keywords.value.map(({ term, count }) => ({ term, count })),
        segments: [...rows.value]
          .sort((a, b) => a.index - b.index)
          .map(({ index, start, end, words: segWords, wpm: segWpm, text: segText }) => ({
            index: index + 1, start, end, words: segWords, wpm: segWpm, text: segText
          }))
      }
      download(JSON.stringify(payload, null, 2), 'application/json', 'json')
    }

    const downloadCsv = () => {
      const escape = (value) => `"${String(value).replace(/"/g, '""')}"`
      const header = ['index', 'start', 'end', 'words', 'wpm', 'text']
      const lines = [...rows.value]
        .sort((a, b) => a.index - b.index)
        .map((row) =>
          [row.index + 1, row.start, row.end, row.words, row.wpm, escape(row.text)].join(',')
        )
      download([header.join(','), ...lines].join('\n'), 'text/csv;charset=utf-8', 'csv')
    }

    const copySummary = async () => {
      const summary = [
        `Transcript: ${transcript.value?.title}`,
        `Words: ${wordCount.value.toLocaleString()} (${uniqueWords.value.toLocaleString()} unique)`,
        `Segments: ${segmentCount.value.toLocaleString()}`,
        `Duration: ${duration.value}`,
        `Speaking rate: ${wpm.value ? `${wpm.value} WPM` : 'n/a'}`,
        `Speech vs. silence: ${talkPercent.value}% / ${100 - talkPercent.value}%`,
        keywords.value.length ? `Top terms: ${keywords.value.map((k) => k.term).join(', ')}` : ''
      ].filter(Boolean).join('\n')

      try {
        await navigator.clipboard.writeText(summary)
        showToast('Summary copied to clipboard')
      } catch (error) {
        showToast('Copy failed. Your browser blocked clipboard access.')
      }
    }

    return {
      transcript, wordCount, segmentCount, averageWords, duration, totalSeconds,
      wpm, readingTime, paceLabel, paceTone, createdLabel,
      metrics, insights, keywords, distribution,
      speechSeconds, silenceSeconds, talkPercent, topPauses, longestPause,
      chart, bars, peakWpm, avgLineY,
      rows, visibleRows, sortMode, showAll,
      toast, formatTime, copySummary, downloadJson, downloadCsv
    }
  }
}
</script>

<style scoped>
.an-page {
  --an-bg: var(--surface);
  --an-bg-soft: var(--surface-muted);
  --an-border: var(--line);
  --an-text: var(--ink);
  --an-muted: var(--muted);
  --an-accent: var(--accent);
  --an-accent-soft: var(--accent-soft);
  --an-good: var(--success);
  --an-good-soft: var(--success-soft);
  --an-warn: var(--warning);
  --an-warn-soft: var(--warning-soft);
  --an-info: var(--accent);

  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  color: var(--an-text);
}

.an-visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}

/* Intro */
.an-eyebrow,
.an-label {
  margin: 0 0 0.35rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--an-accent);
}
.an-intro h2 { margin: 0 0 0.4rem; font-size: 1.9rem; }
.an-intro p:last-child { margin: 0; color: var(--an-muted); max-width: 62ch; }

/* Cards */
.an-card {
  background: var(--an-bg);
  border: 1px solid var(--an-border);
  border-radius: 16px;
  padding: 1.25rem;
  box-shadow: 0 1px 2px rgba(16, 24, 40, 0.04);
}
.an-card h4 { margin: 0; font-size: 1rem; }
.an-card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}
.an-sub { margin: 0.2rem 0 0.9rem; font-size: 0.85rem; color: var(--an-muted); }
.an-card-head .an-sub { margin-bottom: 0; }
.an-muted { margin: 0; color: var(--an-muted); font-size: 0.9rem; }

/* Header */
.an-header {
  display: flex;
  justify-content: space-between;
  gap: 1.25rem;
  flex-wrap: wrap;
}
.an-header h3 { margin: 0 0 0.6rem; font-size: 1.35rem; word-break: break-word; }
.an-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
  font-size: 0.85rem;
  color: var(--an-muted);
}
.an-header-actions { display: flex; flex-direction: column; gap: 0.6rem; align-items: flex-end; }
.an-select-label select {
  min-width: 220px;
  max-width: 100%;
  padding: 0.55rem 0.75rem;
  border-radius: 10px;
  border: 1px solid var(--an-border);
  background: var(--an-bg-soft);
  color: var(--an-text);
  font: inherit;
}

.an-pill {
  display: inline-block;
  padding: 0.15rem 0.6rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--an-bg-soft);
  color: var(--an-muted);
}
.an-pill--good { background: var(--an-good-soft); color: var(--an-good); }
.an-pill--warn { background: var(--an-warn-soft); color: var(--an-warn); }
.an-pill--info { background: var(--an-accent-soft); color: var(--an-info); }

/* Buttons */
.an-btn-row { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.an-btn {
  padding: 0.5rem 0.9rem;
  border-radius: 10px;
  border: 1px solid var(--an-border);
  background: var(--an-bg);
  color: var(--an-text);
  font: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s;
}
.an-btn:hover:not(:disabled) { border-color: var(--an-accent); }
.an-btn:focus-visible,
.an-select-label select:focus-visible,
.an-cta:focus-visible { outline: 2px solid var(--an-accent); outline-offset: 2px; }
.an-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.an-btn--primary { background: var(--an-accent); border-color: var(--an-accent); color: #fff; }
.an-btn--active { background: var(--an-accent-soft); border-color: var(--an-accent); color: var(--an-accent); }
.an-btn--ghost { margin-top: 0.9rem; background: transparent; }

.an-toast {
  min-height: 1.2rem;
  margin: -0.5rem 0 0;
  font-size: 0.85rem;
  color: var(--an-good);
}

/* Metrics */
.an-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 0.9rem;
}
.an-metric {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding: 1.1rem;
  background: var(--an-bg);
  border: 1px solid var(--an-border);
  border-radius: 16px;
}
.an-metric-top { display: flex; align-items: center; gap: 0.6rem; }
.an-metric-top p { margin: 0; font-size: 0.82rem; color: var(--an-muted); }
.an-metric-icon {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 9px;
  background: var(--an-accent-soft);
  color: var(--an-accent);
  font-size: 0.85rem;
  font-weight: 700;
}
.an-metric strong { font-size: 1.7rem; line-height: 1.1; font-variant-numeric: tabular-nums; }
.an-metric-hint { font-size: 0.78rem; color: var(--an-muted); }

/* Grid */
.an-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.9rem;
}
.an-span-2 { grid-column: span 2; }
.an-span-3 { grid-column: span 3; }

/* Chart */
.an-chart svg { width: 100%; height: 160px; display: block; }
.an-chart-bar { fill: var(--an-accent); opacity: 0.85; }
.an-chart-bar:hover { opacity: 1; }
.an-chart-avg { stroke: var(--an-muted); stroke-width: 1; stroke-dasharray: 5 4; vector-effect: non-scaling-stroke; }
.an-chart-axis {
  display: flex;
  justify-content: space-between;
  margin-top: 0.4rem;
  font-size: 0.75rem;
  color: var(--an-muted);
}

/* Lists */
.an-insights { margin: 0.8rem 0 0; padding-left: 1.1rem; display: grid; gap: 0.6rem; font-size: 0.9rem; }
.an-keywords,
.an-dist { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.55rem; }
.an-keywords li,
.an-dist li {
  display: grid;
  grid-template-columns: 90px 1fr 32px;
  align-items: center;
  gap: 0.6rem;
  font-size: 0.85rem;
}
.an-keyword-term { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.an-keyword-bar { height: 8px; border-radius: 999px; background: var(--an-bg-soft); overflow: hidden; }
.an-keyword-bar span { display: block; height: 100%; background: var(--an-accent); border-radius: inherit; }
.an-keyword-count { text-align: right; color: var(--an-muted); font-variant-numeric: tabular-nums; }

/* Speech vs silence */
.an-split { height: 10px; margin: 0.9rem 0; border-radius: 999px; background: var(--an-bg-soft); overflow: hidden; }
.an-split-talk { display: block; height: 100%; background: var(--an-good); }
.an-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; margin: 0 0 0.8rem; }
.an-stats dt { font-size: 0.75rem; color: var(--an-muted); }
.an-stats dd { margin: 0.15rem 0 0; font-weight: 700; font-variant-numeric: tabular-nums; }
.an-pauses { list-style: none; margin: 0; padding: 0; display: grid; gap: 0.4rem; font-size: 0.85rem; }
.an-pauses li { display: flex; justify-content: space-between; color: var(--an-muted); }
.an-pauses strong { color: var(--an-text); }

/* Table */
.an-table-wrap { overflow-x: auto; border: 1px solid var(--an-border); border-radius: 12px; }
.an-table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
.an-table th,
.an-table td { padding: 0.65rem 0.8rem; text-align: left; border-bottom: 1px solid var(--an-border); }
.an-table th { background: var(--an-bg-soft); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--an-muted); }
.an-table tbody tr:last-child td { border-bottom: 0; }
.an-table tbody tr:hover { background: var(--an-bg-soft); }
.an-nowrap { white-space: nowrap; font-variant-numeric: tabular-nums; }
.an-snippet { max-width: 420px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: var(--an-muted); }

.an-disclaimer { margin: 0; font-size: 0.8rem; color: var(--an-muted); max-width: 80ch; }

/* Empty */
.an-empty {
  text-align: center;
  padding: 3rem 1.5rem;
  border: 1px dashed var(--an-border);
  border-radius: 16px;
  background: var(--an-bg);
}
.an-empty-icon {
  display: inline-grid;
  place-items: center;
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--an-accent-soft);
  color: var(--an-accent);
  font-size: 1.5rem;
}
.an-empty h3 { margin: 1rem 0 0.4rem; }
.an-empty p { margin: 0 0 1.2rem; color: var(--an-muted); }
.an-cta {
  display: inline-block;
  padding: 0.65rem 1.2rem;
  border-radius: 10px;
  background: var(--an-accent);
  color: #fff;
  font-weight: 600;
  text-decoration: none;
}

/* Responsive */
@media (max-width: 900px) {
  .an-grid { grid-template-columns: 1fr; }
  .an-span-2,
  .an-span-3 { grid-column: auto; }
  .an-header-actions { align-items: stretch; width: 100%; }
}
</style>