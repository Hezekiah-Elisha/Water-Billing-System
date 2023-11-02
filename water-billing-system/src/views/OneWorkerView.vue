<template>
        Worker {{ $route.params.id }}
        <div class="row">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-header">Worker Details</div>
                    <div class="card-body">
                        <p>Worker ID: {{ worker.username }}</p>
                        <p>Worker Name: {{ worker.name }}</p>
                        <p>Worker Email: {{ worker.email }}</p>
                        <p>Worker Phone: {{ worker.phone }}</p>
                        <p>Worker Location: {{ worker.location }}</p>
                        <p>Worker Role: {{ worker.role }}</p>
                        <p>Worker Status: {{ worker.status }}</p>
                        <p>Worker Created At: {{ worker.created_at }}</p>
                        <p>Worker Updated At: {{ worker.updated_at }}</p>
                    </div>
                </div>
            </div>
        </div>

</template>
<script>
import axios from 'axios'

export default {
    name: 'OneWorkerView',
    data() {
        return {
            worker: {}
        }
    },
    methods: {
        loadWorker() {
            axios
                .get('http://localhost:7000/auth/users/'+this.$route.params.id)
                .then(response => {
                this.worker = response.data;
                console.log(response.data)
                })
                .catch(error => {
                console.log(error);
                });
        }
    },
    mounted() {
        this.loadWorker()
    }
}


</script>