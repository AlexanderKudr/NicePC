!<template>
    <my-header/>
    <motherboard-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import MotherboardContent from '@/components/Motherboard/MotherboardContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    MotherboardContent
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