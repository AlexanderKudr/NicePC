!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <ram-item :ram_item="ram_item" v-for="ram_item in ram_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import RamItem from './RamItem.vue';
    export default {
        components: {
            RamItem
        },
        data() {
            return {
                ram_items: []
            }
        },
        methods:{
            async fetchRam() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=2').then((res) => {
                    this.ram_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchRam()
        }
}
</script>

<style>

</style>