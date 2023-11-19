<template>
    <div v-if="token != null">
        <nav>
            <div class="side-head">
                <h4 class="company">Water Billing System</h4>
            </div>
            <router-link to="/"> <i class="bi bi-house-door-fill"></i> Home</router-link>
            <div v-if="user.role == 'supervisor'">
                <router-link to="/supervisors"> <i class="bi bi-award-fill"></i> Supervisors</router-link>
                <router-link to="/users"> <i class="bi bi-people-fill"></i> Users</router-link>
                <router-link to="/workers"> <i class="bi bi-person-workspace"></i> Workers</router-link>
                <router-link to="/bills"> <i class="bi bi-cash-coin"></i> Bills</router-link>
                <router-link to="/meters"> <i class="bi bi-arrow-up-right-square-fill"></i> Meter</router-link>
                <router-link to="/meter-readings"> <i class="bi bi-speedometer2"></i> Meter Readings</router-link>
                <router-link to="/customers"> <i class="bi bi-cash-stack"></i> Customers</router-link>
            </div>

            <router-link to="/notifications"> <i class="bi bi-bell-fill"></i> Notifications</router-link>
        </nav>
    </div>
</template>

<script>




export default {
    name: 'SideNav',
    data() {
        return {
            token: localStorage.getItem('token'),
            username: "name",
            user: JSON.parse(localStorage.getItem('user')),
        };
    },
}


</script>

<style scoped>

.side-head{
    background-image: linear-gradient(to right, var(--primary-color), var(--secondary-color));
    padding: 10px;
    margin: 0;
    text-align: center;

}

.company, h4{
    color: white;
}

nav{
    height: calc(100vh);
    /* position: fixed; */
    background-color: var(--primary-color);
    display: flex;
    flex-direction: column;
    padding: 0;
}
nav div{
    background-color: var(--primary-color);
    display: flex;
    flex-direction: column;
    padding: 0;
}
nav a{
    color: var(--secondary-color);
    text-decoration: none;
    padding: 10px;
    font-weight: bold;
    text-align: left;
}

nav a:hover{
    /* color: var(--primary-color); */
    color: white;
    background-image: linear-gradient(to right, var(--primary-color), var(--secondary-color));
    /* background-color: white; */
    border-radius: 100px 0px 0px 100px;
    transition: 0.8s;
    translate: 10px;
}

nav a.router-link-exact-active {
  color: var(--primary-color);
  background-color: white;
  border-radius: 100px 0px 0px 100px;
  transition: 0.8s;
}
</style>