!<template>
    <my-header/>
    <prebuilt-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import PrebuiltContent from '@/components/HddSsd/HddSsdContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    PrebuiltContent
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