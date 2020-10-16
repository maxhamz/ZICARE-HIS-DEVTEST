<template>
  <div class="pg-register">
    <Letterhead />
    <RegisterForm />
  </div>
</template>

<script>
import RegisterForm from '../components/RegisterForm.vue'
import Letterhead from '../components/Letterhead.vue'
export default {
  name: 'RegisterPage',
  props: [],
  components: {
    RegisterForm,
    Letterhead
  },
  data () {
    return {}
  },
  methods: {},
  created () {}
}
</script>
<style scoped>
</style>