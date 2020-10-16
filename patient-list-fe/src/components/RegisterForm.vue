<template>
  <div id="form-register">
    <h3>Tambah Data Pasien</h3>
    <form id="add-user-form">
      Nama:
      <input type="text" required id="add-user-name" v-model="addParams.name" />
      <br />
      <br />
      Jenis Kelamin:
      <select id="add-item-saab" required v-model="addParams.saab">
        <option value="L">Laki-laki</option>
        <option value="P">Perempuan</option>
      </select>
      <br />
      <br />NIK:
      <input type="text" required id="add-user-nik" v-model="addParams.nik" />
      <br />
      <br />No HP:
      <input type="text" required id="add-user-cell-no" v-model="addParams.cell_no" />
      <br />
      <br />Alamat:
      <input type="text" required id="add-user-address" v-model="addParams.address" />
      <br />
      <br />Agama:
      <select id="add-item-religion" required v-model="addParams.religion">
        <option value="Islam">Islam</option>
        <option value="Protestan">Kristen Protestan</option>
        <option value="Katholik">Kristen Katholik Roma</option>
        <option value="Hindu">Hindu</option>
        <option value="Buddha">Buddha</option>
        <option value="Konghucu">Konghucu</option>
        <option value="Lainnya">Lainnya</option>
      </select>
      <br />
      <br />Golongan Darah:
      <select id="add-item-blood-type" required v-model="addParams.blood_type">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="AB">AB</option>
        <option value="O">O</option>
      </select>
      <br />
      <br />Pendidikan:
      <select id="add-item-education" required v-model="addParams.education">
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
      <b-button variant="primary" form="add-user-form" @click.prevent="addUser">DAFTARKAN</b-button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'RegisterForm',
  components: {
  },
  props: [],
  data () {
    return {
      user: {},
      addParams: {
        name: '',
        saab: '',
        nik: '',
        cell_no: '',
        address: '',
        religion: '',
        education: '',
        blood_type: ''
      }
    }
  },
  methods: {
    addUser () {
      console.log('ADD NEW PATIENT @ FORMPAGE')
      console.log(this.addParams)
      this.$store
        .dispatch('register', this.addParams)
        .then(response => {
          console.log('PATIENT ADDED')
          console.log(response.data.result)
          this.user = response.data.result
          this.$toasted.success(`${response.data.status} : ${response.data.message}`)
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
  created () {
    // socket.on('added_product', (payload) => {
    //   this.$toasted.success(payload.name + ' ADDED TO INVENTORY', {
    //     position: 'bottom-center'
    //   })
    //   this.$store.dispatch('fetchProducts')
    //   console.log(payload.name + ' ADDED TO INVENTORY')
    // })
  }
}
</script>

<style scoped>
#add-item-form {
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