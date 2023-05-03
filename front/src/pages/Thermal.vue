!<template>
    <my-header/>
    <thermal-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import ThermalContent from '@/components/ThermalPaste/ThermalContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    ThermalContent
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