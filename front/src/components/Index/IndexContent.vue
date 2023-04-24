<template>
    <div class="catalog_body">
        <a class="catalog_categories" href="cpu">
            <img class="img_body" src="@/resoures/cpu.jpg" alt="">
            <div>Процессоры</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/ram.jpg" alt=""> 
            <div>Оперативная память</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/videocard.png" alt="">
            <div>Видеокарты</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/psu.jpg" alt="">
            <div>Блоки питания</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/case.png" alt="">
            <div>Корпусы</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/motherboard.png" alt="">
            <div>Материнские платы</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/cpu_fan.png" alt="">
            <div>Охлаждение процессора</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/case_fan.png" alt="">
            <div>Охлаждение корпуса</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/thermal_paste.png" alt="">
            <div>Термопасты</div>
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/done_pc.jpg" alt="">
            <div>Готовые Сборки</div>
        </a>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>
.catalog_body{
    display: grid;
    grid-auto-rows: min-content;
    grid-template-columns: repeat(5, 1fr);
    gap: 50px;
    padding-top: 100px;
    max-width: 1300px;
    margin: 0 auto;
}

.catalog_categories {
    width: 200px;
    height: 200px;
    text-align: center;
}

.catalog_categories div {
    padding-top: 20px;
    font-weight: 500;
}

.img_body{
    width: 180px;
    height: 180px;
}
</style>