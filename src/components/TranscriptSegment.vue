<template>
  <button
    class="transcript-row"
    :class="{ active }"
    type="button"
    :disabled="!seekable"
    :aria-current="active ? 'true' : undefined"
    :aria-label="seekable ? `${speakerLabel}, ${time}: ${text}. Play from this point` : `${speakerLabel}, ${time}: ${text}. Audio is not saved with browser history`"
    @click="$emit('seek')"
  >
    <span class="segment-header">
      <span class="speaker-line">
        <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3.2" /><path d="M5.5 20a6.5 6.5 0 0 1 13 0" /></svg>
        {{ speakerLabel }}
      </span>
      <span class="seg-meta">{{ time }}</span>
    </span>
    <span class="seg-text">{{ text }}</span>
  </button>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'TranscriptSegment',
  setup(props) {
    const speakerLabel = computed(() => {
      const speakerNumber = props.speaker.match(/^SPK_(\d+)$/i)?.[1]
      return speakerNumber ? `Speaker ${speakerNumber}` : props.speaker
    })

    return { speakerLabel }
  },
  props: {
    speaker: {
      type: String,
      required: true
    },
    time: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    },
    active: {
      type: Boolean,
      default: false
    },
    seekable: {
      type: Boolean,
      default: true
    }
  },
  emits: ['seek']
}
</script>
