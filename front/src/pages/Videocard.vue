!<template>
    <my-header/>
    <videocard-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import VideocardContent from '@/components/Videocard/VideocardContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    VideocardContent
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