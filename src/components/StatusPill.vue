<template>
  <div class="status-chip" :class="stateClass" role="status" aria-live="polite">
    <span class="dot" aria-hidden="true"></span>
    {{ label }}
  </div>
</template>

<script>
export default {
  name: 'StatusPill',
  props: {
    label: {
      type: String,
      required: true
    },
    stateClass: {
      type: String,
      default: 'status-idle'
    }
  }
}
</script>
