<template>
<div class="row">
    <div class="col-md-2">
        <SideNav/>
    </div>
    <div class="col-md-10">
        <h2>Meter Reading Package</h2>
        <hr>
    </div>
</div>


</template>

<script>

import SideNav from '@/components/SideNav.vue';

export default {
    name: 'MeterReadingsView',
    components: {
        SideNav
    }
}

</script>