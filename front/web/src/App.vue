<template>
    <div>
        <form @submit.prevent class="send_cpu">
            <input type="text" placeholder="Name" v-model="cpu_form.name">
            <input type="text" placeholder="Core" v-model="cpu_form.core">
            <input type="text" placeholder="Cpu clock" v-model="cpu_form.cpu_clock">
            <input type="text" placeholder="Socket" v-model="cpu_form.socket">
            <input type="text" placeholder="Threads" v-model="cpu_form.threads">
            <input type="text" placeholder="Tdp" v-model="cpu_form.tdp">
            <input type="text" placeholder="Nm" v-model="cpu_form.nm">
            <input type="text" placeholder="Price" v-model="cpu_form.price">
            <label for="file" style="margin-left: 20px;">Choose picture</label>
            <input type="file" @change="updatePhoto($event.target.files[0])" accept="image/*">
            <button @click="sendToServer" class="btn">Отправить</button>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                cpu_form: {
                    name: '',
                    core: '',
                    cpu_clock: '',
                    socket: '',
                    threads: '',
                    tdp: '',
                    nm: '',
                    price: '',
                },
                image: ''

            }
        },
        methods: {
        updatePhoto(e) {
            this.image = e
        },
        async sendToServer() {
            console.log(this.cpu_form)
            console.log(this.image)
            try {
                await axios.post('http://localhost:8000/cpu_item/', this.cpu_form, this.image).then((res) => {
                console.log(res)
            })
            } catch (error) {
                alert('Error while posting to API')
            }
        }
    }
}

</script>

<style>
.send_cpu input {
    display: block;
    width: 300px;
    height: 40px;
    margin: 20px;
}

.btn {
    height: 30px;
    margin-left: 20px;
}
</style>