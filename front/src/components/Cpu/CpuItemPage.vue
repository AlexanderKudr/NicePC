<template>
    <div class="page">
        {{ this.info }}
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            path: 'http://127.0.0.1:8000/',
            info: []
        }  
    },
    methods: {  
        async fetchThisCpuInfo() {
            await axios.get(`http://127.0.0.1:8000/item/one?item_id=${this.$route.params.id}`)
            .then((res) => {
                if (res.status === 200) {
                    this.info = res.data
                }
            })
        }
    },
    beforeMount() {
        this.fetchThisCpuInfo()
    }
}
</script>

<style>
.page {
    margin-top: 100px;
    font-size: 20px;
}
</style>