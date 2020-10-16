<template>
  <div class="pg-edit">
    <Letterhead />
    <EditForm :details="user2Edit"/>
  </div>
</template>

<script>
import EditForm from '../components/EditForm.vue'
import Letterhead from '../components/Letterhead.vue'
export default {
  name: 'EditPage',
  props: [],
  components: {
    EditForm,
    Letterhead
  },
  data () {
    return {}
  },
  methods: {},
  computed: {
    user2Edit () {
      console.log('MAKING SURE EDIT PARAMS')
      console.log(this.$store.state.user)
      return this.$store.state.user
    }
  },
  created () {
    const id = this.$route.params.id
    console.log('HELLO PATIENT #?')
    console.log(id)
    this.$store.dispatch('showUserEditForm', id)
    // this.$store.dispatch('fetchUser')
  }
}
</script>
<style scoped>
</style>