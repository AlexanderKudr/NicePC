<template>
    <div class="profile_root">
        <div class="side_bar">
            <div class="side_bar_item">
                <a href="profile">Мой профиль</a>
            </div>
            <div class="side_bar_item">
                <img class="svg_arrow" v-if="isOrdersShowen" src="@/components/Profile/arrow-down.svg" alt="">
                <img class="svg_arrow" v-if="!isOrdersShowen" src="@/components/Profile/arrow-right.svg" alt="">
                <button @click="showOrders">
                    Заказы
                </button>
                <div v-if="isOrdersShowen">
                    <ul class="orders_dropdown">
                        <li><a href="#">Заказы</a></li>
                        <li><a href="#">Корзина</a></li>
                        <li><a href="#">Избранное</a></li>
                    </ul>
                </div>
            </div>
            <div class="side_bar_item">
                <a href="#">Настройки профиля</a>
            </div>
        </div>
        <div class="profile_info">

        </div>
        <div class="bonuses">

        </div>
    </div>
</template>

<script>

    export default {
        components:{
            
        },
        data() {
            return {
                isOrdersShowen: false,
                //
            }
        },
        methods: {
            showOrders() {
                this.isOrdersShowen = !this.isOrdersShowen
            }
        },
    }
</script>

<style>
.profile_root {
    padding-top: 100px;
    height: 500px;
}

.side_bar {
    
}

.side_bar_item {
    padding-bottom: 20px;
    font-size: 18px;
}

.side_bar_item button {
    font-size: 18px;
}

.svg_arrow{
    width: 20px;
    height: 20px;
    margin-right: 20px;
    position: absolute;
}

.orders_dropdown {
    padding-top: 15px;
}

.orders_dropdown li{
    padding-left: 10px;
    padding-bottom: 10px;
}

.profile_info {

}

.bonuses {

}
</style>