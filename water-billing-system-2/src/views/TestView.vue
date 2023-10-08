<template>
    <h1> API Version: </h1>
         <p><i class="bi bi-file-diff"></i> {{ message }}</p>

</template>

<script>

import axios from 'axios'

export default {
    name: 'TestView',
    data() {
        return {
            message: ''
        }
    },
    methods: {
        async getVersion() {
            const response = await axios.get('http://localhost:7000/version')
            this.message = response.data['version']
        }
    },
    mounted() {
        this.getVersion()
    }
}

</script>

<style scoped>


</style>