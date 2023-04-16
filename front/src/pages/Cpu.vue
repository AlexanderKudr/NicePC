!<template>
    <my-header/>
    <cpu-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import CpuContent from '@/components/Cpu/CpuContent.vue';
export default {
    components: {
    MyHeader,
    MyFooter,
    CpuContent
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