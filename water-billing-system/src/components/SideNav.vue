<template>
    <div v-if="token != null">
        <nav>
            <h2 class="company">Water Billing System</h2>
            <h4>Welcome {{ username }} </h4>
            <router-link to="/"> <i class="bi bi-house-door-fill"></i> Home</router-link>
            <router-link to="/supervisors"> <i class="bi bi-award-fill"></i> Supervisors</router-link>
            <router-link to="/users"> <i class="bi bi-people-fill"></i> Users</router-link>
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
        };
    },
}


</script>

<style scoped>
.company, h4{
    color: white;
}

nav{
    height: 100vh;
    /* position: fixed; */
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
    color: var(--primary-color);
    background-color: white;
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