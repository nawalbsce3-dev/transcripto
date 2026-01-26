<template>
  <div class="page">
    <div class="bg-gradient"></div>
    <div class="grain"></div>

    <div class="shell">
      <header class="topbar">
        <router-link to="/" class="brand">
          <span class="logo-dot"></span>
          <span class="brand-name">Transcripto</span>
        </router-link>
        
        <nav class="nav-menu">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/features" class="nav-link">Features</router-link>
          <router-link to="/how-it-works" class="nav-link">How It Works</router-link>
          <router-link to="/about" class="nav-link">About</router-link>
        </nav>
      </header>

      <router-view />

      <footer class="footer">
        <div class="footer-content">
          <div class="footer-brand">
            <span class="logo-dot"></span>
            <span class="brand-name">Transcripto</span>
          </div>
          <p class="footer-text">AI-Powered Audio Transcription Platform</p>
          <p class="footer-copy">© 2026 Transcripto • Portfolio Project • Built with Vue.js & OpenAI Whisper</p>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
