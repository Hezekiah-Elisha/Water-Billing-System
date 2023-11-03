<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h1>Bills Page</h1>
        <hr>
    </div>
</div>
</template>

<script>

import SideNav from '@/components/SideNav.vue';

export default {
    name: 'BillsView',
    components: {
        SideNav
    }
}

</script>