<template>
    <div class="catalog_body">
        <a class="catalog_categories" href="cpu">
            <img class="img_body" src="@/resoures/cpu_image_dev.png" alt="">
            <br> Процессоры
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/ram.jpg" alt="">
            <br> Оперативная память
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/videocard.jpg" alt="">
            <br> Видеокарты
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/powersupply.jpg" alt="">
            <br> Блоки питания
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/case.jpeg" alt="">
            <br> Корпусы
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/motherboard.jpg" alt="">
            <br> Материнские платы
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/coolerforproc.jpg" alt="">
            <br> Системы охлаждения процессора
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/collerforcase.jpg" alt="">
            <br> Системы охлаждения корпуса
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/termpaste.png" alt="">
            <br> Термопасты
        </a>
        <a class="catalog_categories" href="">
            <img class="img_body" src="@/resoures/CreatedPack.png" alt="">
            <br> Готовые Сборки
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
    width: 100%;
    grid-auto-rows: min-content;
    max-height: 1500px;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    padding-top: 100px;
}

.img_body{
    width: 180px;
    height: 140px;
}
</style>