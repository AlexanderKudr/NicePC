<template>
    <div>
        <div class="cpu_item">
            <div class="left-box">
                <div>
                    <img class="cpu_picture" :src="path+cpu_item.cpu_image" alt="">
                </div>
                <div>
                    <div class="cpu_name">
                        <a href="">
                            {{ cpu_item.name }}
                        </a>
                    </div>
                    <div class="css_line">
                    </div>
                    <ul class="cpu_specifications">
                        <li>Ядро: {{ cpu_item.core }}</li>
                        <li>Частота: {{ cpu_item.cpu_clock }}</li>
                        <li>Число ядер: {{ cpu_item.threads }}</li>
                        <li>Сокет: {{ cpu_item.socket }}</li>
                        <li>Тепловыделение: {{ cpu_item.tdp }}</li>
                        <li>Технологический процесс: {{ cpu_item.nm }}</li>
                    </ul>
                </div>
            </div>
            <div>
                <p class="cpu_price">{{ cpu_item.price }}₽</p>
                <button @click="addToCart" class="cpu_button">
                    {{ cart_button }}
                </button>
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
            cart_button: 'В корзину'
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
            await axios.post('http://127.0.0.1:8000/cart/', {'product_id': this.cpu_item.id}, {headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}})
            .then((res) => {
                if (res.status === 200) {
                    this.cart_button = 'Добавлено'
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

.cpu_name {
    margin-bottom: 20px;
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

.cpu_button {
    height: 40px;
    padding: 0px 20px;
    font-size: 16px;
    border-radius: 6px;
    border: 1px solid transparent;
    text-align: center;
    background-color: rgba(128, 0, 128, 0.5);
    color: white;
}
</style>