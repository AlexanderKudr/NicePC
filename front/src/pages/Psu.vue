!<template>
    <my-header/>
    <psu-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import PsuContent from '@/components/PowerSupply/PsuContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    PsuContent
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