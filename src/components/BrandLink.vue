<template>
  <router-link :to="to" class="brand" :aria-label="label">
    <span class="brand-mark" aria-hidden="true"><span></span></span>
    <span>Transcripto</span>
  </router-link>
</template>

<script>
export default {
  name: 'BrandLink',
  props: {
    to: {
      type: String,
      default: '/'
    },
    label: {
      type: String,
      default: 'Transcripto home'
    }
  }
}
</script>
