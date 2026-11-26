<template>
  <div class="how-it-works-page">
    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">Simple Process</div>
        <h1>How It Works</h1>
      </div>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-number">1</div>
          <h3>Upload Audio</h3>
          <p>Drag and drop your audio file or browse to select. Supports MP3, WAV, M4A, FLAC, OGG, AAC, WMA, and OPUS formats.</p>
        </div>
        <div class="step-card">
          <div class="step-number">2</div>
          <h3>AI Processing</h3>
          <p>OpenAI Whisper transcribes the audio and creates timestamped segments. Processing time varies with file length and hardware.</p>
        </div>
        <div class="step-card">
          <div class="step-number">3</div>
          <h3>Get Results</h3>
          <p>Review timestamped text alongside your audio. Speaker labels are basic estimates based on pauses, not verified identities.</p>
        </div>
        <div class="step-card">
          <div class="step-number">4</div>
          <h3>Export & Share</h3>
          <p>Copy the transcript or download it as a TXT file. Other export formats are not currently available.</p>
        </div>
      </div>
    </section>

    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">Get Started</div>
        <h2>Ready to Transcribe?</h2>
        <p class="section-desc">Upload your first audio file and experience AI-powered transcription</p>
      </div>
      <div class="cta-panel">
        <div>
          <h2>Start with your audio</h2>
          <p>Processing time depends on file length and available hardware.</p>
        </div>
        <router-link to="/#workspace" class="cta">Start Converting Now <span aria-hidden="true">→</span></router-link>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HowItWorksPage'
}
</script>

<style scoped>
.how-it-works-page {
  display: flex;
  flex-direction: column;
  gap: 32px;
}
</style>
