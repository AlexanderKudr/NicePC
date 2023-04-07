<template>
    <header>
		<modal v-model:show="dialogVisible">
            <form @submit.prevent>
                <div class="myform_title"><h2>Вход</h2></div>
                <input type="username" placeholder="username" class="inputbox" required v-model="loginForm.username">
                <input type="password" placeholder="Пароль" class="inputbox" required v-model="loginForm.password">
                <div class="forgot">
                    <a href="#">Забыли пароль?</a>
                </div>
                <button class="login_button" @click="tryLogin">Войти</button>
            </form>
        </modal>
		<div class="header_all_info">
			<div class="logo">
				<a class="function" href="/">
					NicePC
					<p class="wtf">лучшее для вас</p>
				</a>

			</div>
			<div class="choose_number">
				<select name="">
					<option value="">Петрозаводск</option>
					<option value="">Хабаровск</option>
					<option value="">Саратов</option>
					<option value="">Калуга</option>
				</select>
				<a class="function">+7(981)459-09-38</a>
			</div>
			<div class="info_block">
				<ul class="menu_link">
					<li class="link"><a class="function" href="">Журнал</a></li>
					<li class="link"><a class="function" href="">Конфигуратор</a></li>
					<li class="link"><a class="function" href="">Магазины</a></li>
					<li class="link"><a class="function" href="">Обратная связь</a></li>
				</ul>
			</div>
		</div>
		<div class="catalog">
			<div class="catalog_menu">
				<select name="Каталог" class="catalog_menu_select">
					<a href=""><option value="">Материнские платы</option></a>
					<option value=""><a href="">Оперативная память</a></option>
					<option value="">Видеокарты</option>
					<option value="">Блоки питания</option>
					<option value="">Корпусы</option>
					<option value="">Процессоры</option>
					<option value="">Системы охлаждения процессора</option>
					<option value="">Системы охлаждения корпуса</option>
					<option value="">Термопасты</option>
				</select>
			</div>
			<div class="catalog_search">
				<input class="input_search" type="text" placeholder="Поиск по комплектующим">
			</div>
			<div class="catalog_cart">
				<ul>
					<li><button @click="showDialog" class="login_cart">{{ username }}</button></li>
					<li><a class="cart" href="">Избранное</a></li>
					<li><a class="cart" href="">Сравнение</a></li>
					<li><a class="cart" href="">Корзина</a></li>
				</ul>	
			</div>
		</div>
	</header>
</template>

<script>
	import Modal from '@/components/Modal.vue'
    import axios from 'axios'
    export default {
    components: {
    Modal
    },
    data() {
        return {
            dialogVisible: false,
            loginForm: {
                username: '',
                password: '',
            },
            username: 'Войти'

        }
    },
    methods: {
        showDialog() {
        this.dialogVisible = true
    },
    async tryLogin(post) {
        this.dialogVisible = false
        try {
            var qs = require('qs')
            await axios.post('http://127.0.0.1:8000/login', qs.stringify({'username': this.loginForm.username, 'password': this.loginForm.password})).then((res) => {
            this.username = res.data.username
            this.loginForm = {
                username: '',
                password: '',
            }
          })
        } catch (error) {
            alert('Error while posting to API')
        }
        },
    }
}
</script>

<style>
.logo a {
    background: url('../resoures/1036686.png') left no-repeat;
    background-size: 35px 35px;
    padding-left: 50px;
    display: block;
    width: 150px;
    height: 35px;
    font-size: 25px;
}

.wtf {
    font-size: 12px;
}

a{
    color:black;
}

a:visited {
    color :black;
}

* {
    font-family: 'Montserrat', sans-serif;
}

.header_all_info {
    display: flex;
    justify-content: space-between;
    padding: 40px 200px;
}

.info_block ul {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.function:hover {
    color: orange;
}

.choose_number {
    margin-right: 220px;
}

.catalog {
    display: flex;
    justify-content: space-between;
    padding: 0 200px;
    position: sticky;
    top: 10px;
}

.catalog_search {
    margin-left: 93px;
    padding-top: 22px;
}

.input_search {
    width: 30em;
    height: 40px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.input_search:focus {
    box-shadow: 0px 15px 10px -15px rgba(127, 190, 213, 0.93);
}


.catalog_menu_select {
    padding: 20px 0;
    border: 1px solid black;
    border-radius: 10px;
    font-size: 16px;
}

.catalog_cart {
    padding-top: 45px;
}

.catalog_cart ul {
    display: flex;
    justify-content: space-between;
    gap: 30px;
    align-items: center;
}

.cart:hover {
    color: orange;
}

.myform_title {
    margin: 0 auto;
    font-size: 20px;
    margin-bottom: 70px;
}


.inputbox {
    border: 1px solid rgba(0, 0, 0, 0.5);
    border-radius: 5px;
    display: block;
    margin: 0 auto;
    margin-bottom: 25px;
    width: 350px;
    height: 40px;
}

.forgot {
    padding-left: 45px;
}

.login_button {
    margin: 0 auto;
    margin-top: 60px;
    display: block;
    border: 1px solid rgba(0, 0, 0, 0);
    border-radius: 25px;
    background-color: rgba(128, 0, 128, 0.5);
    width: 400px;
    height: 50px;
    font-size: 16px;
}

</style>