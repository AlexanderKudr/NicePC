!<template>
    <div>
        <cpu-item :cpu_item="cpu_item" v-for="cpu_item in cpu_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import CpuItem from './CpuItem.vue';
    export default {
        components: {
            CpuItem
        },
        data() {
            return {
                cpu_items: []
            }
        },
        methods:{
            async fetchCpu() {
                try {
                    await axios.get('http://127.0.0.1:8000/cpu_item/').then((res) => {
                    this.cpu_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchCpu()
        }
}
</script>

<style>

</style>