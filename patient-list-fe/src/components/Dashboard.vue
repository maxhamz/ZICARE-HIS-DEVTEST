<template>
  <div class="dashboard">
    <UserTable :items="users"/>
  </div>
</template>

<script>
import UserTable from './UserTable'
export default {
  name: 'Dashboard',
  components: {
    UserTable
  },
  props: [],
  data () {
    return {}
  },
  methods: {},
  computed: {
    users () {
      return this.$store.state.users
    },
    isLoading () {
      return this.$store.state.isLoading
    }
  },
  created () {
    this.$store.dispatch('fetchUsers')
  }
}
</script>

<style scoped>
</style>