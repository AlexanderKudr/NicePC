!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <thermal-item :thermal_item="thermal_item" v-for="thermal_item in thermal_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import ThermalItem from './ThermalItem.vue';
    export default {
        components: {
            ThermalItem
        },
        data() {
            return {
                thermal_items: []
            }
        },
        methods:{
            async fetchThermal() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=9').then((res) => {
                    this.thermal_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchThermal()
        }
}
</script>

<style>

</style>