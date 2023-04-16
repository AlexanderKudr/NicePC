<template>
    <div class="cart_item">
        <div class="product">
            <img src="@/resoures/intelcore_i5-10400f.jpg" alt="">
            <a class="name" href="">Intel Core i5 12400F</a>
            <a class="price" href="">14 990₽</a>
            <button class="delete"></button>
        </div>
        <div class="buy">
            В корзине
            1 товар
            14 990₽
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss">
    .cart_item {
        display: grid;
        grid-template-columns: repeat(5,1fr);
        margin: 0 auto;
        .product {
            img {
            width: 100px;
            }
        }
    }
    .buy{
        background-color: grey;
    }
</style>