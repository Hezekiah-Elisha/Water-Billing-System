<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
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
    </div>
</div>

</template>
<script>
import axios from 'axios'
import SideNav from '@/components/SideNav.vue';

export default {
    name: 'OneWorkerView',
    components: {
        SideNav
    },
    data() {
        return {
            worker: {},
            isThere: false
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
        },
        checkWorker(){
            axios
                .get('workers/'+this.$route.params.id)
                .then(response => {
                    if (response.data["message"] == "Worker does not exist"){
                        this.isThere = false
                        console.log(this.isThere);
                    }
                    else{
                        this.isThere = true
                        console.log(this.isThere);
                    }
                // this.worker = response.data[];
                console.log(response.data)
                })
                .catch(error => {
                    console.log(error);
                console.log(`Heeh ${error}`);
                });
        }
    },
    mounted() {
        this.loadWorker()
        this.checkWorker()
    }
}


</script>