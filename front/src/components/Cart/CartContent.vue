<template>
    <div>
        <div class="cart_items">
            <cart-item :cart_item="cart_item" v-for="cart_item in cart_items" />
        </div>
        <div class="cart_top">
            <h2 class="cart_header">Корзина</h2>
            <div class="buy">
                <div class="buy-text">
                    <p>В корзине</p>
                    <p>{{ this.items_count }} товаров</p>
                    <p>На {{ this.allItemsPrice }}₽</p>
                </div>
                <div class="cart_buttons">
                    <button class="buying">К оформлению</button>
                    <button class="delete_all" @click="deleteAllItems">Очистить корзину</button>
                </div>
            </div>
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
    components: {
        CartItem
    },
    methods: {
        async fetchCart() {
            await axios.get('http://127.0.0.1:8000/cart/', { headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` } })
                .then((res) => {
                    this.cart_items = res.data
                    console.log(res.data)
                    this.items_count = res.data.length
                    for (let i = 0; i < res.data.length; i++) {
                        this.allItemsPrice += Number(res.data[i].price.replace(/\s+/g, ''))
                    }
                })
        },
        async deleteAllItems() {
            try {
                await axios.get('http://127.0.0.1:8000/cart/del/all/', { headers: { 'Authorization': `Bearer ${localStorage.getItem('token')}` } })
                location.reload()
            }
            catch (error) {
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
    display: flex;
    flex-direction: column;
    width: 60%;
    margin: 0 auto 70px;

}

.cart_header {
    font-size: 32px;
}

.buy {
    font-size: 20px;
    display: flex;
    padding: 5%;
    background-color: rgb(246, 246, 246);
    flex-direction: column;
    box-shadow: 0px 0px 3px 0px rgba(0, 0, 0, 0.392);

    &-text>p {
        margin-bottom: 10px;
        padding-left: 20%;
    }

    .cart_buttons {
        display: flex;
        flex-direction: column;
    }

    %reuse-buttons {
        height: 40px;
        border-radius: 5px;
        background-color: rgba(128, 0, 128, 0.5);
        width: 60%;
        color: rgb(240, 239, 239);
        transition:  0.15s all;
        font-weight: 600;

        &:hover {
            color: white;
        }
    }

    .buying {
        margin: 20px auto;
        @extend %reuse-buttons;
    }

    .delete_all {
        margin: 0 auto;
        @extend %reuse-buttons;
    }

}
</style>