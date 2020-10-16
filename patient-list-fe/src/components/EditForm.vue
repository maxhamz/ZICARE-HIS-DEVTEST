<template>
  <div id="form-edit">
    <h3>Tambah Data Pasien</h3>
    <form id="edit-user-form">
      Nama:
      <input type="text" required id="edit-user-name" v-model="details.name" />
      <br />
      <br />
      Jenis Kelamin:
      <select id="edit-user-saab" required v-model="details.saab">
        <option value="L">Laki-laki</option>
        <option value="P">Perempuan</option>
      </select>
      <br />
      <br />NIK:
      <input type="text" required id="edit-user-nik" v-model="details.nik" />
      <br />
      <br />No HP:
      <input type="text" required id="edit-user-cell-no" v-model="details.cell_no" />
      <br />
      <br />Alamat:
      <input type="text" required id="edit-user-address" v-model="details.address" />
      <br />
      <br />Agama:
      <select id="edit-user-religion" required v-model="details.religion">
        <option value="Islam">Islam</option>
        <option value="Protestan">Kristen Protestan</option>
        <option value="Katholik">Kristen Katholik Roma</option>
        <option value="Hindu">Hindu</option>
        <option value="Buddha">Buddha</option>
        <option value="Konghucu">Konghucu</option>
        <option value="Lainnya">Lainnya</option>
      </select>
      <br />
      <br />Pendidikan:
      <select id="edit-user-blood-type" required v-model="details.blood_type">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="AB">AB</option>
        <option value="O">O</option>
      </select>
      <br />
      <br />Pendidikan:
      <select id="edit-user-education" required v-model="details.education">
        <option value="SDTT">Tidak Tamat SD / Tidak Sekolah</option>
        <option value="SD">SD</option>
        <option value="SMP">SMP</option>
        <option value="SMA">SMA/SMK/STM</option>
        <option value="D1">Diploma-I</option>
        <option value="D2">Diploma-II</option>
        <option value="D3">Diploma-III</option>
        <option value="S1">Sarjana</option>
        <option value="S2">Magister</option>
        <option value="S3">Doktoral/PhD</option>
        <option value="S4">Pasca-Doktoral</option>
      </select>
      <br><br>
      <b-button variant="primary" form="edit-user-form" @click.prevent="editUser">UBAH DATA</b-button>
    </form>
  </div>
</template>


<script>
export default {
  name: 'EditForm',
  components: {
  },
  props: ['details'],
  data () {
    return {
    }
  },
  methods: {
    editUser () {
      console.log('EDIT PATIENT DATA @ STORE')
      console.log(this.details)
      this.$store.dispatch('editUser', this.details)
        .then(response => {
          console.log('PRODUCT EDITED')
          console.log(response.data)
          this.product = response.data
          this.$store.dispatch('fetchUsers')
          this.$router.push({ path: '/' })
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
    }
  },
  computed: {
    details () {
      console.log('MAKING SURE EDIT PARAMS')
      console.log(this.$store.state.user)
      return this.$store.state.user
    },
    isLoading () {
      return this.$store.state.isLoading
    }
  },
  created () {
    const id = this.$route.params.userid
    console.log('HELLO PATIENT #?')
    console.log(id)
    this.$store.dispatch('showUserEditForm', id)
    // this.$store.dispatch('fetchUser')
  }
}
</script>

<style scoped>
#edit-item-form {
  padding: 2vh;
  margin-top: 2vh;
  margin-bottom: 2vh;
  margin-left: 25%;
  justify-content: center;
  align-content: center;
  align-items: center;
  justify-items: center;
  border: 1px solid black;
  width: 50%;
}
</style>