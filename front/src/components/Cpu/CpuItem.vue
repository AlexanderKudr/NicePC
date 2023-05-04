<template>
    <div>
        <div class="cpu_item">
            <div class="left-box">
                <div>
                    <img class="cpu_picture" :src="path+cpu_item.image" alt="">
                </div>
                <div>
                    <div class="cpu_name">
                        <button @click="$router.push(`/cpu/${cpu_item.id}`)">
                            {{ cpu_item.name }}
                        </button>
                    </div>
                    <div class="css_line">
                    </div>
                    <ul class="cpu_specifications">
                        <li>Ядро: {{ cpu_item.param1 }}</li>
                        <li>Частота: {{ cpu_item.param2 }}</li>
                        <li>Число ядер: {{ cpu_item.param3 }}</li>
                        <li>Сокет: {{ cpu_item.param4 }}</li>
                        <li>Тепловыделение: {{ cpu_item.param5 }}</li>
                        <li>Технологический процесс: {{ cpu_item.param6 }}</li>
                    </ul>
                </div>
            </div>
            <div>
                <p class="cpu_price">{{ cpu_item.price }}₽</p>

                <div v-if="!isInCart" class="buy_button">
                    <button @click="addToCart">Купить</button>
                </div>
                <div v-if="isInCart" class="buy_button">
                    <a href="cart">К корзине</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            path: 'http://127.0.0.1:8000/',
            isInCart: false
        }  
    },
    props: {
        cpu_item: {
            type: Object,
            required: true,
        }
    },
    methods: {  
        async addToCart() {
            await axios.post('http://127.0.0.1:8000/cart/', {'product_id': this.cpu_item.id, 'price': this.cpu_item.price, 'name': this.cpu_item.name}, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then((res) => {
                if (res.status === 200) {
                    this.isInCart = !this.isInCart
                }
            })
        }
    }
}
</script>

<style>

.cpu_item {
    display: flex;
    justify-content: space-between;
    max-width: 1500px;
    margin: 0 auto;
    margin-bottom: 100px;
}

.left-box {
    display: flex;
}

.cpu_picture {
    width: 200px;
    height: 200px;
    margin-right: 50px;
}

.cpu_name button {
    font-size: 20px;
}

.css_line{
    margin-bottom: 40px;
    width: 400px;
    height: 1px;
    background-color: rgb(202, 202, 202);
}

.cpu_specifications li {
    line-height: 20px;
}

.cpu_price {
    font-size: 25px;
    margin-bottom: 20px;
}

.buy_button {
    border-radius: 6px;
    border: 1px solid transparent;
    text-align: center;
    background-color: rgba(128, 0, 128, 0.5);
    width: 120px;
    height: 50px;
}

.buy_button a {
    font-size: 16px;
    line-height: 50px;
}

.buy_button button {
   padding-top: 15px;
   font-size: 16px;
}
</style>