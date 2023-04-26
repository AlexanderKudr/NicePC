<template>
    <div>
        <cart-item :cart_item="cart_item" v-for="cart_item in cart_items"/>
    </div>
</template>

<script>
    import axios from "axios"
    import CartItem from "@/components/Cart/CartItem.vue"
    export default {
        data() {
            return {
                cart_items: []
            }
        },
        components:{
            CartItem
        },
        methods: {
            async fetchCart() {
                await axios.get('http://127.0.0.1:8000/cart/', {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then((res) => {
                this.cart_items = res.data
            })
            }
        },
        beforeMount() {
            this.fetchCart()
        }
    }
</script>

<style>

</style>