<template>
  <div class="home-page">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <div class="eyebrow">Audio to Text • AI-Powered Transcription</div>
        <h1>Transcripto</h1>
        <p class="subtitle">Transform your audio files into accurate, timestamped transcriptions instantly using state-of-the-art OpenAI Whisper AI technology.</p>

        <div class="hero-actions">
          <button class="cta" @click="scrollToUpload">Start Converting</button>
          <div class="status-chip" :class="statusClass">
            <span class="dot"></span>
            {{ statusLabel }}
          </div>
        </div>

        <div class="hero-badges">
          <span class="badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="17 8 12 3 7 8"></polyline>
              <line x1="12" y1="3" x2="12" y2="15"></line>
            </svg>
            Drag & Drop
          </span>
          <span class="badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h6l-2 8 10-12h-6l2-8z"></path>
            </svg>
            Fast Processing
          </span>
          <span class="badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="7" y="7" width="10" height="10" rx="2"></rect>
              <path d="M4 10h3"></path>
              <path d="M4 14h3"></path>
              <path d="M17 10h3"></path>
              <path d="M17 14h3"></path>
              <path d="M10 4v3"></path>
              <path d="M14 4v3"></path>
              <path d="M10 17v3"></path>
              <path d="M14 17v3"></path>
            </svg>
            AI-Powered
          </span>
          <span class="badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="m12 3-9 5 9 5 9-5-9-5Z"></path>
              <path d="m3 13 9 5 9-5"></path>
              <path d="m3 18 9 5 9-5"></path>
            </svg>
            Multi-Format
          </span>
        </div>
      </div>

      <div class="hero-card">
        <div class="mini-stat">
          <span class="label">Current status</span>
          <span class="value" :class="statusClass">{{ status }}</span>
        </div>
        <div class="mini-stat">
          <span class="label">Selected file</span>
          <span class="value">{{ selectedFile ? selectedFile.name : 'None yet' }}</span>
        </div>
        <div class="mini-stat">
          <span class="label">Output</span>
          <span class="value">{{ transcribedText ? 'Ready' : 'Pending' }}</span>
        </div>
      </div>
    </section>

    <!-- Workspace -->
    <section class="workspace" ref="uploadSection">
      <div class="panel upload-panel">
        <div class="panel-header">
          <div>
            <p class="eyebrow">Upload</p>
            <h2>Drop your audio file</h2>
            <p class="muted">Accepts all common audio formats. We keep the flow simple and secure.</p>
          </div>
          <button class="ghost-btn" @click="resetInput" title="Reset selection">Reset</button>
        </div>

        <div
          class="dropzone"
          :class="{ 'is-dragging': isDragging, 'is-active': selectedFile }"
          @dragover.prevent="handleDragOver"
          @dragleave.prevent="handleDragLeave"
          @drop.prevent="handleDrop"
        >
          <input
            ref="fileInput"
            type="file"
            accept="audio/*"
            id="audioFile"
            class="file-input"
            @change="handleFileSelect"
          />
          <label for="audioFile" class="dropzone-body">
            <div class="icon-circle">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="17 8 12 3 7 8"></polyline>
                <line x1="12" y1="3" x2="12" y2="15"></line>
              </svg>
            </div>
            <div class="drop-copy">
              <p class="headline">Drag & drop or browse</p>
              <p class="hint">Lossless, WAV, MP3, M4A, AAC, and more.</p>
            </div>
            <div class="pill-row">
              <span class="pill neutral">{{ uploadText }}</span>
              <span class="pill info" v-if="selectedFile">{{ formatFileSize(selectedFile.size) }}</span>
              <span class="pill warning" v-else>Awaiting file</span>
            </div>
          </label>
        </div>

        <transition name="fade">
          <div v-if="selectedFile" class="file-preview">
            <div class="file-chip">
              <span class="dot success"></span>
              <div class="file-meta">
                <p class="name">{{ selectedFile.name }}</p>
                <p class="size">{{ formatFileSize(selectedFile.size) }}</p>
              </div>
            </div>
          </div>
        </transition>

        <div class="actions">
          <div class="status-legend">
            <span class="legend-dot idle"></span>Idle
            <span class="legend-dot processing"></span>Processing
            <span class="legend-dot success"></span>Completed
          </div>

          <button
            class="convert-btn"
            :disabled="!selectedFile || isProcessing"
            :class="{ 'is-loading': isProcessing }"
            @click="handleConvert"
          >
            <span v-if="!isProcessing" class="btn-text">Convert to Text</span>
            <span v-else class="btn-text loading-text">
              <span class="spinner"></span>
              Processing...
            </span>
          </button>
        </div>

        <transition name="fade">
          <div v-if="errorMessage" class="alert error">{{ errorMessage }}</div>
        </transition>

        <transition name="fade">
          <div v-if="status" class="status-bar" :class="statusClass">
            <div class="status-text">
              <span class="dot"></span>
              {{ status }}
            </div>
            <span class="status-sub">{{ statusDescription }}</span>
          </div>
        </transition>
      </div>

      <div class="panel output-panel">
        <div class="panel-header">
          <div>
            <p class="eyebrow">Transcription</p>
            <h2>Readable, clean text</h2>
            <p class="muted">Copy or download the output. Ready for your AI backend.</p>
          </div>
          <div class="output-actions">
            <button class="ghost-btn" @click="copyToClipboard">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
              </svg>
              {{ copyButtonText }}
            </button>
            <button class="ghost-btn" @click="downloadText" :disabled="!transcribedText">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 3v14"></path>
                <polyline points="6 13 12 19 18 13"></polyline>
                <rect x="4" y="19" width="16" height="2" rx="1"></rect>
              </svg>
              Download .txt
            </button>
          </div>
        </div>

        <div class="output-card" :class="{ empty: !transcribedText }">
          <p class="output-placeholder" v-if="!transcribedText">Drop an audio file and convert to see your transcription here.</p>
          <div v-else>
            <div v-if="displaySegments.length" class="transcript-list">
              <div
                v-for="(seg, idx) in displaySegments"
                :key="idx"
                class="transcript-row"
                :class="{ 'active': idx === activeSegmentIndex }"
                @click="seekToSegment(seg.start)"
              >
                <div class="spk-badge">{{ seg.speaker }}</div>
                <div class="seg-body">
                  <div class="seg-meta">{{ seg.time }}</div>
                  <div class="seg-text">{{ seg.text }}</div>
                </div>
              </div>
            </div>
            <p v-else class="output-text">{{ transcribedText }}</p>
          </div>
        </div>

        <!-- Audio Player -->
        <div v-if="audioUrl" class="audio-player">
          <audio ref="audioElement" :src="audioUrl" @loadedmetadata="onAudioLoaded" @timeupdate="onTimeUpdate"></audio>
          <div class="player-controls">
            <button class="play-btn" @click="togglePlay" :title="isPlaying ? 'Pause' : 'Play'">
              <svg v-if="!isPlaying" viewBox="0 0 24 24" fill="currentColor">
                <path d="M8 5v14l11-7z"/>
              </svg>
              <svg v-else viewBox="0 0 24 24" fill="currentColor">
                <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>
              </svg>
            </button>
            <div class="time-display">{{ currentTimeDisplay }}</div>
            <div class="progress-bar" @click="seekAudio">
              <div class="progress-fill" :style="{ width: progressPercent + '%' }"></div>
            </div>
            <div class="time-display">{{ durationDisplay }}</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'HomePage',
  setup() {
    const fileInput = ref(null)
    const selectedFile = ref(null)
    const isProcessing = ref(false)
    const isDragging = ref(false)
    const status = ref('Idle')
    const transcribedText = ref('')
    const segments = ref([])
    const errorMessage = ref('')
    const copyButtonText = ref('Copy Text')
    const uploadSection = ref(null)
    const audioUrl = ref('')
    const audioElement = ref(null)
    const isPlaying = ref(false)
    const currentTime = ref(0)
    const duration = ref(0)

    const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

    const uploadText = computed(() => {
      return selectedFile.value ? 'Audio file selected' : 'Select or drag audio file'
    })

    const statusClass = computed(() => {
      if (status.value === 'Idle') return 'status-idle'
      if (status.value === 'Processing') return 'status-processing'
      if (status.value === 'Completed') return 'status-completed'
      return ''
    })

    const statusLabel = computed(() => {
      if (status.value === 'Idle') return 'Idle • Ready when you are'
      if (status.value === 'Processing') return 'Processing • Converting audio'
      if (status.value === 'Completed') return 'Completed • Text ready'
      return status.value
    })

    const statusDescription = computed(() => {
      if (status.value === 'Idle') return 'Waiting for an audio file to process.'
      if (status.value === 'Processing') return 'Transcribing with OpenAI Whisper AI.'
      if (status.value === 'Completed') return 'Transcription ready to copy or download.'
      return ''
    })

    const setFile = (file) => {
      if (!file) return
      if (!file.type.startsWith('audio/')) {
        errorMessage.value = 'Please select a valid audio file'
        selectedFile.value = null
        return
      }
      selectedFile.value = file
      errorMessage.value = ''
      status.value = 'Idle'
      transcribedText.value = ''
      segments.value = []
      
      if (audioUrl.value) {
        URL.revokeObjectURL(audioUrl.value)
      }
      audioUrl.value = URL.createObjectURL(file)
    }

    const handleFileSelect = (event) => {
      const files = event.target.files
      if (files && files.length > 0) {
        setFile(files[0])
      }
    }

    const handleDragOver = () => {
      isDragging.value = true
    }

    const handleDragLeave = () => {
      isDragging.value = false
    }

    const handleDrop = (event) => {
      const files = event.dataTransfer?.files
      if (files && files.length > 0) {
        setFile(files[0])
      }
      isDragging.value = false
    }

    const handleConvert = async () => {
      if (!selectedFile.value) {
        errorMessage.value = 'Please select an audio file first'
        return
      }

      errorMessage.value = ''
      transcribedText.value = ''
      segments.value = []
      isProcessing.value = true
      status.value = 'Processing'

      try {
        const formData = new FormData()
        formData.append('audio', selectedFile.value)

        const response = await fetch(`${API_BASE_URL}/api/transcribe`, {
          method: 'POST',
          body: formData,
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.error || 'Transcription failed')
        }

        transcribedText.value = data.transcription
        segments.value = Array.isArray(data.segments) ? data.segments : []
        status.value = 'Completed'

      } catch (error) {
        console.error('Transcription error:', error)
        errorMessage.value = error.message || 'Failed to transcribe audio. Make sure the backend is running.'
        status.value = 'Idle'
      } finally {
        isProcessing.value = false
      }
    }

    const formatFileSize = (bytes) => {
      if (bytes === 0) return '0 Bytes'
      const k = 1024
      const sizes = ['Bytes', 'KB', 'MB']
      const i = Math.floor(Math.log(bytes) / Math.log(k))
      return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i]
    }

    const buildPlainText = () => {
      if (!displaySegments.value.length) return transcribedText.value || ''
      return displaySegments.value
        .map(s => `${s.speaker}  ${s.time}  ${s.text}`)
        .join('\n')
    }

    const copyToClipboard = async () => {
      const text = buildPlainText()
      if (!text) return
      try {
        await navigator.clipboard.writeText(text)
        copyButtonText.value = 'Copied!'
        setTimeout(() => {
          copyButtonText.value = 'Copy Text'
        }, 2000)
      } catch (error) {
        errorMessage.value = 'Failed to copy text'
      }
    }

    const downloadText = () => {
      const text = buildPlainText()
      if (!text) return
      const blob = new Blob([text], { type: 'text/plain' })
      const url = URL.createObjectURL(blob)
      const link = document.createElement('a')
      link.href = url
      link.download = 'transcription.txt'
      link.click()
      URL.revokeObjectURL(url)
    }

    const resetInput = () => {
      selectedFile.value = null
      transcribedText.value = ''
      status.value = 'Idle'
      errorMessage.value = ''
      if (fileInput.value) {
        fileInput.value.value = ''
      }
      
      if (audioUrl.value) {
        URL.revokeObjectURL(audioUrl.value)
        audioUrl.value = ''
      }
      isPlaying.value = false
      currentTime.value = 0
      duration.value = 0
    }

    const scrollToUpload = () => {
      uploadSection.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }

    const togglePlay = () => {
      if (!audioElement.value) return
      if (isPlaying.value) {
        audioElement.value.pause()
        isPlaying.value = false
      } else {
        audioElement.value.play()
        isPlaying.value = true
      }
    }

    const onAudioLoaded = () => {
      if (audioElement.value) {
        duration.value = audioElement.value.duration || 0
      }
    }

    const onTimeUpdate = () => {
      if (audioElement.value) {
        currentTime.value = audioElement.value.currentTime || 0
      }
    }

    const seekAudio = (event) => {
      if (!audioElement.value) return
      const rect = event.currentTarget.getBoundingClientRect()
      const percent = (event.clientX - rect.left) / rect.width
      audioElement.value.currentTime = percent * duration.value
    }

    const seekToSegment = (start) => {
      if (!audioElement.value || !audioUrl.value) return
      const target = Math.max(0, start || 0)
      audioElement.value.currentTime = target
      audioElement.value.play()
      isPlaying.value = true
    }

    const currentTimeDisplay = computed(() => formatTime(currentTime.value))
    const durationDisplay = computed(() => formatTime(duration.value))
    const progressPercent = computed(() => {
      if (!duration.value) return 0
      return (currentTime.value / duration.value) * 100
    })

    const formatTime = (seconds) => {
      if (seconds == null || isNaN(seconds)) return '0:00'
      const m = Math.floor(seconds / 60)
      const s = Math.floor(seconds % 60)
      return `${m}:${s.toString().padStart(2, '0')}`
    }

    const activeSegmentIndex = computed(() => {
      if (!Array.isArray(segments.value) || segments.value.length === 0) return -1
      const time = currentTime.value
      for (let i = 0; i < segments.value.length; i++) {
        const seg = segments.value[i]
        const start = seg.start || 0
        const end = seg.end || 0
        if (time >= start && time <= end) {
          return i
        }
      }
      return -1
    })

    const displaySegments = computed(() => {
      if (!Array.isArray(segments.value) || segments.value.length === 0) return []
      let current = 'SPK_1'
      let lastEnd = null
      const PAUSE_THRESHOLD = 1.4
      return segments.value.map((seg, idx) => {
        let spk = seg.speaker
        if (!spk) {
          const gap = lastEnd == null ? 0 : Math.max(0, (seg.start || 0) - lastEnd)
          if (gap >= PAUSE_THRESHOLD && idx > 0) {
            current = current === 'SPK_1' ? 'SPK_2' : 'SPK_1'
          }
          spk = current
        }
        lastEnd = seg.end || lastEnd
        return {
          speaker: spk,
          time: formatTime(seg.start || 0),
          text: (seg.text || '').trim(),
          start: seg.start || 0,
          end: seg.end || 0
        }
      })
    })

    return {
      fileInput,
      uploadSection,
      selectedFile,
      isProcessing,
      isDragging,
      status,
      transcribedText,
      segments,
      errorMessage,
      uploadText,
      statusClass,
      statusLabel,
      statusDescription,
      copyButtonText,
      displaySegments,
      activeSegmentIndex,
      audioUrl,
      audioElement,
      isPlaying,
      currentTime,
      duration,
      currentTimeDisplay,
      durationDisplay,
      progressPercent,
      togglePlay,
      onAudioLoaded,
      onTimeUpdate,
      seekAudio,
      seekToSegment,
      handleFileSelect,
      handleConvert,
      handleDragOver,
      handleDragLeave,
      handleDrop,
      formatFileSize,
      copyToClipboard,
      downloadText,
      resetInput,
      scrollToUpload
    }
  }
}
</script>

<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Import styles from main App.vue - these will be moved to a global stylesheet */
</style>
