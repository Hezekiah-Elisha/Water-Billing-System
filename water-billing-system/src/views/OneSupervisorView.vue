<template>
    <!-- Supervisor {{ $route.params.id }} -->
    <h2>Supervisor <span>{{ user.username }}</span></h2>
    <hr>
    <p>Email: {{ user.email }}</p>

    <div v-if="isThere">
        <p>Phone: {{ extraInfo.phone }}</p>
        <p>Location: {{ extraInfo.location }}</p>
    </div>

    <div v-else>
        <h3>Complete Supervisor Registration</h3>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name : 'OneSupervisorView',
    data() {
        return {
            user : {},
            extraInfo : {},
            isThere: false,
        }
    },
    methods: {
        loadUser() {
            axios
                .get('http://localhost:7000/auth/users/'+this.$route.params.id)
                .then(response => {
                this.user = response.data;
                console.log(response.data)
                })
                .catch(error => {
                console.log(error);
                });
        },
        submit() {
            axios.post('http://localhost:7000/supervisors', {
                user_id: this.user.id,
                phone: this.extraInfo.phone,
                location: this.extraInfo.location
            })
            .then(response=>{
                console.log(response.data)
                if (response.status === 200) {
                    this.success = 'Supervisor created successfully!'
                }
                else if (response.status === 409) {
                    console.log('Note: Email or Password is incorrect')
                    this.error = 'Supervisor already exists'
                }
            })
            .catch(error=>{
                this.error = 'Error creating supervisor'+error
            })
        },
        checkSupervisor() {
            axios.get('http://localhost:7000/supervisors/'+this.$route.params.id)
                .then(response => {
                    console.log(response.data)
                    if (response.data['message'] === 'Supervisor does not exist') {
                        this.isThere = false
                    }
                    else {
                        this.isThere = true
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }

    },
    created() {
        this.loadUser()
        this.checkSupervisor()
    }
}


</script>

<style scoped>
h2, span{
    text-transform: capitalize;
}
</style>