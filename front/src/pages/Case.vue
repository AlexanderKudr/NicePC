!<template>
    <my-header/>
    <case-content/>
    <my-footer/>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import CaseContent from '@/components/Case/CaseContent.vue'
export default {
    components: {
    MyHeader,
    MyFooter,
    CaseContent
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