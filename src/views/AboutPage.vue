<template>
  <div class="about-page">
    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">About Transcripto</div>
        <h1>Professional Audio-to-Text Platform</h1>
      </div>
      <div class="info-grid">
        <div class="info-card">
          <div class="info-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="8"></circle>
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M12 2v2"></path>
              <path d="M12 20v2"></path>
              <path d="M2 12h2"></path>
              <path d="M20 12h2"></path>
            </svg>
          </div>
          <h3>What is Transcripto?</h3>
          <p>Transcripto is a focused audio-to-text utility that runs OpenAI Whisper on its own server to create timestamped transcript drafts for podcasts, meetings, interviews, and more. Audio is not sent to a third-party AI API. Results depend on audio quality, accents, and background noise.</p>
        </div>
        <div class="info-card">
          <div class="info-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 18h6"></path>
              <path d="M10 22h4"></path>
              <path d="M8 14a6 6 0 1 1 8 0c-.8.7-1 1.7-1 2.7V18H9v-1.3c0-1-.2-2-1-2.7Z"></path>
            </svg>
          </div>
          <h3>Why Choose Transcripto?</h3>
          <p>Upload MP3, WAV, M4A, FLAC, OGG, AAC, WMA, or OPUS files up to 25 MB, review timestamped segments alongside playback, then copy or download the transcript. Speaker labels are estimated from pauses and are not true diarization.</p>
        </div>
      </div>
    </section>

    <section class="info-section tech-section">
      <div class="section-header centered">
        <div class="eyebrow">Technology</div>
        <h2>Built With Modern Stack</h2>
      </div>
      <div class="tech-grid">
        <div class="tech-item">
          <div class="tech-label">Frontend</div>
          <div class="tech-value">Vue 3 + Vite</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">Backend</div>
          <div class="tech-value">Flask + Python</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">AI Model</div>
          <div class="tech-value">OpenAI Whisper (local)</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">ML Runtime</div>
          <div class="tech-value">PyTorch</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">Audio Processing</div>
          <div class="tech-value">FFmpeg</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">Model Size</div>
          <div class="tech-value">Base (tiny to large supported)</div>
        </div>
      </div>
    </section>

    <section class="info-section credits-section">
      <div class="section-header centered">
        <div class="eyebrow">About This Project</div>
        <h2>Development & Credits</h2>
      </div>
      <div class="credits-grid">
        <div class="credit-card">
          <h3>Developed By</h3>
          <p class="credit-text">Built as a portfolio project showcasing modern web development, AI integration, and full-stack capabilities.</p>
          <div class="credit-links">
            <a href="https://nawaldot.com/" target="_blank" rel="noreferrer" class="credit-link">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="7" r="4"></circle>
                <path d="M5.5 21a6.5 6.5 0 0 1 13 0"></path>
              </svg>
              Developer Portfolio
            </a>
            <a href="https://www.linkedin.com/in/nawal-mudassar-ali-b81a532a0" target="_blank" rel="noreferrer" class="credit-link">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 7h18"></path>
                <path d="M3 11h18"></path>
                <path d="M9 7v10"></path>
                <path d="M15 7v10"></path>
                <path d="M7 21h10"></path>
              </svg>
              LinkedIn
            </a>
            <a href="https://github.com/nawalbsce3-dev/transcripto" target="_blank" rel="noreferrer" class="credit-link">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 8h8"></path>
                <path d="M8 12h8"></path>
                <path d="M8 16h5"></path>
                <rect x="4" y="4" width="16" height="16" rx="2"></rect>
              </svg>
              GitHub
            </a>
          </div>
        </div>
        <div class="credit-card">
          <h3>Developed For</h3>
          <p class="credit-text">Designed for creators, podcasters, researchers, journalists, and professionals who need a clear audio-to-text first draft.</p>
          <ul class="use-cases">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 13l4 4L19 7"></path>
              </svg>
              Meeting transcriptions
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 13l4 4L19 7"></path>
              </svg>
              Podcast episodes
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 13l4 4L19 7"></path>
              </svg>
              Interview recordings
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 13l4 4L19 7"></path>
              </svg>
              Lecture notes
            </li>
          </ul>
        </div>
      </div>
      <div class="privacy-note">
        <strong>Privacy &amp; temporary processing</strong>
        <ul class="privacy-list">
          <li>Your audio is uploaded to the Transcripto server and stored temporarily, only while it is being transcribed.</li>
          <li>The file is deleted as soon as processing finishes.</li>
          <li>Transcription runs on the server with a local Whisper model, so audio is not sent to a third-party AI API.</li>
          <li>Transcripts are not stored. Transcripto has no accounts, permanent storage, or transcript history.</li>
          <li>Uploads are checked for file type and size (25 MB limit) before processing.</li>
          <li>This is a portfolio project, so please avoid uploading sensitive or confidential recordings.</li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'AboutPage'
}
</script>

<style scoped>
.about-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
  color: var(--ink);
}

.info-grid,
.credits-grid,
.tech-grid {
  gap: 12px;
}

.info-icon {
  border-color: #e4dff2;
  background: var(--accent-soft);
  color: var(--accent);
}

.tech-item {
  border-color: var(--line);
  background: #f8f7fc;
}

.tech-label {
  color: var(--muted);
}

.tech-value {
  color: var(--accent);
}

.credit-link {
  border-color: var(--line);
  background: #fff;
  color: var(--accent);
}

.privacy-note {
  border-color: var(--line-strong);
  background: var(--accent-soft);
  color: var(--ink-soft);
}

.privacy-note strong {
  color: var(--accent);
}

.privacy-list {
  margin: 10px 0 0;
  padding-left: 20px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
</style>