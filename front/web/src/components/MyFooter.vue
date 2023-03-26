<template>
    <footer>
		<div class="footer">
			<div class="footer_contacts">
				<h1>Контакты</h1>
				<a class="footter_sup" href="">Адреса магазинов</a><br>
				<a class="footter_sup" href="">+7(981)459-09-38</a>
				<select class="city_change" name="" id="">Выбор города
					<option value="">Петрозаводск</option>
					<option value="">Хабаровск</option>
					<option value="">Саратов</option>
					<option value="">Калуга</option>
				</select><br>
				<button>
					<a class="footter_sup" href="">Задать вопрос</a>
				</button>
			</div>
			<div class="footer_info">
				<ul class="footer_ul_info">
					<a class="footter_sup" href=""><li>Журнал</li></a>
					<a class="footter_sup" href=""><li>Акции</li></a>
                    <a class="footter_sup" href=""><li>Информация</li></a>
                    <a class="footter_sup" href=""><li>Доставка</li></a>
                    <a class="footter_sup" href=""><li>Гарантия</li></a>
                    <a class="footter_sup" href=""><li>Кредит и рассрочка</li></a>
				</ul>
				<ul class="footer_support">
					<a class="footter_sup" href=""><li>Сервисные центры</li></a>
					<a class="footter_sup" href=""><li>Услуги</li></a>
					<a class="footter_sup" href=""><li>Корпоративным клиентам</li></a>
					<a class="footter_sup" href=""><li>Аренда помещений</li></a>
					<a class="footter_sup" href=""><li>Партнёрская программа</li></a>
					<a class="footter_sup" href=""><li>Обзоры</li></a>
					<a class="footter_sup" href=""><li>Форум</li></a>
				</ul>
			</div>
		</div>
	</footer>
</template>

<script>
    export default {
        
    }
</script>

<style>
.footer_info{
    display: flex;
    margin-left: 40px;
}
.footer_support{
    margin-left:120px;
    list-style: none
}
.footer{
    display: flex;
    color: rgb(0, 0, 0);
    justify-content: space-between;
	padding: 40px 200px;
}
.footer_ul_info{
  font-family: "PT Root UI5", sans-serif;
  list-style: none;
  color: rgb(0, 0, 0);
}
.footter_sup{
    text-decoration: none;
    color: rgb(0, 0, 0);
    font-weight: 440;
    cursor: pointer;
}
 
.footter_sup:hover {
    color: orange;
}

.footer_ul_docs{
    list-style: none;
    color: rgb(0, 0, 0);
    
}
.footter_docs{
    text-decoration: none;
    color: rgb(0, 0, 0);
    cursor: pointer;
}

.footter_docs:hover{
    color: orange;
}


</style>