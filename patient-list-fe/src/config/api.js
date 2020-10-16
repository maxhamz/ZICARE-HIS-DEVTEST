import axios from 'axios'
const BASEURL = 'http://localhost:5000'

const instance = axios.create({
  baseURL: BASEURL
})

export default instance