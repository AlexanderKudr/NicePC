<template>
    <div>
        <div>
            <span>Cart storage</span>
            {{ this.response }}
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import CartItem from "@/components/Cart/CartItem.vue"
    export default {
        data() {
            return {
                response: ''
            }
        },
        components:{
            CartItem
        },
        methods: {
            async fetchCart() {
                await axios.get('http://127.0.0.1:8000/cart/', {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then((res) => {
                this.response = res.data
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