<script>
import { nextTick, ref, watch } from 'vue'

export default {
  name: 'AppHeader',
  props: {
    pageTitle: { type: String, default: 'Transcripto' },
    currentTitle: { type: String, default: '' },
    search: { type: String, default: '' },
    menuOpen: { type: Boolean, default: false }
  },
  emits: ['open-menu', 'update:search'],
  setup(props) {
    const menuButton = ref(null)
    watch(() => props.menuOpen, async (open, wasOpen) => {
      if (!open && wasOpen) {
        await nextTick()
        menuButton.value?.focus()
      }
    })
    return { menuButton }
  }
}
</script>
