<template>
	<div class="user-table">
		<table>
			<tr>
				<th>NO</th>
				<th>NAMA</th>
				<th>JENIS KELAMIN</th>
				<th>NIK</th>
				<th>NO HP</th>
				<th>ALAMAT</th>
				<th>AGAMA</th>
				<th>PENDIDIKAN</th>
				<th>GOLONGAN DARAH</th>
				<th>OPTION</th>
			</tr>
			<tr v-for="item in items">
                <td>{{item.id}}</td>
                <td>{{item.name}}</td>
                <td>{{item.saab}}</td>
                <td>{{item.nik}}</td>
                <td>{{item.cell_no}}</td>
                <td>{{item.address}}</td>
                <td>{{item.religion}}</td>
                <td>{{item.education}}</td>
                <td>{{item.blood_type}}</td>
                <td>
                   <b-button-group>
                    <b-button variant="info" @click.prevent="showUserEditForm(item.id)">EDIT</b-button>
                    <b-button variant="danger" @click.prevent="dropUser(item.id)">HAPUS</b-button>
                  </b-button-group>
                </td>
            </tr>
		</table>
	</div>
</template>

<script>
export default {
  name: 'UserTable',
  components: {},
  props: ['items'],
  data () {
    return {}
  },
  methods: {
      dropUser (userId) {
        console.log('DELETE USER @ CARD')
        console.log(userId)
        this.$store
            .dispatch('deleteUser', userId)
            .then(response => {
                console.log('DELETE PRODUCT SUCCESS')
                console.log(response.data.message)
                this.$toasted.show(`${response.status} ${response.message}`)
                this.$store.dispatch('fetchProducts')
            })
            .catch(err => {
                console.log(err.response)
            //   const arr = err.response.data.errors
            //   const code = err.response.status
            //   const type = err.response.statusText
            //   const ct = code + ' ' + type
            //   arr.forEach(el => {
            //     this.$toasted.error(`${ct}: ${el}`)
            //   })
            })
      },
      showUserEditForm (userId) {
        console.log('SHOW EDIT USER FORM @ TABLE')
        console.log(userId)
        this.$router.push({ name: 'EditPage', params: { id: userId } })
      }
  },
    computed: {},
    created () {}
  }
</script>
<style scoped>
</style>