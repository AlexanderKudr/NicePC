!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <psu-item :psu_item="psu_item" v-for="psu_item in psu_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import PsuItem from '@/components/PowerSupply/PsuItem.vue';
    export default {
        components: {
            PsuItem
        },
        data() {
            return {
                psu_items: []
            }
        },
        methods:{
            async fetchPsu() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=4').then((res) => {
                    this.psu_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchPsu()
        }
}
</script>

<style>

</style>