!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <motherboard-item :motherboard_item="motherboard_item" v-for="motherboard_item in motherboard_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import MotherboardItem from '@/components/Motherboard/MotherboardItem.vue';
    export default {
        components: {
            MotherboardItem
        },
        data() {
            return {
                motherboard_items: []
            }
        },
        methods:{
            async fetchMotherboard() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=6').then((res) => {
                    this.motherboard_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchMotherboard()
        }
}
</script>

<style>

</style>