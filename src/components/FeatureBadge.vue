<template>
  <span class="badge">
    <slot name="icon"></slot>
    <slot></slot>
  </span>
</template>

<script>
export default {
  name: 'FeatureBadge'
}
</script>
