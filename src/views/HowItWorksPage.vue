<template>
  <div class="how-it-works-page">
    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">Simple Process</div>
        <h2>How It Works</h2>
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
          <p>OpenAI Whisper AI analyzes your audio, detecting speech patterns, speakers, and generating accurate timestamps for each segment.</p>
        </div>
        <div class="step-card">
          <div class="step-number">3</div>
          <h3>Get Results</h3>
          <p>Receive a clean, timestamped transcript with speaker labels. Play audio alongside the transcript, click segments to jump to any point.</p>
        </div>
        <div class="step-card">
          <div class="step-number">4</div>
          <h3>Export & Share</h3>
          <p>Copy to clipboard or download as a text file. Ready for documentation, subtitles, analysis, or integration with your workflow.</p>
        </div>
      </div>
    </section>

    <section class="info-section">
      <div class="section-header centered">
        <div class="eyebrow">Get Started</div>
        <h2>Ready to Transcribe?</h2>
        <p class="section-desc">Upload your first audio file and experience AI-powered transcription</p>
      </div>
      <div style="text-align: center; margin-top: 24px;">
        <router-link to="/" class="cta">Start Converting Now</router-link>
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
