<template>
  <div class="features-page">
    <section class="features">
      <div class="section-header centered">
        <div class="eyebrow">Core Features</div>
        <h1>Everything You Need</h1>
      </div>
      <div class="features-grid">
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M13 2L3 14h6l-2 8 10-12h-6l2-8z"></path>
            </svg>
          </div>
          <h3>AI-Assisted Transcription</h3>
          <p>Whisper creates a useful first draft. Results can vary with recording quality, accents, background noise, and the selected model.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 12a8 8 0 0 1 16 0"></path>
              <path d="M4 12v4a2 2 0 0 0 2 2h2v-5H4z"></path>
              <path d="M20 12v4a2 2 0 0 1-2 2h-2v-5h4z"></path>
            </svg>
          </div>
          <h3>Multi-Format Support</h3>
          <p>Upload MP3, WAV, M4A, FLAC, OGG, AAC, WMA, or OPUS audio for podcasts, meetings, interviews, and more.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
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
          </div>
          <h3>Multilingual Speech Support</h3>
          <p>OpenAI Whisper supports speech transcription across languages. Clarity depends on the audio and speaking conditions.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="7"></circle>
              <path d="M12 9v4l3 2"></path>
            </svg>
          </div>
          <h3>Timestamped Segments</h3>
          <p>Segments include timestamps. Click a line to jump to that point in the audio.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="7" cy="7" r="2"></circle>
              <circle cx="17" cy="7" r="2"></circle>
              <path d="M5 21v-2a4 4 0 0 1 4-4h6a4 4 0 0 1 4 4v2"></path>
            </svg>
          </div>
          <h3>Estimated Speaker Labels</h3>
          <p>Basic speaker labels are estimated from pauses in the audio. They are not verified speaker identification or diarization.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="8"></circle>
              <path d="M10 9v6l5-3z"></path>
            </svg>
          </div>
          <h3>Synchronized Playback</h3>
          <p>Built-in audio player with real-time transcript highlighting. Follow along as the audio plays.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 3v12"></path>
              <path d="M7 12l5 5 5-5"></path>
              <path d="M5 19h14"></path>
            </svg>
          </div>
          <h3>Easy Export</h3>
          <p>Copy the transcript or download it as a TXT file for your notes and documentation.</p>
        </div>
        <div class="feature-card">
          <div class="icon-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="5" y="11" width="14" height="9" rx="2"></rect>
              <path d="M8 11V7a4 4 0 0 1 8 0v4"></path>
            </svg>
          </div>
          <h3>Temporary File Handling</h3>
          <p>Audio is temporarily stored on the server for processing and removed afterward. The app does not keep a transcript history.</p>
        </div>
      </div>
    </section>

    <section class="info-section formats-section">
      <div class="section-header">
        <div class="eyebrow">Audio Compatibility</div>
        <h2>Supported Formats</h2>
        <p class="section-desc">Upload one of the supported audio formats. Each file can be up to 25 MB.</p>
      </div>
      <div class="formats-grid">
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          MP3
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          WAV
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          M4A
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          FLAC
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          OGG
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          AAC
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          WMA
        </div>
        <div class="format-badge">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 18V5l9-2v13"></path>
            <circle cx="6" cy="18" r="2"></circle>
            <circle cx="15" cy="16" r="2"></circle>
          </svg>
          OPUS
        </div>
      </div>
      <div class="format-note">
        <p>Maximum file size: 25 MB</p>
        <p>Formats are checked before transcription</p>
        <p>Processing time depends on file length and hardware</p>
      </div>
    </section>

    <section class="cta-panel">
      <div>
        <h2>Ready to make a first draft?</h2>
        <p>Upload an audio file and review a timestamped transcript.</p>
      </div>
      <router-link to="/#workspace" class="cta">Start transcribing <span aria-hidden="true">→</span></router-link>
    </section>
  </div>
</template>

<script>
export default {
  name: 'FeaturesPage'
}
</script>

<style scoped>
.features-page {
  display: flex;
  flex-direction: column;
  gap: 32px;
}
</style>
