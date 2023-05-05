<template>
    <my-header />
    <index-content />
    <my-footer />
</template>

<script>
import MyHeader from '@/components/MyHeader.vue'
import MyFooter from '@/components/MyFooter.vue'
import IndexContent from '@/components/Index/IndexContent.vue'

export default {
    components: {
        MyHeader,
        MyFooter,
        IndexContent
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