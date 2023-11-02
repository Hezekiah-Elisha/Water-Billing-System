<template>
    <!-- <hr> -->
    <div class="d-flex justify-content-between top-head">
        <h2><i class="bi bi-bell-fill"></i>Notifications</h2>
        <button class="btn info" @click="notificationModal = true" > <i class="bi bi-pencil-fill"></i>Register meter</button>
    </div>
    
    <!-- <hr> -->
    <WorkerComponent v-if="notificationModal" @close="notificationModal = false">
        <h2>Send Notification</h2>
        <form @submit.prevent="submit" class="form">
            <input v-model="message" type="text" placeholder="Message">
            <select v-model="user_id" id="">
                <option value="">Select Receiver</option>
                <option v-for="user in allUsers" :key="user.id" value="{{user.id}}">{{ user.username }}</option>
            </select>
            <select v-model="type" id="">
                <option value="">Select Type</option>
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
            </select>
            <button class="btn btn-info">Send</button>
        </form>
    </WorkerComponent>

    <h3>Send Notification</h3>


    <div class="row">
        <div class="col-md-4" v-for="notification in notifications" :key="notification.id">
            <div class="card">
                <div class="card-header">{{ notification.message }}</div>
                <div class="card-body">
                    <p><b>Time: </b>{{ notification.date }}</p>
                    <p><b>Type: </b>{{ notification.type }}</p>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
    import WorkerComponent from '@/components/WorkerComponent.vue';
    import axios from 'axios';

    axios.defaults.baseURL = 'http://localhost:7000';

    // let username = "";

    export default {
        name: 'NotificationsView',
        components: {
            WorkerComponent
        },
        data() {
            return {
                notifications: [],
                allUsers: [],
                message: '',
                type: '',
                user_id: '',
                notificationModal: false,
            }
        },
        methods: {
            getNotifications() {
                axios.get('notifications')
                    .then(response => {
                        this.notifications = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    })
            },
            getAllUsers() {
                axios.get('auth/users')
                    .then(response => {
                        this.allUsers = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    })
            },
            submit() {
                const now = new Date();
                const year = now.getFullYear();
                const month = String(now.getMonth() + 1).padStart(2, "0");
                const day = String(now.getDate()).padStart(2, "0");
                const hours = String(now.getHours()).padStart(2, "0");
                const minutes = String(now.getMinutes()).padStart(2, "0");
                const seconds = String(now.getSeconds()).padStart(2, "0");

                // Format the date and time as "%Y-%m-%d %H:%M:%S"
                const date =`${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;

                axios.post('notifications', {
                    message: this.message,
                    type: this.type,
                    user_id: this.user_id,
                    date: date,
                    viewed: false
                })
                    .then(response => {
                        console.log(response.data);
                        this.getNotifications();
                        this.notificationModal = false;
                    })
                    .catch(error => {
                        console.log(error);
                    })
            }
        },
        mounted() {
            this.getNotifications();
            this.getAllUsers();
        }
    }

</script>

<style scoped>
.info{
    background-color: var(--primary-color);
    color: white;
    border-radius: 10px;
    padding: 10px;
    /* margin: 10px; */

}

    .form {
        display: flex;
        flex-direction: column;
        width: 50%;
        text-align: center;
    }

    .form input {
        margin-bottom: 10px;
    }

    .form select {
        margin-bottom: 10px;
    }

    .form button {
        margin-bottom: 10px;
    }

    .form option{
        text-transform: capitalize;
    }

    .card {
        margin-bottom: 10px;
    }

    .card-header {
        background-color: var(--primary-color);
        color: var(--neutral-color);
    }

    .card-body {
        background-color: var(--tertiary-color);
    }

    .card-body p {
        margin-bottom: 0;
    }

    .card-body p b {
        color: var(--primary-color);
    }

    .card-body p b:first-child {
        margin-right: 10px;
    }

</style>