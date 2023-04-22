<template>
    <div class="profile_root">
        <div class="side_bar">
            <div class="side_bar_item">
                <a href="profile">Мой профиль</a>
            </div>
            <div class="side_bar_item">
                <div class="svg_arrow">
                    <img v-if="isOrdersShowen" src="@/components/Profile/arrow-down.svg" alt="">
                    <img v-if="!isOrdersShowen" src="@/components/Profile/arrow-right.svg" alt="">
                </div>
                <button @click="showOrders">
                    Заказы
                </button>
                <div v-if="isOrdersShowen">
                    <ul class="orders_dropdown">
                        <li><a href="#">Заказы</a></li>
                        <li><a href="cart">Корзина</a></li>
                        <li><a href="#">Избранное</a></li>
                    </ul>
                </div>
            </div>
            <div class="side_bar_item">
                <a href="#">Настройки профиля</a>
            </div>
        </div>
        <div class="profile_info">
            <div class="profile_info_title">
                Профиль
            </div>
            <div class="profile_info_main">
                <img class="profile_info_avatar" :src="path+'83577273.jpg'" alt="">
                <div>
                    Никита
                </div>
            </div>

        </div>
        <div class="bonuses">

        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        components:{
            
        },
        data() {
            return {
                isOrdersShowen: false,
                path: 'http://127.0.0.1:8000/images/avatar/'
            }
        },
        methods: {
            showOrders() {
                this.isOrdersShowen = !this.isOrdersShowen
            },

            // async fetchProfileInfo() {
            //     try {
            //         await axios.get('http://127.0.0.1:8000/cpu_item/').then((res) => {
            //         this.cpu_items = res.data
            //         })
            //     } 
            //     catch (error) {
            //         alert('Error while posting to API')
            //     }
            // }
        },
    }
</script>

<style>
.profile_root {
    display: flex;
    padding-top: 50px;
}

.side_bar {
    width: 500px;
}

.side_bar_item {
    padding-bottom: 20px;
    font-size: 18px;
}

.side_bar_item button {
    font-size: 18px;
}

.svg_arrow {
    position: absolute;
    margin-left: -20px;
    margin-top: 5px;
}

.svg_arrow img{
    width: 10px;
    height: 10px;

}

.orders_dropdown {
    padding-top: 15px;
}

.orders_dropdown li {
    padding-left: 10px;
    padding-bottom: 10px;
}

.profile_info_main{
    padding-top: 100px;
    display: flex;
    font-size: 20px;
    border-bottom: 1px solid rgb(0, 0, 0, 0.3);
}

.profile_info_title {
    font-size: 30px;
}

.profile_info_avatar {
    border: 0px solid white;
    border-radius: 50%;
    width: 100px;
    height: 100px;

}

.bonuses {

}
</style>