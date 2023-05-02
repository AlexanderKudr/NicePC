<template>
    <div>
        <div class="cart_top">
            <h2>Корзина</h2>
            <div class="buy">
                <p class="text1">В корзине</p> 
                <p class="text2">{{ this.items_count }} товаров</p>
                <p class="text3">На {{ this.allItemsPrice }}₽</p>
                <button class="buying">К оформлению</button>
                <button class="delete_all" @click="deleteAllItems">Очистить корзину</button>
            </div>
        </div>
        <div class="cart_items">
            <cart-item :cart_item="cart_item" v-for="cart_item in cart_items"/>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import CartItem from "@/components/Cart/CartItem.vue"
    export default {
        data() {
            return {
                cart_items: [],
                items_count: null,
                allItemsPrice: 0
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
                this.items_count = res.data.length
                for (let i = 0; i < res.data.length; i++) {
                    this.allItemsPrice += Number(res.data[i].price.replace(/\s+/g, ''))
                }
            })
            },
            async deleteAllItems() {
                try{
                    await axios.get(`http://127.0.0.1:8000/cart/delete/all/`, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
                    location.reload()
                }
                catch(error) {
                    alert('Error')
                }
            }
        },
        beforeMount() {
            this.fetchCart()
        }
    }
</script>

<style lang="scss">
.cart_top {
    position: relative;
    display: flex;
    justify-content: space-between;
}

.cart_items {
    margin-top: -230px;
    max-width: 920px;
}

.buy {
    font-size: 20px;
    display: flex;
    padding: 20px;
    background-color: rgba(202, 202, 202, 0.5);
    flex-direction: column;
    width: 300px;
    margin-top: 100px;

    .text2{
        margin-top: 5px;
    }

    .text3{
        margin-top: 20px;
    }

    .buying{
        height: 40px;
        margin-top: 20px;
        border-radius: 5px;
        background-color: rgba(128, 0, 128, 0.5);
    }

    .buying:hover{
        color: white;
    }
    
    .delete_all{
        height: 40px;
        border-radius: 5px;
        margin-top: 20px;
        background-color: rgba(128, 0, 128, 0.5);
    }
    .delete_all:hover{
        color: white;
    }
}
</style>