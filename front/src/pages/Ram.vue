!<template>
    <my-header/>
    <ram-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import RamContent from '@/components/RAM/RamContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    RamContent
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