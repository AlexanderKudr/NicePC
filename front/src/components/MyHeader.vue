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
					<li v-if="localStorageToken === null"><button @click="showDialog">Войти</button></li>
                    <li v-if="localStorageToken !== null"><button @click="showDropdown">{{ this.localStorageUsername }}</button></li>
					<li><a class="cart" href="">Избранное</a></li>
					<li><a class="cart" href="">Сравнение</a></li>
					<li><a class="cart" href="cart">Корзина</a></li>
				</ul>
                <div class="dropdown_content" v-if="dropdownVisible">
                    <div class="dropdown_info">
                        <ul>
                            <li><a href="#">Мой профиль</a></li>
                            <li><a href="#">Заказы</a></li>
                            <li><button @click="tryLogout">Выйти</button></li>
                        </ul>
                    </div>
                </div>
                <div class="dropdown" v-if="dropdownVisible" @click="hideDropdown"></div>
			</div>
		</div>
	</header>
</template>

<script>
	import Modal from '@/components/Modal.vue'

    export default {
    components: {
    Modal
    },
    data() {
        return {
            dialogVisible: false,
            dropdownVisible: false,
            loginForm: {
                username: '',
                password: '',
            },
            localStorageToken: localStorage.getItem('token'),
            localStorageUsername: localStorage.getItem('username'),
            upHere: false
        }
    },
    methods: {
        showDialog() {
        this.dialogVisible = true
        },
        showDropdown() {
            this.dropdownVisible = true
        },
        hideDropdown() {
            this.dropdownVisible = false
        },
        tryLogin() {
            this.dialogVisible = false
            this.$store.dispatch('onLogin', {
                login: this.loginForm.username,
                password: this.loginForm.password
            })
                .then(() => {
                    location.reload()
                })
        },
        tryLogout() {
            this.$store.dispatch('onLogout')
                .then(() => {
                    location.reload()
                })
        }
    },
}
</script>

<style>
.test_token {
    margin-top: 20px;
    margin-left: 200px;
}

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

.dropdown {
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    position: fixed;
    z-index: 1;
}

.dropdown_content {
    position: absolute;
    width: 300px;
    height: 350px;
    border: 1px solid white;
    border-radius: 25px;
    background-color: white;
    margin-top: 10px;
    box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);
    z-index: 2;
}

.dropdown_info {
    margin-top: 50px;
    margin-left: 40px;
}

.dropdown_info ul {
    display: block;
}
.dropdown_info li {
    font-size: 20px;
    padding-bottom: 20px;
}

.dropdown_info li button {
    font-size: 20px;
}

.dropdown_info li a:hover {
    color: orange;
}

.dropdown_info li button:hover {
    color: orange;
}
</style>