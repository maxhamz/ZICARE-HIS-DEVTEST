import Vue from "vue";
import Vuex from "vuex";
import axios from "../config/api";
var formData = require("form-data");
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    users: [],
    user: {},
    isLogin: false,
    isLoading: false
  },
  mutations: {
    SET_USERS(state, payload) {
      state.users = payload;
    },
    SET_USER(state, payload) {
      state.user = payload;
    },
    SET_LOADING(state, payload) {
      state.isLoading = payload;
    }
  },
  getters: {
    getUser: state => {
      return state.user;
    }
  },
  actions: {
    register(context, payload) {
      console.log("REGISTER @ STORE");
      console.log(payload);
      var regisForm = new formData();

      // APPENDING ALL PARAMS
      regisForm.append("name", payload.name);
      regisForm.append("saab", payload.saab);
      regisForm.append("nik", payload.nik);
      regisForm.append("cell_no", payload.cell_no);
      regisForm.append("address", payload.address);
      regisForm.append("religion", payload.religion);
      regisForm.append("education", payload.education);
      regisForm.append("blood_type", payload.blood_type);

      axios({
        method: "POST",
        url: "/users/register",
        data: regisForm,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
        .then(response => {
          console.log("REGISTER SUCCESS");
          console.log(response.data);
          //   socket.emit('registered', response.data)
          //   socket.on('registered2', (payload) => {
          //     Vue.toasted.success(`Welcome, ${payload.email}. You may login now.`)
          //   })
        })
        .catch(err => {
          console.log(err.response);
          //   const arr = err.response.data.errors
          //   const code = err.response.status
          //   const type = err.response.statusText
          //   const ct = code + ' ' + type
          //   arr.forEach(el => {
          //     Vue.toasted.error(`${ct}: ${el}`)
          //   })
        });
    },

    fetchUsers(context) {
      console.log("FETCH Users @ STORE");
      context.commit("SET_LOADING", true);
      axios({
        method: "get",
        url: "/users/getall"
      })
        .then(response => {
          console.log("SUCCESS FETCHING PRODUCTS");
          console.log(response);
          context.commit("SET_USERS", response.data.result);
          //   socket.emit('getProducts', response.data.data)
          //   socket.on('getProducts2', (payload) => {
          //     context.commit('SET_PRODUCTS', payload)
          //     // Vue.toasted.success('FETCHED ALL PRODUCTS')
          //   })
        })
        .catch(err => {
          console.log(err.response);
          //   const arr = err.response.data.errors
          //   const code = err.response.status
          //   const type = err.response.statusText
          //   const ct = code + ' ' + type
          //   arr.forEach(el => {
          //     Vue.toasted.error(`${ct}: ${el}`)
          //   })
        });
      // .finally(_ => {
      //   context.commit('SET_LOADING', false)
      // })
    },

    getOneUser(context, payload) {
      console.log("FETCH ONE USER @ STORE");
      context.commit("SET_LOADING", true);
      axios({
        method: "get",
        url: "/users/getById/" + payload
      })
        .then(response => {
          console.log("SUCCESS FETCHING ONE USER");
          console.log(response.data.result);
          context.commit("SET_USER", response.data.result);
        })
        .catch(err => {
          console.log(err.response);
          //   const arr = err.response.data.errors
          //   const code = err.response.status
          //   const type = err.response.statusText
          //   const ct = code + ' ' + type
          //   arr.forEach(el => {
          //     Vue.toasted.error(`${ct}: ${el}`)
          //   })
        });
      // .finally(_ => {
      //   context.commit('SET_LOADING', false)
      // })
    },

    showUserEditForm(context, payload) {
      console.log("FETCH EDIT FORM @ STORE");
      context.dispatch("getOneUser", payload);
    },

    editUser(context, payload) {
      console.log("EDIT USER @ STORE");

      var editForm = new formData();

      // APPENDING ALL PARAMS
      editForm.append("name", payload.name);
      editForm.append("saab", payload.saab);
      editForm.append("nik", payload.nik);
      editForm.append("cell_no", payload.cell_no);
      editForm.append("address", payload.address);
      editForm.append("religion", payload.religion);
      editForm.append("education", payload.education);
      editForm.append("blood_type", payload.blood_type);

      return axios({
        method: "put",
        url: "/users/editUser/" + payload.id,
        data: editForm,
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
    },

    deleteUser(context, payload) {
      console.log("DELETE USER @ STORE");
      console.log(payload);
      return axios({
        method: "DELETE",
        url: "/users/deleteUser/" + payload
      });
    }
  },
  modules: {}
});
