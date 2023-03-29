!<template>
    <div>
        <div class="cpu_item">
            <img class="cpu_picture" src="../resoures/6028061696.jpg" alt="">
			<a  class="cpu_name" href="">
					Intel Core i5-10400F, OEM
			</a>
			<div class="css_line"></div>
			<ul class="cpu_specifications">
				<li>{{ this.core }}</li>
				<li>Частота: 2.6 ГГц и 4.4 ГГц в режиме Turbo;</li>
				<li>Сокет: LGA 1200;</li>
				<li>Потоков 6, 12;</li>
				<li>Тепловыделение: 65 Вт;</li>
				<li>Технологический процесс: 14 нм;</li>
			</ul>
			<p class="cpu_price">11 490₽
			    <button class="cpu_button">
				    В корзину
			    </button>
            </p>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                core: "Ядро: Sandy Bridge"
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
    margin-left: 196px;
    margin-right: 196px;
    background-color: white;
    border-bottom: 1px solid rgb(223, 223, 225);
    transition: all 0.3s ease 0s;
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
    margin: 0px;
    box-sizing: border-box;
    outline: 0px;
    font-style: inherit;
    font-variant: inherit;
    font-stretch: inherit;
    font-family: inherit;
    font-size-adjust: inherit;
    font-kerning: inherit;
    font-optical-sizing: inherit;
    font-language-override: inherit;
    font-feature-settings: inherit;
    font-variation-settings: inherit;
    text-decoration: none;
    white-space: nowrap;
    appearance: none;
    overflow: hidden;
    cursor: pointer;
    width: 100%;
    -moz-box-pack: center;
    justify-content: center;
    -moz-box-align: center;
    align-items: center;
    position: relative;
    border-radius: 6px;
    border: 1px solid transparent;
    text-align: center;
    transition-property: color, font-weight, border-bottom-color;
    transition-duration: 150ms;
    transition-timing-function: ease-in-out;
    background-color: rgb(176, 176, 176);
    color: rgb(255, 255, 255);
    font-weight: 500;
}
</style>