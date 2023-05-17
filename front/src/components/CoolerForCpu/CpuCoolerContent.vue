!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;" >
        <cpu-cooler-item :cpu_cooler_item="cpu_cooler_item" v-for="cpu_cooler_item in cpu_cooler_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import CpuCoolerItem from '@/components/CoolerForCpu/CpuCoolerItem.vue';
    export default {
        components: {
            CpuCoolerItem
        },
        data() {
            return {
                cpu_cooler_items: []
            }
        },
        methods:{
            async fetchCpuCooler() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=7').then((res) => {
                    this.cpu_cooler_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchCpuCooler()
        }
}
</script>

<style>

</style>