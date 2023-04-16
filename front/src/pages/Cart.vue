<template>
    <div>
        <MyHeader/>
        <CartContent/>
        <MyFooter/>
    </div>
</template>

<script>
import MyHeader from '@/components/MyHeader.vue';
import MyFooter from '@/components/MyFooter.vue';
import CartContent from '@/components/Cart/CartContent.vue';
    export default {
        components:{
            MyHeader,
            MyFooter,
            CartContent
        }
    }
</script>

<style>

</style>