<template>
  <div class="landing" :data-theme="manualTheme" @keydown.esc="mobileNavOpen = false">
    <a class="skip-link" href="#main-content">Skip to content</a>

    <header class="site-header" :class="{ 'is-scrolled': scrolled }">
      <div class="header-inner">
        <router-link class="wordmark" to="/" aria-label="Transcripto home">
          <img src="/Transcripto_Logo_Purple.png" alt="Transcripto" />
        </router-link>

        <nav class="desktop-nav" aria-label="Primary navigation">
          <a href="#features">Features</a>
          <a href="#how-it-works">How it works</a>
          <a href="#security">Security</a>
          <a href="#faq">FAQ</a>
        </nav>

        <div class="header-actions">
          <router-link class="button button-primary button-small" to="/transcribe">Open app</router-link>
          <button
            class="menu-button"
            type="button"
            :aria-expanded="mobileNavOpen"
            aria-controls="mobile-navigation"
            aria-label="Toggle navigation"
            @click="mobileNavOpen = !mobileNavOpen"
          >
            <svg v-if="!mobileNavOpen" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
            <svg v-else viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg>
          </button>
        </div>
      </div>

      <nav v-if="mobileNavOpen" id="mobile-navigation" class="mobile-nav" aria-label="Mobile navigation">
        <a href="#features" @click="mobileNavOpen = false">Features</a>
        <a href="#how-it-works" @click="mobileNavOpen = false">How it works</a>
        <a href="#security" @click="mobileNavOpen = false">Security</a>
        <a href="#faq" @click="mobileNavOpen = false">FAQ</a>
        <router-link to="/transcribe" @click="mobileNavOpen = false">Open app</router-link>
      </nav>
    </header>

    <main id="main-content">
      <section class="hero container" aria-labelledby="hero-title">
        <div class="hero-copy reveal">
          <p class="eyebrow">Self-hosted · OpenAI Whisper</p>
          <h1 id="hero-title">Audio to <span>timestamped transcript</span>, on your own infrastructure.</h1>
          <p class="hero-subhead">25 MB per file, 8 formats, and transcription history that stays in localStorage. Process recordings through a local Flask and Whisper stack.</p>
          <div class="hero-actions">
            <router-link class="button button-primary" to="/transcribe">
              Start transcribing
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-5-5 5 5-5 5" /></svg>
            </router-link>
            <a class="button button-secondary" href="https://github.com/nawalbsce3-dev/transcripto#readme" target="_blank" rel="noreferrer">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11a3 3 0 0 1 3 3v15a3 3 0 0 0-3-3H6.5A2.5 2.5 0 0 0 4 20.5zM14 6a3 3 0 0 1 3-3h2.5A2.5 2.5 0 0 1 22 5.5v15a2.5 2.5 0 0 0-2.5-2.5H17a3 3 0 0 0-3 3" /></svg>
              Read the docs
            </a>
          </div>
          <p class="trust-row">
            <span>No account required</span><b aria-hidden="true">·</b>
            <span>Audio deleted after processing</span><b aria-hidden="true">·</b>
            <span>Runs on your server</span>
          </p>
        </div>

        <div class="hero-product reveal" aria-hidden="true">
          <div class="product-window">
            <div class="window-bar">
              <div class="window-dots"><i></i><i></i><i></i></div>
              <span>Interview.wav</span>
              <span class="window-status"><i></i> Complete</span>
            </div>
            <div class="product-playback">
              <button type="button" tabindex="-1" aria-hidden="true">
                <svg viewBox="0 0 24 24"><path d="m8 5 11 7-11 7z" /></svg>
              </button>
              <div class="waveform">
                <i v-for="n in 32" :key="n" :style="{ height: `${waveHeight(n)}%` }"></i>
              </div>
              <span class="timecode">03:42 / 08:15</span>
            </div>
            <div class="transcript-view">
              <div class="transcript-segment">
                <span>00:12</span>
                <p>The first pass should preserve the original structure and names.</p>
              </div>
              <div class="transcript-segment is-active">
                <span>01:44</span>
                <p>Each segment includes a start time and end time for playback.</p>
              </div>
              <div class="transcript-segment">
                <span>02:31</span>
                <p>Whisper returns the text locally; the result is saved in this browser.</p>
              </div>
              <div class="transcript-segment">
                <span>03:42</span>
                <p>Copy the text or export the available analysis formats.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="spec-strip" aria-label="Technology stack">
        <div class="container spec-inner">
          <span>Built with</span>
          <ul>
            <li>Vue 3</li>
            <li>Vite</li>
            <li>Flask</li>
            <li>OpenAI Whisper</li>
          </ul>
        </div>
      </section>

      <section id="features" class="section container" aria-labelledby="features-title">
        <div class="section-heading reveal">
          <p class="section-kicker">Product capabilities</p>
          <h2 id="features-title">A complete path from audio to reviewed text.</h2>
        </div>

        <div class="bento-grid">
          <article class="feature-card feature-wide reveal">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></svg>
            <h3>Timestamped playback</h3>
            <p>Jump between timestamped segments while reviewing the original recording.</p>
            <div class="mini-transcript" aria-hidden="true">
              <button type="button" tabindex="-1">00:12</button>
              <button type="button" tabindex="-1" class="is-active">01:44</button>
              <button type="button" tabindex="-1">02:31</button>
              <button type="button" tabindex="-1">03:42</button>
            </div>
          </article>

          <article class="feature-card reveal">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="M7 9h10M7 13h6" /></svg>
            <h3>Browser-only history</h3>
            <p>Recent results remain available without an account or database.</p>
            <div class="mono-chip">20 / 20 saved</div>
          </article>

          <article class="feature-card reveal">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m-5-5 5 5 5-5" /><path d="M5 21h14" /></svg>
            <h3>Eight audio formats</h3>
            <p>Upload one of the accepted audio containers.</p>
            <div class="format-grid" aria-label="Supported formats">
              <span v-for="format in formats" :key="format">{{ format }}</span>
            </div>
          </article>

          <article class="feature-card reveal">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m5 10V4m6 16v-7m5 7V7" /></svg>
            <h3>Local analysis</h3>
            <p>Metrics are calculated from the saved transcript and segment timestamps.</p>
            <div class="stat-row">
              <div><span>WPM</span><strong>142</strong></div>
              <div><span>Pauses</span><strong>12</strong></div>
              <div><span>Unique</span><strong>38%</strong></div>
            </div>
          </article>

          <article class="feature-card feature-wide reveal">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m-5-5 5 5 5-5" /><path d="M5 21h14" /></svg>
            <h3>Export anywhere</h3>
            <p>Copy the generated text or retain segment and metric data in a separate format.</p>
            <div class="export-pills">
              <button type="button" tabindex="-1">Download <code>.txt</code></button>
              <button type="button" tabindex="-1">Export <code>CSV / JSON</code></button>
            </div>
          </article>
        </div>
      </section>

      <section id="how-it-works" class="section how-section" aria-labelledby="how-title">
        <div class="container">
          <div class="section-heading reveal">
            <p class="section-kicker">How it works</p>
            <h2 id="how-title">A direct request, with the temporary file removed afterward.</h2>
          </div>

          <div class="steps reveal">
            <article>
              <span class="step-number">01</span>
              <h3>Add audio</h3>
              <p>Choose a file or record directly in the browser.</p>
            </article>
            <article>
              <span class="step-number">02</span>
              <h3>Send to the API</h3>
              <p>The file is posted as multipart form data.</p>
            </article>
            <article>
              <span class="step-number">03</span>
              <h3>Whisper transcribes</h3>
              <p>The base model can extract text and segments.</p>
            </article>
            <article>
              <span class="step-number">04</span>
              <h3>Read, analyse, export</h3>
              <p>Review timestamps or download the result.</p>
            </article>
            <code class="endpoint">POST /api/transcribe</code>
          </div>
        </div>
      </section>

      <section id="security" class="security-band" aria-labelledby="security-title">
        <div class="container security-grid">
          <div class="security-copy reveal">
            <p class="section-kicker">Security and privacy</p>
            <h2 id="security-title">Processing stays under your control.</h2>
            <p>Transcripto has no external transcription API, account system, or database. Audio and history have separate lifetimes: temporary server files are removed after processing, and browser history is stored only on the current device.</p>
          </div>
          <ul class="checklist reveal">
            <li>
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" /></svg>
              <span>Uploads are written to disk and deleted immediately after processing</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" /></svg>
              <span>No database or external history service</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" /></svg>
              <span>History is capped at 20 entries in localStorage</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12 4 4L19 6" /></svg>
              <span><code>fp16=False</code> — CPU execution needs no GPU</span>
            </li>
          </ul>
        </div>
      </section>

      <section class="section container dashboard-preview" aria-labelledby="analysis-title">
        <div class="analysis-copy reveal">
          <p class="section-kicker">Local analysis</p>
          <h2 id="analysis-title">Inspect pacing and structure after transcription.</h2>
          <p>Duration, pace, silence, and repeated terms are derived from the saved text and Whisper segment timestamps. Nothing is sent for a second AI pass.</p>
          <router-link class="text-link" to="/transcribe">
            View a sample analysis
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-5-5 5 5-5 5" /></svg>
          </router-link>
        </div>

        <div class="analysis-card reveal" aria-label="Analysis dashboard preview" aria-hidden="true">
          <div class="analysis-stat-grid">
            <div><span>Words</span><strong>1,284</strong><small>944 unique</small></div>
            <div><span>WPM</span><strong>142</strong><small>conversational</small></div>
            <div><span>Pauses</span><strong>12</strong><small>2.8s longest</small></div>
            <div><span>Unique %</span><strong>38%</strong><small>vocabulary variety</small></div>
          </div>
          <div class="distribution">
            <div class="distribution-head">
              <span>Segment length</span>
              <code>seconds</code>
            </div>
            <div class="bar-chart">
              <i style="height:42%;opacity:.35"></i>
              <i style="height:76%;opacity:.75"></i>
              <i style="height:58%;opacity:.55"></i>
              <i style="height:92%;opacity:1"></i>
              <i style="height:68%;opacity:.65"></i>
              <i style="height:48%;opacity:.45"></i>
              <i style="height:82%;opacity:.82"></i>
              <i style="height:62%;opacity:.58"></i>
            </div>
          </div>
        </div>
      </section>

      <section class="cta-band" aria-labelledby="cta-title">
        <div class="container cta-inner">
          <div>
            <h2 id="cta-title">Use your own server for the next transcript.</h2>
            <p>Upload audio, review timestamped segments, and keep the history in this browser.</p>
          </div>
          <div class="cta-actions">
            <router-link class="button button-white" to="/transcribe">Start transcribing</router-link>
            <a href="https://github.com/nawalbsce3-dev/transcripto" target="_blank" rel="noreferrer">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.87c-2.78.6-3.37-1.18-3.37-1.18-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.61.07-.61 1.01.07 1.54 1.04 1.54 1.04.9 1.53 2.35 1.09 2.92.83.09-.65.35-1.09.64-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.64 0 0 .84-.27 2.75 1.02A9.58 9.58 0 0 1 12 6.85c.85 0 1.71.11 2.51.34 1.91-1.29 2.75-1.02 2.75-1.02.55 1.37.2 2.39.1 2.64.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.86V21c0 .27.18.58.69.48A10 10 0 0 0 12 2Z" /></svg>
              Star on GitHub
            </a>
          </div>
        </div>
      </section>

      <section id="faq" class="section container faq-section" aria-labelledby="faq-title">
        <div class="section-heading reveal">
          <p class="section-kicker">FAQ</p>
          <h2 id="faq-title">Implementation details</h2>
        </div>
        <div class="faq-list reveal">
          <details>
            <summary>Where is uploaded audio stored?</summary>
            <p>The Flask server writes the upload to a temporary file for the duration of transcription. The file is deleted in a <code>finally</code> block after Whisper returns.</p>
          </details>
          <details>
            <summary>Where does transcription history live?</summary>
            <p>The frontend stores up to 20 completed transcripts in browser <code>localStorage</code>. It does not write transcript history to a database or external history service.</p>
          </details>
          <details>
            <summary>What is the maximum file size?</summary>
            <p>The interface validates files at 25 MB. Supported formats are MP3, WAV, M4A, FLAC, OGG, AAC, WMA, and OPUS.</p>
          </details>
          <details>
            <summary>Which Whisper model is used?</summary>
            <p>The default runtime model is <code>base</code>. Deployment configuration uses <code>tiny</code>, and the backend supports tiny, base, small, medium, and large through <code>WHISPER_MODEL</code>.</p>
          </details>
          <details>
            <summary>Can it run without a GPU?</summary>
            <p>Yes. Transcription calls <code>model.transcribe(..., fp16=False)</code>, so it is designed to run on CPU. Processing time depends on audio length and available hardware.</p>
          </details>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container footer-main">
        <div class="footer-brand">
          <router-link class="wordmark" to="/" aria-label="Transcripto home">
            <img src="/Transcripto_Logo_Purple.png" alt="Transcripto" />
          </router-link>
          <p>Self-hosted audio transcription with OpenAI Whisper.</p>
        </div>
        <div class="footer-column">
          <h2>Product</h2>
          <router-link to="/transcribe">Transcribe</router-link>
          <router-link to="/analysis">Analysis</router-link>
          <router-link to="/features">Features</router-link>
        </div>
        <div class="footer-column">
          <h2>Resources</h2>
          <a href="https://github.com/nawalbsce3-dev/transcripto#readme" target="_blank" rel="noreferrer">Docs</a>
          <a href="https://github.com/nawalbsce3-dev/transcripto" target="_blank" rel="noreferrer">GitHub</a>
          <a href="https://github.com/nawalbsce3-dev/transcripto/issues" target="_blank" rel="noreferrer">Issues</a>
        </div>
        <div class="footer-column">
          <h2>Company</h2>
          <router-link to="/about">About</router-link>
          <a href="mailto:hello@transcripto.app">Contact</a>
        </div>
        <div class="footer-column">
          <h2>Legal</h2>
          <router-link to="/about">Privacy</router-link>
          <router-link to="/about">Terms</router-link>
        </div>
      </div>
      <div class="container footer-bottom">
        <p>© {{ new Date().getFullYear() }} Transcripto</p>
        <button class="theme-toggle" type="button" :aria-label="`Switch to ${manualTheme === 'dark' ? 'light' : 'dark'} theme`" @click="toggleTheme">
          <svg v-if="manualTheme === 'dark'" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4" /><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42" /></svg>
          <svg v-else viewBox="0 0 24 24" aria-hidden="true"><path d="M21 15.5A9 9 0 1 1 8.5 3 7 7 0 0 0 21 15.5Z" /></svg>
          <span>{{ manualTheme === 'dark' ? 'Dark' : 'Light' }}</span>
        </button>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

const formats = ['MP3', 'WAV', 'M4A', 'FLAC', 'OGG', 'AAC', 'WMA', 'OPUS']
const scrolled = ref(false)
const mobileNavOpen = ref(false)
const manualTheme = ref('')
let revealObserver

const waveHeight = (n) => 18 + Math.abs(Math.sin(n * 0.78) * 55) + (n % 5) * 3

const updateScrolled = () => {
  scrolled.value = window.scrollY > 40
}

const toggleTheme = () => {
  const next = manualTheme.value === 'dark' ? 'light' : 'dark'
  manualTheme.value = next
  localStorage.setItem('transcripto.theme', next)
}

onMounted(() => {
  updateScrolled()
  window.addEventListener('scroll', updateScrolled, { passive: true })

  const savedTheme = localStorage.getItem('transcripto.theme')
  if (savedTheme === 'light' || savedTheme === 'dark') {
    manualTheme.value = savedTheme
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    manualTheme.value = 'dark'
  } else {
    manualTheme.value = 'light'
  }

  if ('IntersectionObserver' in window) {
    revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible')
          revealObserver.unobserve(entry.target)
        }
      })
    }, { threshold: 0.15 })

    document.querySelectorAll('.reveal').forEach((element, index) => {
      element.style.transitionDelay = `${(index % 4) * 60}ms`
      revealObserver.observe(element)
    })
  } else {
    document.querySelectorAll('.reveal').forEach((element) => element.classList.add('is-visible'))
  }
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', updateScrolled)
  revealObserver?.disconnect()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap');

.landing {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f5f5f7;
  --border: #e5e5ea;
  --border-strong: #d4d4dc;
  --text: #0a0a0f;
  --text-muted: #5c5c6e;
  --text-subtle: #8a8a9a;
  --accent: #4f46e5;
  --accent-hover: #4338ca;
  --accent-soft: #eef2ff;
  --success: #059669;
  --warning: #d97706;
  --radius-sm: 6px;
  --radius: 10px;
  --radius-lg: 14px;
  --radius-xl: 20px;
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  min-height: 100vh;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  overflow-x: hidden;
}

.landing[data-theme='dark'],
.landing[data-theme='dark'] * {
  --bg: #08080b;
  --surface: #111114;
  --surface-2: #17171c;
  --border: #23232b;
  --border-strong: #2f2f3a;
  --text: #f4f4f6;
  --text-muted: #9d9daa;
  --text-subtle: #6e6e7c;
  --accent: #6366f1;
  --accent-hover: #818cf8;
  --accent-soft: #1e1b4b;
  --success: #059669;
  --warning: #d97706;
}

@media (prefers-color-scheme: dark) {
  .landing:not([data-theme='light']) {
    --bg: #08080b;
    --surface: #111114;
    --surface-2: #17171c;
    --border: #23232b;
    --border-strong: #2f2f3a;
    --text: #f4f4f6;
    --text-muted: #9d9daa;
    --text-subtle: #6e6e7c;
    --accent: #6366f1;
    --accent-hover: #818cf8;
    --accent-soft: #1e1b4b;
  }
}

* { box-sizing: border-box; }
a { color: inherit; text-decoration: none; }
button, summary, a { -webkit-tap-highlight-color: transparent; }
button, a, summary { transition: color 150ms cubic-bezier(.4,0,.2,1), background-color 150ms cubic-bezier(.4,0,.2,1), border-color 150ms cubic-bezier(.4,0,.2,1), transform 150ms cubic-bezier(.4,0,.2,1); }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.container { width: min(1184px, calc(100% - 48px)); margin-inline: auto; }

.skip-link {
  position: fixed;
  z-index: 100;
  left: 16px;
  top: 8px;
  transform: translateY(-80px);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 10px 14px;
}
.skip-link:focus { transform: translateY(0); }

.site-header {
  position: sticky;
  z-index: 50;
  top: 0;
  height: 60px;
  background: color-mix(in srgb, var(--surface) 70%, transparent);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid transparent;
}
.site-header.is-scrolled { border-bottom-color: var(--border); }
.header-inner {
  width: min(1184px, calc(100% - 48px));
  height: 60px;
  margin-inline: auto;
  display: grid;
  grid-template-columns: 220px 1fr auto;
  align-items: center;
}
.wordmark {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  min-height: 44px;
}
.wordmark img {
  display: block;
  width: auto;
  height: 28px;
  max-width: 180px;
}
.desktop-nav { display: flex; justify-content: center; gap: 28px; }
.desktop-nav a, .github-link {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  color: var(--text-muted);
  font-size: 14px;
  font-weight: 500;
}
.desktop-nav a:hover, .github-link:hover { color: var(--text); }
.header-actions { display: flex; align-items: center; gap: 8px; }
.menu-button { display: none; }
.mobile-nav { display: none; }

.button {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  border: 1px solid transparent;
  border-radius: var(--radius);
  padding: 0 17px;
  font-size: 14px;
  font-weight: 600;
}
.button svg, .text-link svg, .cta-actions svg { width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.button-primary { background: var(--accent); color: #fff; }
.button-primary:hover { background: var(--accent-hover); transform: translateY(-1px); }
.button-small { min-height: 36px; padding-inline: 14px; }
.button-secondary { background: var(--surface); border-color: var(--border); color: var(--text); }
.button-secondary:hover { border-color: var(--border-strong); transform: translateY(-1px); }

.hero {
  min-height: 640px;
  display: grid;
  grid-template-columns: 55% 45%;
  align-items: center;
  gap: 32px;
  padding-block: 88px 96px;
}
.hero-copy { max-width: 670px; }
.eyebrow, .section-kicker {
  margin: 0 0 20px;
  color: var(--accent);
  font-family: var(--font-mono);
  font-size: 12px;
  font-weight: 500;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.eyebrow {
  display: inline-flex;
  align-items: center;
  min-height: 30px;
  border-radius: 999px;
  background: var(--accent-soft);
  padding: 5px 10px;
  margin-bottom: 24px;
  text-transform: none;
  letter-spacing: .04em;
}
h1, h2, h3, p { margin-top: 0; }
h1 {
  max-width: 680px;
  margin-bottom: 24px;
  font-size: 56px;
  line-height: 1.04;
  letter-spacing: -.03em;
  font-weight: 600;
}
h1 span { color: var(--accent); }
.hero-subhead {
  max-width: 52ch;
  margin-bottom: 32px;
  color: var(--text-muted);
  font-size: 18px;
  line-height: 1.6;
  letter-spacing: -.01em;
}
.hero-actions { display: flex; gap: 12px; margin-bottom: 24px; }
.trust-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 0;
  color: var(--text-subtle);
  font-size: 13px;
  line-height: 1.5;
}
.trust-row b { font-weight: 400; }

.hero-product { min-width: 0; }
.product-window {
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  background: var(--surface);
  box-shadow: 0 1px 2px rgba(0,0,0,.04), 0 12px 32px -12px rgba(0,0,0,.12);
  overflow: hidden;
}
.window-bar {
  height: 52px;
  display: grid;
  grid-template-columns: 64px 1fr auto;
  align-items: center;
  border-bottom: 1px solid var(--border);
  padding: 0 16px;
  color: var(--text-muted);
  font-size: 12px;
}
.window-dots { display: flex; gap: 5px; }
.window-dots i { width: 7px; height: 7px; border: 1px solid var(--border-strong); border-radius: 50%; }
.window-status { display: flex; align-items: center; gap: 6px; }
.window-status i { width: 6px; height: 6px; border-radius: 50%; background: var(--success); }
.product-playback {
  height: 72px;
  display: grid;
  grid-template-columns: 36px 1fr auto;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid var(--border);
  padding: 12px 16px;
}
.product-playback button { width: 36px; height: 36px; border: 1px solid var(--border); border-radius: 50%; background: var(--surface); color: var(--text); }
.product-playback button svg { width: 18px; height: 18px; fill: currentColor; }
.waveform { height: 34px; display: flex; align-items: center; gap: 3px; overflow: hidden; }
.waveform i { width: 3px; max-height: 100%; flex: 0 0 3px; border-radius: 3px; background: var(--border-strong); }
.timecode { color: var(--text-muted); font: 500 11px var(--font-mono); font-variant-numeric: tabular-nums; }
.transcript-view { padding: 8px; }
.transcript-segment {
  min-height: 68px;
  display: grid;
  grid-template-columns: 48px 1fr;
  gap: 8px;
  align-items: start;
  border-left: 2px solid transparent;
  border-radius: 6px;
  padding: 12px 10px;
  color: var(--text-muted);
  font-size: 13px;
  line-height: 1.5;
}
.transcript-segment span { color: var(--text-subtle); font-family: var(--font-mono); font-size: 11px; font-variant-numeric: tabular-nums; }
.transcript-segment p { margin: 0; }
.transcript-segment.is-active { border-left-color: var(--accent); background: var(--accent-soft); color: var(--text); }
.transcript-segment.is-active span { color: var(--accent); }

.spec-strip { background: var(--surface-2); border-block: 1px solid var(--border); }
.spec-inner { min-height: 112px; display: flex; align-items: center; justify-content: center; gap: 24px; }
.spec-inner > span { color: var(--text-subtle); font-size: 13px; }
.spec-inner ul { display: flex; flex-wrap: wrap; gap: 8px; margin: 0; padding: 0; list-style: none; }
.spec-inner li { border: 1px solid var(--border); border-radius: 999px; background: var(--surface); padding: 8px 12px; color: var(--text-muted); font: 500 12px var(--font-mono); }

.section { padding-block: 128px; }
.section-heading { max-width: 660px; margin-bottom: 48px; }
.section-heading .section-kicker { margin-bottom: 12px; }
.section-heading h2, .security-copy h2, .analysis-copy h2 {
  margin: 0;
  font-size: 36px;
  line-height: 1.12;
  letter-spacing: -.03em;
}
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-flow: dense;
  gap: 16px;
}
.feature-card {
  min-height: 252px;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
  padding: 28px;
}
.feature-card:hover { border-color: var(--border-strong); }
.feature-card.feature-wide { grid-column: span 2; }
.feature-icon { width: 20px; height: 20px; margin-bottom: 24px; fill: none; stroke: var(--text-muted); stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.feature-card h3 { margin-bottom: 8px; font-size: 15px; line-height: 1.3; letter-spacing: -.01em; }
.feature-card p { max-width: 52ch; margin-bottom: 24px; color: var(--text-muted); font-size: 14px; line-height: 1.6; }
.mini-transcript { display: flex; gap: 8px; }
.mini-transcript button { height: 36px; border: 1px solid var(--border); border-radius: var(--radius-sm); background: var(--surface); color: var(--text-muted); font: 500 11px var(--font-mono); }
.mini-transcript button.is-active { border-left: 2px solid var(--accent); background: var(--accent-soft); color: var(--accent); }
.mono-chip { display: inline-flex; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 8px 10px; color: var(--text-muted); font: 500 12px var(--font-mono); font-variant-numeric: tabular-nums; }
.format-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; }
.format-grid span { border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 7px 4px; text-align: center; color: var(--text-muted); font: 500 10px var(--font-mono); }
.stat-row { display: grid; grid-template-columns: repeat(3, 1fr); border: 1px solid var(--border); border-radius: var(--radius); }
.stat-row div { display: flex; flex-direction: column; gap: 5px; border-right: 1px solid var(--border); padding: 12px; }
.stat-row div:last-child { border-right: 0; }
.stat-row span { color: var(--text-subtle); font: 500 10px var(--font-mono); text-transform: uppercase; }
.stat-row strong { font-size: 18px; font-variant-numeric: tabular-nums; }
.export-pills { display: flex; flex-wrap: wrap; gap: 8px; }
.export-pills button { min-height: 44px; border: 1px solid var(--border); border-radius: 999px; background: var(--surface); padding: 0 14px; color: var(--text-muted); font-size: 13px; }
.export-pills code { color: var(--text); font-family: var(--font-mono); }

.how-section { border-block: 1px solid var(--border); background: var(--surface); }
.steps {
  position: relative;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
  padding-top: 24px;
}
.steps::before { content:''; position:absolute; left:14px; right:14px; top:38px; height:1px; background:var(--border); }
.steps article { position: relative; z-index:1; }
.step-number { width:28px; height:28px; display:flex; align-items:center; justify-content:center; margin-bottom:20px; border:1px solid var(--border); border-radius:50%; background:var(--surface); color:var(--text-muted); font:500 11px var(--font-mono); }
.steps h3 { margin-bottom:8px; font-size:15px; }
.steps p { max-width:24ch; color:var(--text-muted); font-size:14px; line-height:1.6; }
.endpoint { position:absolute; right:0; bottom:-48px; border:1px solid var(--border); border-radius:6px; background:var(--surface-2); padding:7px 9px; color:var(--text-muted); font:500 11px var(--font-mono); }

.security-band { background: var(--surface-2); border-block: 1px solid var(--border); }
.security-grid { min-height: 420px; display:grid; grid-template-columns:1fr 1fr; align-items:center; gap:96px; }
.security-copy p:last-child, .analysis-copy p { color:var(--text-muted); font-size:16px; line-height:1.7; }
.checklist { margin:0; padding:0; list-style:none; }
.checklist li { display:grid; grid-template-columns:20px 1fr; gap:12px; align-items:start; min-height:64px; border-bottom:1px solid var(--border); padding:18px 0; color:var(--text); font-size:15px; line-height:1.5; }
.checklist li:last-child { border-bottom:0; }
.checklist svg { width:20px; height:20px; fill:none; stroke:var(--success); stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
.checklist code { font-family:var(--font-mono); }

.dashboard-preview { display:grid; grid-template-columns:40% 60%; align-items:center; gap:64px; }
.analysis-copy { max-width:430px; }
.analysis-copy h2 { margin-bottom:20px; }
.text-link { min-height:44px; display:inline-flex; align-items:center; gap:8px; color:var(--accent); font-size:14px; font-weight:600; }
.text-link:hover { color:var(--accent-hover); }
.analysis-card { border:1px solid var(--border); border-radius:var(--radius-lg); background:var(--surface); padding:20px; box-shadow:0 12px 32px -12px rgba(0,0,0,.10); }
.analysis-stat-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:8px; }
.analysis-stat-grid div { min-height:112px; display:flex; flex-direction:column; border:1px solid var(--border); border-radius:var(--radius); padding:14px; }
.analysis-stat-grid span { margin-bottom:8px; color:var(--text-subtle); font:500 11px var(--font-mono); text-transform:uppercase; }
.analysis-stat-grid strong { margin-bottom:auto; font-size:28px; line-height:1; font-variant-numeric:tabular-nums; }
.analysis-stat-grid small { color:var(--text-subtle); font-size:11px; }
.distribution { margin-top:12px; border:1px solid var(--border); border-radius:var(--radius); padding:14px 14px 10px; }
.distribution-head { display:flex; justify-content:space-between; margin-bottom:12px; color:var(--text-muted); font-size:12px; }
.distribution-head code { color:var(--text-subtle); font-family:var(--font-mono); }
.bar-chart { height:88px; display:flex; align-items:flex-end; gap:8px; border-bottom:1px solid var(--border); }
.bar-chart i { flex:1; border-radius:3px 3px 0 0; background:var(--accent); }

.cta-band { background:var(--accent); color:#fff; }
.cta-inner { min-height:272px; display:flex; align-items:center; justify-content:space-between; gap:48px; }
.cta-inner h2 { max-width:720px; margin-bottom:10px; font-size:32px; line-height:1.2; letter-spacing:-.02em; }
.cta-inner p { margin:0; color:rgba(255,255,255,.80); font-size:16px; }
.cta-actions { display:flex; flex-direction:column; align-items:center; gap:12px; }
.button-white { min-width:168px; background:#fff; color:var(--accent); }
.button-white:hover { background:#f7f7ff; transform:translateY(-1px); }
.cta-actions a:last-child { min-height:44px; display:inline-flex; align-items:center; gap:8px; color:rgba(255,255,255,.85); font-size:13px; }
.cta-actions a:last-child svg { fill:currentColor; }

.faq-section { border-bottom:1px solid var(--border); }
.faq-list { max-width:1184px; }
.faq-list details { border-top:1px solid var(--border); }
.faq-list details:last-child { border-bottom:1px solid var(--border); }
.faq-list summary { min-height:64px; display:flex; align-items:center; justify-content:space-between; cursor:pointer; list-style:none; font-size:15px; font-weight:500; }
.faq-list summary::-webkit-details-marker { display:none; }
.faq-list summary::after { content:'+'; color:var(--text-muted); font-size:20px; }
.faq-list details[open] summary::after { content:'−'; }
.faq-list details p { max-width:760px; margin:-4px 32px 20px 0; color:var(--text-muted); font-size:14.5px; line-height:1.7; }
.faq-list code { font-family:var(--font-mono); }

.site-footer { background:var(--bg); }
.footer-main { display:grid; grid-template-columns:2fr repeat(4,1fr); gap:32px; padding-block:64px 48px; }
.footer-brand p { max-width:280px; margin-top:12px; color:var(--text-subtle); font-size:13px; line-height:1.6; }
.footer-column { display:flex; flex-direction:column; gap:10px; }
.footer-column h2 { margin:0 0 4px; color:var(--text-subtle); font:500 11px var(--font-mono); text-transform:uppercase; }
.footer-column a { min-height:32px; display:inline-flex; align-items:center; color:var(--text-muted); font-size:13px; }
.footer-column a:hover { color:var(--text); }
.footer-bottom { min-height:72px; display:flex; align-items:center; justify-content:space-between; border-top:1px solid var(--border); }
.footer-bottom p { margin:0; color:var(--text-subtle); font-size:13px; }
.theme-toggle { min-height:44px; display:inline-flex; align-items:center; gap:8px; border:1px solid var(--border); border-radius:999px; background:var(--surface); padding:0 12px; color:var(--text-muted); font-size:12px; }
.theme-toggle svg { width:16px; height:16px; fill:none; stroke:currentColor; stroke-width:1.5; stroke-linecap:round; stroke-linejoin:round; }

.reveal { opacity:0; transform:translateY(8px); transition:opacity 400ms ease, transform 400ms ease; }
.reveal.is-visible { opacity:1; transform:translateY(0); }

@media (max-width:1024px) {
  .header-inner { grid-template-columns:180px 1fr auto; }
  .hero { grid-template-columns:1fr; padding-block:72px 96px; }
  .hero-copy { max-width:760px; }
  .hero-product { max-width:680px; width:100%; }
  .bento-grid { grid-template-columns:repeat(2,1fr); }
  .dashboard-preview { grid-template-columns:1fr; }
  .analysis-copy { max-width:620px; }
  .security-grid { gap:48px; }
  .footer-main { grid-template-columns:2fr repeat(2,1fr); }
}

@media (max-width:768px) {
  .container, .header-inner { width:min(100% - 40px, 1184px); }
  .wordmark img { height:24px; max-width:150px; }
  .header-inner { grid-template-columns:1fr auto; }
  .desktop-nav, .github-link { display:none; }
  .menu-button { width:44px; height:44px; display:inline-flex; align-items:center; justify-content:center; border:1px solid var(--border); border-radius:var(--radius); background:var(--surface); color:var(--text); }
  .menu-button svg { width:20px; height:20px; fill:none; stroke:currentColor; stroke-width:1.5; stroke-linecap:round; }
  .header-actions .button-small { display:none; }
  .mobile-nav { position:absolute; left:0; right:0; top:60px; display:flex; flex-direction:column; border-bottom:1px solid var(--border); background:var(--surface); padding:8px 20px 16px; }
  .mobile-nav a { min-height:44px; display:flex; align-items:center; border-bottom:1px solid var(--border); color:var(--text-muted); font-size:14px; }
  .mobile-nav a:last-child { border-bottom:0; color:var(--accent); }
  .hero { padding-block:64px 80px; }
  h1 { font-size:40px; }
  .hero-subhead { font-size:16px; }
  .section { padding-block:96px; }
  .section-heading h2, .security-copy h2, .analysis-copy h2 { font-size:32px; }
  .bento-grid { grid-template-columns:1fr; }
  .feature-card.feature-wide { grid-column:auto; }
  .spec-inner { min-height:96px; flex-direction:column; gap:12px; padding-block:20px; }
  .steps { grid-template-columns:1fr 1fr; row-gap:40px; }
  .steps::before { display:none; }
  .endpoint { bottom:-52px; }
  .security-grid { grid-template-columns:1fr; gap:32px; padding-block:80px; }
  .dashboard-preview { gap:40px; }
  .cta-inner { min-height:320px; flex-direction:column; align-items:flex-start; justify-content:center; }
  .cta-actions { align-items:flex-start; }
  .footer-main { grid-template-columns:repeat(2,1fr); }
  .footer-brand { grid-column:1/-1; }
}

@media (max-width:480px) {
  .container, .header-inner { width:calc(100% - 40px); }
  .wordmark img { height:22px; max-width:140px; }
  .hero { min-height:auto; padding-block:48px 64px; }
  h1 { font-size:32px; }
  .hero-actions { flex-direction:column; }
  .hero-actions .button { width:100%; }
  .trust-row { display:grid; gap:4px; }
  .trust-row b { display:none; }
  .product-window { border-radius:var(--radius-lg); }
  .window-bar { grid-template-columns:48px 1fr auto; }
  .window-status { display:none; }
  .product-playback { grid-template-columns:36px 1fr; }
  .timecode { display:none; }
  .transcript-segment { grid-template-columns:42px 1fr; }
  .section { padding-block:64px; }
  .section-heading { margin-bottom:32px; }
  .section-heading h2, .security-copy h2, .analysis-copy h2 { font-size:28px; }
  .format-grid { grid-template-columns:repeat(4,1fr); }
  .steps { grid-template-columns:1fr; gap:32px; }
  .endpoint { position:static; width:fit-content; margin-top:-4px; }
  .security-grid { padding-block:64px; }
  .checklist li { min-height:56px; }
  .analysis-stat-grid { gap:6px; }
  .analysis-stat-grid div { min-height:104px; padding:10px; }
  .analysis-stat-grid strong { font-size:24px; }
  .cta-inner { padding-block:64px; }
  .cta-inner h2 { font-size:28px; }
  .cta-actions, .button-white { width:100%; }
  .cta-actions a:last-child { justify-content:center; width:100%; }
  .faq-list summary { padding-right:8px; }
  .footer-main { grid-template-columns:1fr; gap:32px; }
  .footer-brand { grid-column:auto; }
  .footer-bottom { align-items:center; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { scroll-behavior:auto !important; transition-duration:0.01ms !important; }
  .reveal { opacity:1; transform:none; }
}
</style>
