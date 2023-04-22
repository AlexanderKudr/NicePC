<template>
    <p class="back"><a href="">Обратно к покупкам</a></p>
    <h1>Корзина</h1>
    <div class="cart_item">
        <div class="product">
            <img src="@/resoures/intelcore_i5-10400f.jpg" alt="">
            <a class="name" href="">Intel Core i5 12400F</a>
            <a class="price" href="">14 990₽</a>
        </div>
        <div class="buy">
            <p class="text1">В корзине</p> 
            <p class="text2">1 товар</p>
            <p class="text3">14 990₽</p>
            <button class="delete">К оформлению</button>
            <button class="delete_all">Очистить корзину</button>
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss">
    .back{
        margin-top: 40px;
    }
    h1{
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 30px;
    }
    .cart_item {
        display: grid;
        grid-template-columns: repeat(5,1fr);
        margin: 0 auto;
        .product {
            display: grid;
            grid-template-columns: min-content 7fr 4fr min-content;
            grid-template-areas:
                "image title  status  actions" 
                "image delivery status  actions" 
                ".   marked   marked  .    " 
                ".   content  content .    ";
            font-size: 20px;
            grid-column: auto / span 4;
            img {
                grid-area: image;
                width: 100px;
            }
        }
    
    .buy{
        font-size: 20px;
        display: flex;
        padding: 20px;
        grid-column: auto / span 1;
        background-color: rgba(202, 202, 202, 0.5);
        flex-direction: column;
        .text2{
            margin-top: 5px;
        }
        .text3{
            margin-top: 20px;
        }
        .delete{
            height: 40px;
            margin-top: 20px;
            border-radius: 5px;
            background-color: rgba(128, 0, 128, 0.5);
        }
        .delete:hover{
            color: white;
        }
        
    }
    .delete_all{
            height: 40px;
            margin-top: 20px;
            border-radius: 5px;
            background-color: rgba(128, 0, 128, 0.5);
        }
    .delete_all:hover{
        color: white;
    }
    }
</style>