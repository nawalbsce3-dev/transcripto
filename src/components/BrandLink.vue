<template>
  <router-link :to="to" class="brand" :aria-label="label">
    <img class="brand-logo" src="/Transcripto_Logo_Purple.png" alt="Transcripto" />
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
