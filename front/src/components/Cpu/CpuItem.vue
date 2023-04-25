<template>
    <div>
        <div class="cpu_item">
            <img class="cpu_picture" :src="path+cpu_item.cpu_image" alt="">
			<a  class="cpu_name" href="">
                {{ cpu_item.name }}
			</a>
			<div class="css_line"></div>
			<ul class="cpu_specifications">
				<li>Ядро: {{ cpu_item.core }}</li>
				<li>Частота: {{ cpu_item.cpu_clock }}</li>
				<li>Число ядер: {{ cpu_item.threads }}</li>
				<li>Сокет: {{ cpu_item.socket }}</li>
				<li>Тепловыделение: {{ cpu_item.tdp }}</li>
				<li>Технологический процесс: {{ cpu_item.nm }}</li>
			</ul>
			<p class="cpu_price">{{ cpu_item.price }}₽
                <button @click="addToCart" class="cpu_button">
				    {{ cart_button }}
			    </button>
            </p>
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
            this.cart_button = 'clicked'
            await axios.post('http://127.0.0.1:8000/cart/', this.cpu_item.id).then((res) => {
                    
                })
        }
    }
}
</script>

<style>
.cpu_item{
    position: relative;
    display: grid;
    grid-template-columns: 220px 52px auto 52px 239px;
    grid-template-areas:
    "image . header    .       controls" 
    "image . separator   .       .     " 
    "image . description description order   ";
    padding: 20px 30px 30px;
    margin-top: 30px;
    background-color: white;
    border-bottom: 1px solid rgb(223, 223, 225);
    transition: all 0.3s ease 0s;
    z-index: -1;
  }
.cpu_item:hover{
    box-shadow: 0 0 10px rgb(187, 187, 187);
}

.cpu_specifications{
    list-style: none;
    grid-area: description;
    font-size: 14px;
    line-height: 18px;
}
.cpu_name{
    grid-area: header;
    font-size: 20px;
}
.css_line{
    grid-area: separator;
    width: 100%;
    height: 1px;
    background-color: rgb(245, 245, 246);
}

.cpu_picture{
    width: 250px;
    height: 200px;
    grid-area: image;
}

.cpu_price{
    font-size: 32px;
    flex-wrap: wrap;
    -moz-box-pack: end;
    justify-content: flex-end;
    align-self: flex-end;
    gap: 8px;
    grid-area: order;
    padding-bottom: 40px;
}

.cpu_button{
    height: 40px;
    padding: 0px 20px;
    font-size: 16px;
    line-height: 20px;
    width: 100%;
    border-radius: 6px;
    border: 1px solid transparent;
    text-align: center;
    background-color: rgba(128, 0, 128, 0.5);
    color: white;
}
</style>