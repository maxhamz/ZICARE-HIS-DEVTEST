<template>
	<div id="pg-home">
		<Letterhead/>
		<h1>DAFTAR PASIEN</h1>
        <Dashboard />
		<div id="bottom-bar">
			<router-link to="/register">
				<b-button variant="success">TAMBAH</b-button>
			</router-link>
		</div>
	</div>
</template>

<script>
import Letterhead from "../components/Letterhead";
import Dashboard from "../components/Dashboard"
export default {
	name: "Home",
	props: [],
	components: {
		Letterhead, Dashboard
	},
	data() {
		return {};
	},
	methods: {},
	created() {
        this.$store.dispatch('fetchUsers')
    },
};
</script>

<style>
</style>