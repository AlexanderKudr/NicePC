!<template>
    <my-header/>
    <case-cooler-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import CaseCoolerContent from '@/components/CoolerForCase/CaseCoolerContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    CaseCoolerContent
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