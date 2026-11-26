<template>
  <div class="home-page">
    <section id="workspace" ref="uploadSection" class="workspace dashboard-grid" aria-label="Audio transcription workspace">
      <div class="panel upload-panel">
        <div class="panel-header">
          <div class="panel-title-group">
            <h2 class="panel-title">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 3 1.6 5.4L19 10l-5.4 1.6L12 17l-1.6-5.4L5 10l5.4-1.6L12 3Zm7 11 .8 2.2L22 17l-2.2.8L19 20l-.8-2.2L16 17l2.2-.8L19 14Z" /></svg>
              Input
            </h2>
            <p class="muted">Choose an audio file to transcribe.</p>
          </div>
          <StatusPill :state-class="statusClass" :label="statusLabel" />
          <details ref="inputOptionsMenu" class="input-options-menu">
            <summary aria-label="Input options" title="Input options">
              <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1" /><circle cx="12" cy="12" r="1" /><circle cx="19" cy="12" r="1" /></svg>
            </summary>
            <div class="input-options-popover">
              <button type="button" @click="clearInputAndClose">Clear input</button>
              <router-link to="/features">Supported formats</router-link>
            </div>
          </details>
        </div>

        <div class="input-method-label">Input Method</div>
        <div class="mode-toggle" role="group" aria-label="Audio input mode">
          <button class="mode-option" :class="{ 'is-active': inputMode === 'record' }" type="button" :aria-pressed="inputMode === 'record'" :disabled="isRecording || isRecordingPaused || isProcessing" @click="selectInputMode('record')">Record</button>
          <button class="mode-option" :class="{ 'is-active': inputMode === 'upload' }" type="button" :aria-pressed="inputMode === 'upload'" :disabled="isRecording || isRecordingPaused || isProcessing" @click="selectInputMode('upload')">Upload</button>
        </div>

        <div
          v-if="inputMode === 'upload'"
          class="dropzone"
          :class="{ 'is-dragging': isDragging, 'is-active': selectedFile }"
          role="group"
          :aria-label="selectedFile ? `Selected file: ${selectedFile.name}` : 'Upload audio file'"
          @dragover.prevent="handleDragOver"
          @dragleave.prevent="handleDragLeave"
          @drop.prevent="handleDrop"
          @click.self="!selectedFile && openFilePicker()"
          @keydown.enter.prevent="!selectedFile && openFilePicker()"
          @keydown.space.prevent="!selectedFile && openFilePicker()"
        >
          <input
            ref="fileInput"
            type="file"
            accept=".mp3,.wav,.m4a,.flac,.ogg,.aac,.wma,.opus,audio/*"
            id="audioFile"
            class="file-input"
            aria-label="Choose an audio file"
            @change="handleFileSelect"
          />
          <div v-if="selectedFile" ref="selectedFileCard" class="selected-file-card" tabindex="-1">
            <span class="selected-file-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24"><path d="M13 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V10z" /><path d="M13 3v7h7M8 15h8M8 18h6" /></svg>
            </span>
            <div class="selected-file-copy">
              <strong class="selected-file-name">{{ selectedFile.name }}</strong>
              <span class="selected-file-size">{{ formatFileSize(selectedFile.size) }} · Ready to transcribe</span>
            </div>
            <button class="reset-button" type="button" @click="resetInput" :disabled="isProcessing" aria-label="Remove selected audio file">Remove</button>
          </div>
          <div v-else class="dropzone-body" @click="openFilePicker">
            <span class="icon-circle" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 16V4m0 0L7 9m5-5 5 5" />
                <path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3" />
              </svg>
            </span>
            <span class="drop-copy">
              <span class="headline">Drag and drop or browse</span>
              <span class="hint">Choose an audio file from your device</span>
            </span>
            <span class="format-chips" aria-label="Supported formats">
              <span v-for="format in supportedFormats" :key="format">{{ format }}</span>
            </span>
            <span class="format-hint">Maximum file size: 25 MB</span>
            <button ref="browseButton" class="browse-button" type="button" @click.stop="openFilePicker">Browse files</button>
          </div>
        </div>
        <p v-if="inputMode === 'upload'" class="upload-privacy-note">Audio is temporarily stored on the server while processing and removed afterward.</p>

        <div v-if="inputMode === 'record'" class="recorder-panel" :class="{ 'is-recording': isRecording }">
          <p class="recorder-status" aria-live="polite">{{ recorderMessage }}</p>
          <div class="recording-timer" :aria-label="`Recording duration ${recordingTimeDisplay}`">
            <span>{{ recordingTimeDisplay.slice(0, -2) }}</span><strong>{{ recordingTimeDisplay.slice(-2) }}</strong>
          </div>
          <div class="recording-waveform" :class="{ 'is-active': isRecording }" aria-hidden="true">
            <span
              v-for="(height, index) in visualizerBars"
              :key="index"
              :style="{ height: `${height}%`, animationDelay: `${(index % 10) * 55}ms` }"
            ></span>
          </div>
          <div class="recorder-actions">
            <button v-if="!isRecording && !isRecordingPaused" class="record-start-button" type="button" @click="startRecording">
              <span class="record-dot" aria-hidden="true"></span> Start recording
            </button>
            <template v-else>
              <button class="pause-button" type="button" @click="toggleRecordingPause">
                <svg v-if="isRecording" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM15 5h4v14h-4z" /></svg>
                <svg v-else viewBox="0 0 24 24" aria-hidden="true"><path d="m8 5 11 7-11 7z" /></svg>
                {{ isRecording ? 'Pause' : 'Resume' }}
              </button>
              <button class="stop-button" type="button" @click="stopRecording">
                <span class="stop-icon" aria-hidden="true"></span> Stop
              </button>
            </template>
          </div>
          <p v-if="recordingError" class="recording-error" role="alert">{{ recordingError }}</p>
          <p class="recorder-hint">Recording stays on this device and is converted to WAV. The 25 MB limit applies.</p>
        </div>

        <div v-if="inputMode === 'upload' && audioUrl" class="compact-audio-player">
          <button class="audio-play-button" type="button" @click="togglePlay" :disabled="!duration || isProcessing" :aria-label="isPlaying ? 'Pause audio playback' : 'Play audio'">
            <svg v-if="isPlaying" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM15 5h4v14h-4z" /></svg>
            <svg v-else viewBox="0 0 24 24" aria-hidden="true"><path d="m8 5 11 7-11 7z" /></svg>
          </button>
          <span class="audio-time">{{ currentTimeDisplay }}</span>
          <div class="audio-progress-wrap">
            <div class="audio-progress-track" :style="{ '--audio-progress': `${audioProgress}%` }"></div>
            <input
              class="audio-progress-input"
              type="range"
              min="0"
              :max="duration || 0"
              step="0.1"
              :value="currentTime"
              :disabled="!duration || isProcessing"
              :aria-label="`Audio position, ${currentTimeDisplay} of ${durationDisplay}`"
              @input="seekAudio"
            />
          </div>
          <span class="audio-time">{{ durationDisplay }}</span>
        </div>

        <div v-if="inputMode === 'upload'" class="conversion-row">
          <button
            class="convert-btn"
            :disabled="!selectedFile || isProcessing"
            :class="{ 'is-loading': isProcessing }"
            @click="handleConvert"
          >
            <span v-if="!isProcessing" class="btn-text">Convert to Text</span>
            <span v-else class="btn-text loading-text">
              <span class="spinner"></span>
              Processing…
            </span>
          </button>
          <span class="conversion-hint">Up to 25 MB · 8 supported formats</span>
        </div>

        <div v-if="status === 'Error'" ref="statusMessage" class="alert error" role="alert" tabindex="-1">
          <strong>{{ errorTitle }}</strong>
          <span>{{ errorMessage }}</span>
          <button v-if="selectedFile && !isProcessing" class="retry-button" type="button" @click="handleConvert">Try again</button>
        </div>
        <p v-if="playbackErrorMessage" class="copy-error" role="alert">{{ playbackErrorMessage }}</p>
      </div>

      <div class="panel output-panel">
        <div class="panel-header">
          <div class="panel-title-group">
            <h2 class="panel-title">Output</h2>
            <p class="muted">{{ transcribedText ? 'Review your generated transcript.' : 'Your generated transcript will appear here.' }}</p>
          </div>
          <div class="output-actions">
            <button class="output-icon-button" type="button" :aria-label="isEditingTitle ? 'Finish editing transcript title' : 'Edit transcript title'" @click="toggleTitleEdit">
              <svg v-if="!isEditingTitle" viewBox="0 0 24 24" aria-hidden="true"><path d="m15 5 4 4M4 20l4-.8L19 8a2.1 2.1 0 0 0-3-3L5 16z" /></svg>
              <svg v-else viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" /></svg>
            </button>
            <details ref="exportMenu" class="export-menu" :class="{ 'is-disabled': !transcribedText }" :aria-disabled="!transcribedText" @click="!transcribedText && $event.preventDefault()">
              <summary class="export-button" :aria-disabled="!transcribedText" :tabindex="transcribedText ? 0 : -1">
                Export
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m7 10 5 5 5-5" /></svg>
              </summary>
              <div class="export-menu-popover">
                <button type="button" @click="downloadAndClose">Download .txt</button>
              </div>
            </details>
            <button class="copy-button" type="button" @click="copyToClipboard" :disabled="!transcribedText" :aria-label="copyButtonText === 'Copied!' ? 'Transcript copied' : 'Copy transcript'" aria-live="polite">
              <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2" /><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3" /></svg>
              {{ copyButtonText === 'Copied!' ? 'Copied' : 'Copy' }}
            </button>
          </div>
        </div>
        <p v-if="copyErrorMessage" class="copy-error" role="alert">{{ copyErrorMessage }}</p>
        <div v-if="!transcribedText && !isProcessing" class="output-info-bar">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="12" rx="3" /><path d="M5 11a7 7 0 0 0 14 0m-7 7v3m-4 0h8" /></svg>
          <span>Your generated transcript will appear here.</span>
        </div>

        <div class="transcript-title-row">
          <h3 v-if="!isEditingTitle" ref="transcriptHeading" class="transcript-title" tabindex="-1">{{ transcriptTitle }}</h3>
          <input
            v-else
            ref="titleInput"
            v-model="transcriptTitle"
            class="transcript-title-input"
            maxlength="100"
            aria-label="Transcript title"
            @keydown.enter="toggleTitleEdit"
          />
          <span v-if="transcribedText" class="estimated-speakers">Estimated speakers</span>
        </div>
        <p v-if="historySelection && !audioUrl" class="history-audio-note">Audio files aren’t saved in browser history, so playback is unavailable for this transcript.</p>

        <div ref="transcriptScroller" class="output-card" :class="{ empty: !transcribedText }" :aria-busy="isProcessing" aria-live="polite">
          <div v-if="isProcessing" class="transcript-loading" aria-label="Transcription in progress">
            <span class="spinner"></span>
            <p>Transcribing with OpenAI Whisper AI…</p>
            <div class="skeleton-line"></div>
            <div class="skeleton-line"></div>
            <div class="skeleton-line"></div>
          </div>
          <div v-else-if="transcribedText">
            <div v-if="displaySegments.length" class="transcript-list">
              <TranscriptSegment
                v-for="(seg, idx) in displaySegments"
                :key="idx"
                :speaker="seg.speaker"
                :time="seg.time"
                :text="seg.text"
                :active="idx === activeSegmentIndex"
                :seekable="Boolean(audioUrl)"
                @seek="seekToSegment(seg.start)"
              />
            </div>
            <p v-else class="output-text">{{ transcribedText }}</p>
          </div>
        </div>

        <p v-if="transcribedText && displaySegments.length" class="speaker-disclaimer">
          Speaker labels are estimates from pauses, not verified speaker identification.
        </p>

        <div class="polish-row">
          <button class="polish-button" type="button" disabled title="Coming soon" aria-label="Polish transcript with AI — coming soon">
            <span aria-hidden="true">✦</span> Polish with AI <span class="coming-soon">Coming soon</span>
          </button>
        </div>

        <audio
          v-if="audioUrl"
          ref="audioElement"
          class="audio-element"
          :src="audioUrl"
          @loadedmetadata="onAudioLoaded"
          @timeupdate="onTimeUpdate"
          @play="isPlaying = true"
          @pause="isPlaying = false"
          @ended="isPlaying = false"
        ></audio>

        <div v-if="status !== 'Error'" class="workspace-status" :class="statusClass">
          <span class="workspace-status-dot" aria-hidden="true"></span>
          <span>{{ statusLabel }}</span>
          <span class="workspace-status-detail">{{ statusDescription }}</span>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import { ref, computed, nextTick, onBeforeUnmount, watch } from 'vue'
import StatusPill from '../components/StatusPill.vue'
import TranscriptSegment from '../components/TranscriptSegment.vue'

export default {
  name: 'HomePage',
  props: {
    historySelection: {
      type: Object,
      default: null
    },
    historySearch: {
      type: String,
      default: ''
    }
  },
  emits: ['transcription-completed', 'title-change', 'clear-history-selection'],
  components: {
    StatusPill,
    TranscriptSegment
  },
  setup(props, { emit }) {
    const fileInput = ref(null)
    const selectedFile = ref(null)
    const inputMode = ref('upload')
    const isProcessing = ref(false)
    const isDragging = ref(false)
    const isRecording = ref(false)
    const isRecordingPaused = ref(false)
    const recordingSeconds = ref(0)
    const recordingError = ref('')
    const mediaRecorder = ref(null)
    const transcriptTitle = ref('New Transcription')
    const isEditingTitle = ref(false)
    const status = ref('Idle')
    const transcribedText = ref('')
    const segments = ref([])
    const errorMessage = ref('')
    const errorTitle = ref('Transcription failed.')
    const copyErrorMessage = ref('')
    const playbackErrorMessage = ref('')
    const detectedLanguage = ref('')
    const copyButtonText = ref('Copy Text')
    const uploadSection = ref(null)
    const selectedFileCard = ref(null)
    const browseButton = ref(null)
    const statusMessage = ref(null)
    const transcriptHeading = ref(null)
    const titleInput = ref(null)
    const transcriptScroller = ref(null)
    const exportMenu = ref(null)
    const inputOptionsMenu = ref(null)
    const audioUrl = ref('')
    const audioElement = ref(null)
    const isPlaying = ref(false)
    const currentTime = ref(0)
    const duration = ref(0)
    const recordingTimeDisplay = computed(() => {
      const hours = Math.floor(recordingSeconds.value / 3600)
      const minutes = Math.floor((recordingSeconds.value % 3600) / 60)
      const seconds = recordingSeconds.value % 60
      return [hours, minutes, seconds].map(value => String(value).padStart(2, '0')).join(':')
    })
    const recorderMessage = computed(() => {
      if (isRecording.value) return 'Recording in progress…'
      if (isRecordingPaused.value) return 'Recording paused'
      return 'Start a recording when you’re ready.'
    })
    const audioProgress = computed(() => duration.value ? Math.min(100, (currentTime.value / duration.value) * 100) : 0)
    const visualizerBars = Array.from({ length: 48 }, (_, index) => {
      const amplitude = Math.abs(Math.sin(index * 0.37) * 0.7 + Math.sin(index * 0.13) * 0.3)
      return Math.round(14 + amplitude * 64)
    })
    const MAX_FILE_SIZE = 25 * 1024 * 1024
    const ALLOWED_EXTENSIONS = new Set(['mp3', 'wav', 'm4a', 'flac', 'ogg', 'aac', 'wma', 'opus'])
    const supportedFormats = ['MP3', 'WAV', 'M4A', 'FLAC', 'OGG', 'AAC', 'WMA', 'OPUS']
    let copyResetTimeout
    let recordingTimer
    let recordingStream
    let recordingChunks = []
    let recordingExceededLimit = false
    let discardingRecording = false
    let loadedHistoryId = ''

    const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

    const statusClass = computed(() => {
      if (status.value === 'Idle') return 'status-idle'
      if (status.value === 'Processing') return 'status-processing'
      if (status.value === 'Completed') return 'status-completed'
      if (status.value === 'Error') return 'status-error'
      return ''
    })

    const statusLabel = computed(() => {
      if (status.value === 'Idle') return 'Ready when you are'
      if (status.value === 'Processing') return 'Transcribing with OpenAI Whisper AI…'
      if (status.value === 'Completed') return 'Transcription ready to copy or download'
      if (status.value === 'Error') return 'Error · Action needed'
      return status.value
    })

    const statusDescription = computed(() => {
      if (status.value === 'Idle') return 'Waiting for an audio file to process.'
      if (status.value === 'Processing') return 'Please wait while Whisper prepares your transcript.'
      if (status.value === 'Completed') return 'Transcription ready to copy or download.'
      if (status.value === 'Error') return 'Check the message below and try again.'
      return ''
    })

    const clearAudioPreview = () => {
      if (audioElement.value) {
        audioElement.value.pause()
        audioElement.value.removeAttribute('src')
        audioElement.value.load()
      }
      if (audioUrl.value) {
        URL.revokeObjectURL(audioUrl.value)
        audioUrl.value = ''
      }
      isPlaying.value = false
      currentTime.value = 0
      duration.value = 0
    }

    const focusSelectedFile = async () => {
      await nextTick()
      selectedFileCard.value?.focus()
    }

    const rejectFile = async (message) => {
      selectedFile.value = null
      transcribedText.value = ''
      segments.value = []
      emit('clear-history-selection')
      transcriptTitle.value = 'New Transcription'
      emit('title-change', transcriptTitle.value)
      copyErrorMessage.value = ''
      playbackErrorMessage.value = ''
      detectedLanguage.value = ''
      errorMessage.value = message
      errorTitle.value = 'Check your audio file.'
      status.value = 'Error'
      clearAudioPreview()
      if (fileInput.value) fileInput.value.value = ''
      await nextTick()
      statusMessage.value?.focus()
    }

    const setFile = (file) => {
      if (!file) return
      const extension = file.name.split('.').pop()?.toLowerCase()
      if (!extension || !ALLOWED_EXTENSIONS.has(extension)) {
        rejectFile('This audio format is not supported. Choose MP3, WAV, M4A, FLAC, OGG, AAC, WMA, or OPUS.')
        return
      }
      if (file.size > MAX_FILE_SIZE) {
        rejectFile('This file is larger than 25 MB. Choose a smaller audio file and try again.')
        return
      }
      clearAudioPreview()
      selectedFile.value = file
      errorMessage.value = ''
      errorTitle.value = 'Transcription failed.'
      copyErrorMessage.value = ''
      playbackErrorMessage.value = ''
      detectedLanguage.value = ''
      status.value = 'Idle'
      transcribedText.value = ''
      segments.value = []
      inputMode.value = 'upload'
      emit('clear-history-selection')
      transcriptTitle.value = file.name.replace(/\.[^.]+$/, '') || file.name
      emit('title-change', transcriptTitle.value)
      audioUrl.value = URL.createObjectURL(file)
      focusSelectedFile()
    }

    const handleFileSelect = (event) => {
      const files = event.target.files
      if (files && files.length > 0) {
        setFile(files[0])
      }
      event.target.value = ''
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
      detectedLanguage.value = ''
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

        const data = await response.json().catch(() => ({}))

        if (!response.ok) {
          throw new Error(data.error || `The server returned an error (${response.status}). Please try again.`)
        }

        if (typeof data.transcription !== 'string') {
          throw new Error('The transcription service returned an invalid response. Please try again.')
        }
        if (!data.transcription.trim()) {
          throw new Error('No speech was detected in this audio. Try a recording with clearer speech.')
        }
        transcribedText.value = data.transcription
        segments.value = Array.isArray(data.segments) ? data.segments : []
        detectedLanguage.value = typeof data.language === 'string' ? data.language : ''
        status.value = 'Completed'
        emit('transcription-completed', {
          title: transcriptTitle.value,
          text: transcribedText.value,
          segments: segments.value
        })
        await nextTick()
        transcriptHeading.value?.focus()

      } catch (error) {
        console.error('Transcription error:', error)
        errorMessage.value = error instanceof Error && error.message === 'Failed to fetch'
          ? 'The transcription service could not be reached. Check that the backend is running, then try again.'
          : (error.message || 'The audio could not be transcribed. Please try another file.')
        errorTitle.value = 'Transcription failed.'
        status.value = 'Error'
        await nextTick()
        statusMessage.value?.focus()
      } finally {
        isProcessing.value = false
      }
    }

    const formatFileSize = (bytes) => {
      if (bytes === 0) return '0 B'
      const k = 1024
      const sizes = ['B', 'KB', 'MB']
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
        copyErrorMessage.value = ''
        copyButtonText.value = 'Copied!'
        clearTimeout(copyResetTimeout)
        copyResetTimeout = setTimeout(() => {
          copyButtonText.value = 'Copy Text'
        }, 2000)
      } catch (error) {
        copyErrorMessage.value = 'Could not copy the transcript. Check browser clipboard permissions and try again.'
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
      document.body.appendChild(link)
      link.click()
      link.remove()
      window.setTimeout(() => URL.revokeObjectURL(url), 1000)
    }

    const downloadAndClose = () => {
      downloadText()
      if (exportMenu.value) exportMenu.value.open = false
    }

    const resetInput = ({ focus = true } = {}) => {
      selectedFile.value = null
      transcribedText.value = ''
      segments.value = []
      status.value = 'Idle'
      errorMessage.value = ''
      errorTitle.value = 'Transcription failed.'
      copyErrorMessage.value = ''
      playbackErrorMessage.value = ''
      detectedLanguage.value = ''
      recordingError.value = ''
      transcriptTitle.value = 'New Transcription'
      emit('clear-history-selection')
      isEditingTitle.value = false
      emit('title-change', transcriptTitle.value)
      if (fileInput.value) {
        fileInput.value.value = ''
      }
      clearAudioPreview()
      if (focus) {
        nextTick(() => {
          if (inputMode.value === 'upload') browseButton.value?.focus()
          else inputOptionsMenu.value?.querySelector('summary')?.focus()
        })
      }
    }

    const openFilePicker = () => {
      if (!isProcessing.value) fileInput.value?.click()
    }

    const selectInputMode = (mode) => {
      if (isProcessing.value || isRecording.value || isRecordingPaused.value) return
      if (mode === 'record' && audioElement.value) audioElement.value.pause()
      inputMode.value = mode
      recordingError.value = ''
    }

    const clearInputAndClose = async () => {
      if (inputOptionsMenu.value) inputOptionsMenu.value.open = false
      resetInput({ focus: false })
      await nextTick()
      if (inputMode.value === 'upload') browseButton.value?.focus()
      else inputOptionsMenu.value?.querySelector('summary')?.focus()
    }

    const toggleTitleEdit = async () => {
      if (!isEditingTitle.value) {
        isEditingTitle.value = true
        await nextTick()
        titleInput.value?.focus()
        titleInput.value?.select()
        return
      }
      transcriptTitle.value = transcriptTitle.value.trim() || 'Untitled transcription'
      isEditingTitle.value = false
      emit('title-change', transcriptTitle.value)
    }

    const stopRecordingTracks = () => {
      if (!recordingStream) return
      recordingStream.getTracks().forEach(track => track.stop())
      recordingStream = null
    }

    const encodeRecordingAsWav = async (blob) => {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext
      if (!AudioContextClass) throw new Error('This browser cannot prepare the recording for transcription. Please upload an audio file instead.')
      const context = new AudioContextClass()
      try {
        const decoded = await context.decodeAudioData(await blob.arrayBuffer())
        const channels = Math.min(decoded.numberOfChannels, 2)
        const bytesPerSample = 2
        const dataLength = decoded.length * channels * bytesPerSample
        const buffer = new ArrayBuffer(44 + dataLength)
        const view = new DataView(buffer)
        const writeString = (offset, value) => {
          for (let index = 0; index < value.length; index += 1) view.setUint8(offset + index, value.charCodeAt(index))
        }
        writeString(0, 'RIFF')
        view.setUint32(4, 36 + dataLength, true)
        writeString(8, 'WAVE')
        writeString(12, 'fmt ')
        view.setUint32(16, 16, true)
        view.setUint16(20, 1, true)
        view.setUint16(22, channels, true)
        view.setUint32(24, decoded.sampleRate, true)
        view.setUint32(28, decoded.sampleRate * channels * bytesPerSample, true)
        view.setUint16(32, channels * bytesPerSample, true)
        view.setUint16(34, bytesPerSample * 8, true)
        writeString(36, 'data')
        view.setUint32(40, dataLength, true)
        const channelData = Array.from({ length: channels }, (_, index) => decoded.getChannelData(index))
        let offset = 44
        for (let frame = 0; frame < decoded.length; frame += 1) {
          for (let channel = 0; channel < channels; channel += 1) {
            const sample = Math.max(-1, Math.min(1, channelData[channel][frame]))
            view.setInt16(offset, sample < 0 ? sample * 0x8000 : sample * 0x7fff, true)
            offset += bytesPerSample
          }
        }
        return new File([buffer], `recording-${new Date().toISOString().replace(/[:.]/g, '-')}.wav`, { type: 'audio/wav' })
      } finally {
        await context.close()
      }
    }

    const startRecording = async () => {
      recordingError.value = ''
      if (!navigator.mediaDevices?.getUserMedia || typeof MediaRecorder === 'undefined') {
        recordingError.value = 'Audio recording is not supported in this browser. You can upload an audio file instead.'
        return
      }
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
        if (typeof MediaRecorder === 'undefined') {
          stream.getTracks().forEach(track => track.stop())
          throw new Error('Audio recording is not supported in this browser. You can upload an audio file instead.')
        }
        resetInput({ focus: false })
        inputMode.value = 'record'
        recordingStream = stream
        recordingChunks = []
        recordingExceededLimit = false
        discardingRecording = false
        recordingSeconds.value = 0
        const preferredMime = ['audio/webm;codecs=opus', 'audio/ogg;codecs=opus', 'audio/mp4']
          .find(type => MediaRecorder.isTypeSupported?.(type))
        const recorder = new MediaRecorder(stream, preferredMime ? { mimeType: preferredMime } : undefined)
        mediaRecorder.value = recorder
        recorder.ondataavailable = (event) => {
          if (!event.data.size) return
          recordingChunks.push(event.data)
          const recordedSize = recordingChunks.reduce((total, chunk) => total + chunk.size, 0)
          if (recordedSize > MAX_FILE_SIZE && !recordingExceededLimit) {
            recordingExceededLimit = true
            recordingError.value = 'This recording has reached the 25 MB limit. Stop and make a shorter recording.'
            if (recorder.state !== 'inactive') recorder.stop()
          }
        }
        recorder.onerror = () => {
          recordingError.value = 'The recording could not be completed. Check microphone access and try again.'
          isRecording.value = false
          isRecordingPaused.value = false
          clearInterval(recordingTimer)
          stopRecordingTracks()
        }
        recorder.onstop = async () => {
          clearInterval(recordingTimer)
          isRecording.value = false
          isRecordingPaused.value = false
          stopRecordingTracks()
          if (discardingRecording) return
          if (recordingExceededLimit) return
          const recording = new Blob(recordingChunks, { type: recorder.mimeType || 'audio/webm' })
          recordingChunks = []
          if (!recording.size) {
            recordingError.value = 'No audio was captured. Check your microphone and try again.'
            return
          }
          try {
            const wavFile = await encodeRecordingAsWav(recording)
            inputMode.value = 'upload'
            setFile(wavFile)
          } catch (error) {
            recordingError.value = error instanceof Error ? error.message : 'The recording could not be prepared. Please upload an audio file instead.'
          }
        }
        recorder.start(1000)
        isRecording.value = true
        recordingTimer = window.setInterval(() => { recordingSeconds.value += 1 }, 1000)
      } catch (error) {
        recordingError.value = error instanceof Error && error.name === 'NotAllowedError'
          ? 'Microphone access was denied. Allow microphone access or upload an audio file instead.'
          : (error instanceof Error ? error.message : 'Could not start recording. Please try again.')
        stopRecordingTracks()
      }
    }

    const toggleRecordingPause = () => {
      const recorder = mediaRecorder.value
      if (!recorder) return
      if (recorder.state === 'recording') {
        recorder.pause()
        isRecording.value = false
        isRecordingPaused.value = true
        clearInterval(recordingTimer)
      } else if (recorder.state === 'paused') {
        recorder.resume()
        isRecording.value = true
        isRecordingPaused.value = false
        recordingTimer = window.setInterval(() => { recordingSeconds.value += 1 }, 1000)
      }
    }

    const stopRecording = () => {
      const recorder = mediaRecorder.value
      clearInterval(recordingTimer)
      isRecording.value = false
      isRecordingPaused.value = false
      if (recorder && recorder.state !== 'inactive') recorder.stop()
    }

    const togglePlay = async () => {
      if (!audioElement.value) return
      if (isPlaying.value) {
        audioElement.value.pause()
      } else {
        playbackErrorMessage.value = ''
        try {
          await audioElement.value.play()
        } catch {
          playbackErrorMessage.value = 'Audio playback could not start. Try using the play button again.'
        }
      }
    }

    const stopPlayback = () => {
      if (!audioElement.value) return
      audioElement.value.pause()
      audioElement.value.currentTime = 0
      currentTime.value = 0
    }

    const onAudioLoaded = () => {
      if (audioElement.value) {
        duration.value = Number.isFinite(audioElement.value.duration) ? audioElement.value.duration : 0
      }
    }

    const onTimeUpdate = () => {
      if (audioElement.value) {
        currentTime.value = audioElement.value.currentTime || 0
      }
    }

    const seekAudio = (event) => {
      if (!audioElement.value) return
      audioElement.value.currentTime = Number(event.target.value)
    }

    const seekToSegment = (start) => {
      if (!audioElement.value || !audioUrl.value) return
      const target = Math.max(0, start || 0)
      audioElement.value.currentTime = target
      playbackErrorMessage.value = ''
      audioElement.value.play().catch(() => {
        playbackErrorMessage.value = 'Audio playback could not start. Try using the play button again.'
      })
    }

    const currentTimeDisplay = computed(() => formatTime(currentTime.value))
    const durationDisplay = computed(() => formatTime(duration.value))
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

    watch(() => props.historySelection, async (item) => {
      if (!item) {
        loadedHistoryId = ''
        return
      }
      if (item.id === loadedHistoryId) return
      if (status.value === 'Completed' && item.text === transcribedText.value && item.title === transcriptTitle.value && audioUrl.value) {
        loadedHistoryId = item.id
        return
      }
      clearAudioPreview()
      selectedFile.value = null
      transcribedText.value = item.text
      segments.value = item.segments
      transcriptTitle.value = item.title
      isEditingTitle.value = false
      status.value = 'Completed'
      errorMessage.value = ''
      copyErrorMessage.value = ''
      detectedLanguage.value = ''
      copyButtonText.value = 'Copy Text'
      if (fileInput.value) fileInput.value.value = ''
      loadedHistoryId = item.id
      emit('title-change', transcriptTitle.value)
      await nextTick()
      transcriptHeading.value?.focus()
    }, { immediate: true })

    watch(activeSegmentIndex, async (index) => {
      if (index < 0) return
      await nextTick()
      transcriptScroller.value?.querySelector('.transcript-row.active')?.scrollIntoView({
        block: 'nearest',
        behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
      })
    })

    onBeforeUnmount(() => {
      clearTimeout(copyResetTimeout)
      clearInterval(recordingTimer)
      discardingRecording = true
      if (mediaRecorder.value && mediaRecorder.value.state !== 'inactive') {
        mediaRecorder.value.onstop = null
        mediaRecorder.value.stop()
      }
      stopRecordingTracks()
      clearAudioPreview()
    })

    return {
      fileInput,
      inputMode,
      supportedFormats,
      uploadSection,
      selectedFileCard,
      browseButton,
      statusMessage,
      transcriptHeading,
      titleInput,
      transcriptScroller,
      inputOptionsMenu,
      transcriptTitle,
      isEditingTitle,
      exportMenu,
      selectedFile,
      isProcessing,
      isDragging,
      isRecording,
      isRecordingPaused,
      recordingSeconds,
      recordingTimeDisplay,
      recorderMessage,
      recordingError,
      status,
      transcribedText,
      segments,
      errorMessage,
      errorTitle,
      copyErrorMessage,
      playbackErrorMessage,
      detectedLanguage,
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
      audioProgress,
      visualizerBars,
      openFilePicker,
      selectInputMode,
      startRecording,
      toggleRecordingPause,
      stopRecording,
      toggleTitleEdit,
      clearInputAndClose,
      togglePlay,
      stopPlayback,
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
      downloadAndClose,
      resetInput
    }
  }
}
</script>

<style scoped>
.home-page {
  display: block;
}
</style>
