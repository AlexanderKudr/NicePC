<template>
    <my-header/>
    <profile-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import ProfileContent from '@/components/Profile/ProfileContent.vue'

export default {
    components: {
    MyHeader,
    MyFooter,
    ProfileContent
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