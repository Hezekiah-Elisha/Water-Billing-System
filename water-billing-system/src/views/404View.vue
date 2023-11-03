<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <div class="not_found">
            <img src="../assets/undraw_page_not_found_re_e9o6.svg" class="img-fluid" alt="">
            <h1>Page Not Found</h1>
            <p>Please click bellow to head to a recognized page</p>
            <router-link to="/dashboard">Dashboard</router-link>
        </div>
    </div>
</div>
</template>

<script>

import SideNav from '@/components/SideNav.vue';

export default {
    name: 'NotFoundView',
    components: {
        SideNav
    }
}

</script>

<style scoped>

.not_found {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center; 
}

.not_found img {
    width: 400px;
    height: 400px;
}

</style>