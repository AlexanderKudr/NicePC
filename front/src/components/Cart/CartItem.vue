<template>

    <div class="cart_item">
        <div class="items">
            <div class="product">
                <img src="@/resoures/intelcore_i5-10400f.jpg" alt="">
                <p class="name" href="">{{ cart_item.name }}</p>
                <p class="price" href="">{{ cart_item.price }}₽</p>
                <button @click="deleteItem" class="tooltip">
                    <img src="@/resoures/delete_button.svg" alt="">
                </button>
            </div>
        </div>
        
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data() {
            return {

            }
        },
        props: {
            cart_item: {
                type: Object,
                required: true,
            }
        },
        methods: {
            async deleteItem() {
                await axios.get(`http://127.0.0.1:8000/cart/delete/${this.cart_item.id}`, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
                location.reload()
            }
        }
    }
</script>

<style lang="scss">
    
h2{
    margin-top: 10px;
    margin-bottom: 20px;
    font-size: 30px;
}

.cart_item {
    display: grid;
    grid-template-columns: repeat(5,1fr);
    margin: 0 auto;

    .items {
        grid-column: auto / span 4;
    }

    .product {
        display: grid;
        grid-template-columns: min-content 7fr 4fr min-content;
        grid-template-areas:
            "image title  status  actions" 
            "image delivery status  actions" 
            ".   marked   marked  .    " 
            ".   content  content .    ";
        font-size: 20px;
        margin-bottom: 90px;

        .tooltip {
            z-index: 2;
        }

        .tooltip img {
        width: 30px;
        height: 30px;
        }
            
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
}
</style>