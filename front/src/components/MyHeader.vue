<template>
    <header>
		<modal v-model:show="dialogVisible">
            <div class="myform_title">
                <div @click="showSignIn">
                    Вход
                </div>
                <span>/</span>
                <div @click="showSignUp">
                    Регистрация
                </div>
            </div>
 
            <form v-if="signIn" @submit.prevent>

                <input type="username" placeholder="Имя пользователя" class="inputbox" required v-model="loginForm.username">
                <input type="password" placeholder="Пароль" class="inputbox" required v-model="loginForm.password">
                <div class="forgot">
                    <a href="#">Забыли пароль?</a>
                </div>
                <button class="login_button" @click="tryLogin">Войти</button>
            </form>

            <form v-if="signUp" @submit.prevent>

                <input type="username" placeholder="Имя пользователя" class="inputbox" required v-model="registerForm.username">
                <input type="email" placeholder="Электронная почта" class="inputbox" required v-model="registerForm.email">
                <input type="password" placeholder="Пароль" class="inputbox" required v-model="registerForm.password">
    
                <button class="login_button" @click="tryRegister">Зарегистрироваться</button>
            </form>
        </modal>
		<div class="header_all_info">
			<div class="logo">
				<a href="/">
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
				<a>+7(981)459-09-38</a>
			</div>
			<div class="info_block">
                Дипломный проект Гончеренко Владислава
			</div>
		</div>
		<div class="catalog">
			<div class="catalog_search">
				<input class="input_search" type="text" placeholder="Поиск по комплектующим">
			</div>

            <svg class=" Icon Icon_size_m"><use href="#Wishlist"></use></svg>
            <svg class=" Icon Icon_size_m"><use href="#Wishlist"></use></svg>


			<div class="catalog_cart">
				<ul>
					<li class='login_ui' v-if="localStorageToken === null"><button @click="showDialog">Войти</button></li>
                    <li class='login_ui' v-if="localStorageToken !== null"><button @click="showDropdown">{{ this.localStorageUsername }}</button></li>
					<li class='favorites_ui'><a href="">Избранное</a></li>
					<li class='compare_ui'><a href="">Сравнение</a></li>
					<li class='cart_ui'><a href="cart">Корзина</a></li>
				</ul>
                <div class="dropdown_content" v-if="dropdownVisible">
                    <div class="dropdown_info">
                        <ul>
                            <li><a href="profile">Мой профиль</a></li>
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
    import axios from 'axios'
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
            registerForm: {
                username: '',
                email: '',
                password: ''
            },
            localStorageToken: localStorage.getItem('token'),
            localStorageUsername: localStorage.getItem('username'),
            upHere: false,
            signIn: true,
            signUp: false
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
        },
        showSignIn() {
            this.signIn = true
            this.signUp = false
        },
        showSignUp() {
            this.signIn = false
            this.signUp = true
        },
        async tryRegister() {
            await axios.post('http://localhost:8000/user/', this.registerForm).then((res) => {
                if (res.status === 200) {
                    this.dialogVisible = false
                    this.signIn = true
                    this.signUp = false
                }
            })
        }
    },
}
</script>

<style>
.test_token {
    margin-top: 20px;
}

.logo a {
    background: url('@/resoures/1036686.png') left no-repeat;
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

.header_all_info {
    display: flex;
    justify-content: space-between;
    padding-top: 40px;
}

.info_block ul {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.choose_number {
    margin-right: 220px;
}

.catalog {
    display: flex;
    justify-content: space-between;
    position: sticky;
    top: 10px;
}

.catalog_search {
    margin-left: 450px;
    padding-top: 45px;
}

.input_search {
    width: 40em;
    height: 40px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.input_search:hover {
    border-bottom: 1px solid rgba(236, 170, 236, 0.781);
}

.input_search:focus {
    box-shadow: 0px 15px 10px -15px rgba(221, 134, 221, 0.781);
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

.login_ui {
    padding-bottom: 25px;
}

.login_ui button {
    background: url('@/resoures/user.svg') top no-repeat;
    background-size: 18px 18px;
    padding-top: 25px;
}

.favorites_ui a {
    background: url('@/resoures/favorites.svg') top no-repeat;
    background-size: 20px 20px;
    padding-top: 25px;
}

.compare_ui a {
    background: url('@/resoures/compare.svg') top no-repeat;
    background-size: 20px 20px;
    padding-top: 25px;
}

.cart_ui a {
    background: url('@/resoures/cart.svg') top no-repeat;
    background-size: 20px 20px;
    padding-top: 25px;
}

.myform_title {
    font-size: 30px;
    margin-bottom: 70px;
    display: flex;
}

.myform_title div {
    margin: 0 auto;
}

.myform_title div:hover {
    color: rgba(128, 0, 128, 0.5);
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
</style>