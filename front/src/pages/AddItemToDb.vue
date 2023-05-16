<template>
    <ul class="choose_item">
        <li @click="setTypeId1">Процессор</li>
        <li @click="setTypeId2">Оператос</li>
        <li @click="setTypeId3">Видеокарта</li>
        <li @click="setTypeId4">Блок питания</li>
        <li @click="setTypeId5">Корпус</li>
        <li @click="setTypeId6">Материнка</li>
        <li @click="setTypeId7">Охлад проца</li>
        <li @click="setTypeId8">Охлад корпуса</li>
        <li @click="setTypeId9">Термопаста</li>
        <li @click="setTypeId10">Хранилище данных</li>
    </ul>
    <div v-if="this.form.type_id === 1">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Название" v-model="form.name">
            <input type="text" placeholder="Ядро" v-model="form.param1">
            <input type="text" placeholder="Частота" v-model="form.param2">
            <input type="text" placeholder="Сокет" v-model="form.param3">
            <input type="text" placeholder="Число ядер" v-model="form.param4">
            <input type="text" placeholder="Тепловыделение" v-model="form.param5">
            <input type="text" placeholder="Технологический процесс" v-model="form.param6">
            <input type="text" placeholder="param7" v-model="form.param7">
            <input type="text" placeholder="Цена" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 2">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Название" v-model="form.name">
            <input type="text" placeholder="Объем" v-model="form.param1">
            <input type="text" placeholder="Частота" v-model="form.param2">
            <input type="text" placeholder="Латентность" v-model="form.param3">
            <input type="text" placeholder="Тайминги" v-model="form.param4">
            <input type="text" placeholder="Форм-фактор" v-model="form.param5">
            <input type="text" placeholder="Цена" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 3">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Видеочипсет" v-model="form.param1">
            <input type="text" placeholder="Память" v-model="form.param2">
            <input type="text" placeholder="Интерфейс" v-model="form.param3">
            <input type="text" placeholder="Техпроцесс" v-model="form.param4">
            <input type="text" placeholder="Разъемы" v-model="form.param5">
            <input type="text" placeholder="Питание" v-model="form.param6">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 4">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Мощность" v-model="form.param1">
            <input type="text" placeholder="Форм-фактор" v-model="form.param2">
            <input type="text" placeholder="Вентилятор" v-model="form.param3">
            <input type="text" placeholder="Разъемы" v-model="form.param4">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 5">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Форм-фактор" v-model="form.param1">
            <input type="text" placeholder="Внутренние отсеки" v-model="form.param2">
            <input type="text" placeholder="Разъемы" v-model="form.param3">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 6">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Форм-фактор" v-model="form.param1">
            <input type="text" placeholder="Сокет" v-model="form.param2">
            <input type="text" placeholder="Память" v-model="form.param3">
            <input type="text" placeholder="Слоты" v-model="form.param4">
            <input type="text" placeholder="Разъемы" v-model="form.param5">
            <input type="text" placeholder="Сеть" v-model="form.param6">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 7">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Вентиляторы" v-model="form.param1">
            <input type="text" placeholder="Максимальное тепловыделение ЦП" v-model="form.param2">
            <input type="text" placeholder="Радиатор" v-model="form.param3">
            <input type="text" placeholder="Основание" v-model="form.param4">
            <input type="text" placeholder="Питание от МП" v-model="form.param5">
            <input type="text" placeholder="Высота кулера" v-model="form.param6">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 8">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Вентиляторы" v-model="form.param1">
            <input type="text" placeholder="Питание от МП" v-model="form.param2">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 9">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Теплопроводность" v-model="form.param1">
            <input type="text" placeholder="Вес" v-model="form.param2">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
    <div v-if="this.form.type_id === 10">
        <form @submit.prevent class="send_item">
            <input type="text" placeholder="Name" v-model="form.name">
            <input type="text" placeholder="Объем накопителя" v-model="form.param1">
            <input type="text" placeholder="Скорости:" v-model="form.param2">
            <input type="text" placeholder="Интерфейс" v-model="form.param3">
            <input type="text" placeholder="Форм-фактор" v-model="form.param4">
            <input type="text" placeholder="Тепловыделение" v-model="form.param5">
            <input type="text" placeholder="Технологический процесс" v-model="form.param6">
            <input type="text" placeholder="Price" v-model="form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
                form: {
                    type_id: null,
                    name: '',
                    param1: '',
                    param2: '',
                    param3: '',
                    param4: '',
                    param5: '',
                    param6: '',
                    param7: '',
                    price: '',
                },
                image: {},
                

            }
        },
        methods: {
        updatePhoto(e) {
            this.image = e
        },
        async sendToServer() {
            try {
                var formData = new FormData()
                formData.append('image', this.image)
                formData.append('request', JSON.stringify(this.form))
                var headers = { 'Content-Type': 'multipart/form-data' }
                await axios.post('http://localhost:8000/item/', formData, {headers: headers}).then((res) => {
                alert('good')
            })
            } catch (error) {
                alert(error)
            }
        },
        setTypeId1() {
            this.form.type_id = 1
        },
        setTypeId2() {
            this.form.type_id = 2
        },
        setTypeId3() {
            this.form.type_id = 3
        },
        setTypeId4() {
            this.form.type_id = 4
        },
        setTypeId5() {
            this.form.type_id = 5
        },
        setTypeId6() {
            this.form.type_id = 6
        },
        setTypeId7() {
            this.form.type_id = 7
        },
        setTypeId8() {
            this.form.type_id = 8
        },
        setTypeId9() {
            this.form.type_id = 9
        },
        setTypeId10() {
            this.form.type_id = 10
        },
    }
}

</script>

<style>
.choose_item {
    display: flex;
    margin-top: 20px;
    gap: 10px;
    font-size: 20px;
}

.choose_item li:hover {
    color: rgba(128, 0, 128, 0.5);
}

.send_item input {
    display: block;
    width: 300px;
    height: 40px;
    margin: 20px;
    border: 1px solid black;
}

.btn {
    height: 30px;
    margin-left: 20px;
}
</style>