<template>
    <InfoComponent info="Hey"/>
    <h1> API Version: </h1>
         <p><i class="bi bi-file-diff"></i> {{ message }}</p>

</template>

<script>

import axios from 'axios'
import InfoComponent from '@/components/common/InfoComponent.vue'

export default {
    name: 'TestView',
    components: {
        InfoComponent
    },
    data() {
        return {
            message: ''
        }
    },
    methods: {
        async getVersion() {
            const response = await axios.get('version')
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