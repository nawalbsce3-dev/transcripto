<template>
  <div class="about-page">
    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">About Transcripto</div>
        <h2>Professional Audio-to-Text Platform</h2>
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
          <p>Transcripto is a modern, AI-powered transcription platform that converts audio files into accurate, timestamped text transcriptions. Built with OpenAI's Whisper AI model, it delivers professional-grade results for podcasts, meetings, interviews, and more.</p>
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
          <p>Get speaker-separated transcriptions with precise timestamps, support for multiple audio formats, and an intuitive interface. Perfect for content creators, researchers, journalists, and business professionals.</p>
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
          <div class="tech-value">OpenAI Whisper</div>
        </div>
        <div class="tech-item">
          <div class="tech-label">Audio Processing</div>
          <div class="tech-value">FFmpeg</div>
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
            <a href="https://n-porfolio-v1.vercel.app/" target="_blank" rel="noreferrer" class="credit-link">
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
            <a href="#" class="credit-link">
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
          <p class="credit-text">Designed for content creators, podcasters, researchers, journalists, and professionals who need fast, accurate audio transcription.</p>
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
      <div class="tech-credits">
        <h4>Powered By</h4>
        <p>OpenAI Whisper AI • Vue.js 3 • Flask • FFmpeg • Python • Vite</p>
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
  gap: 32px;
}
</style>
