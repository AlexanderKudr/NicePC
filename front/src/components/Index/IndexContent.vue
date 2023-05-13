<script setup >
import { ref } from 'vue'
const counter = ref(0);
</script>
<template>
    <div class="catalog_body">
        <a class="catalog_categories" href="cpu">
            <img class="img_body" src="@/resoures/cpu.jpg" alt="">
            <div>Процессоры</div>
        </a>
        <a class="catalog_categories" href="ram">
            <img class="img_body" src="@/resoures/ram.jpg" alt="">
            <div>Оперативная память</div>
        </a>
        <a class="catalog_categories" href="videocard">
            <img class="img_body" src="@/resoures/videocard.png" alt="">
            <div>Видеокарты</div>
        </a>
        <a class="catalog_categories" href="psu">
            <img class="img_body" src="@/resoures/psu.jpg" alt="">
            <div>Блоки питания</div>
        </a>
        <a class="catalog_categories" href="case">
            <img class="img_body" src="@/resoures/case.png" alt="">
            <div>Корпусы</div>
        </a>
        <a class="catalog_categories" href="motherboard">
            <img class="img_body" src="@/resoures/motherboard.png" alt="">
            <div>Материнские платы</div>
        </a>
        <a class="catalog_categories" href="cpu_cooler">
            <img class="img_body" src="@/resoures/cpu_fan.png" alt="">
            <div>Охлаждение процессора</div>
        </a>
        <a class="catalog_categories" href="case_cooler">
            <img class="img_body" src="@/resoures/case_fan.png" alt="">
            <div>Охлаждение корпуса</div>
        </a>
        <a class="catalog_categories" href="thermal">
            <img class="img_body" src="@/resoures/thermal_paste.png" alt="">
            <div>Термопасты</div>
        </a>
        <a class="catalog_categories" href="hdd_ssd">
            <img class="img_body" src="@/resoures/hdd.jpg" alt="">
            <div>Хранилище данных</div>
        </a>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
.catalog_body {
    // overflow-y: auto;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin: 60px 0 30px 0;

    @media screen and (max-width: 768px) {
        gap: 50px;
    }

}

.catalog_categories {
    width: 200px;
    height: 200px;
    text-align: center;

    @media screen and (max-width: 768px) {
        width: 80px;
        height: 80px;

    }

}

// .catalog_categories div {
//     padding-top: 20px;
//     font-weight: 500;
// }

.img_body {
    width: 180px;
    height: 180px;
    margin-bottom: 10px;

    @media screen and (max-width: 768px) {
        width: 80px;
        height: 80px;

    }
}
</style>