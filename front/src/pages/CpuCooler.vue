!<template>
    <my-header/>
    <cpu-cooler-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import CpuCoolerContent from '@/components/CoolerForCpu/CpuCoolerContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    CpuCoolerContent
},
    data() {
        return {
            
        }
    },
    methods: {
        
    }
}
</script>

<style>

</style>