!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <videocard-item :videocard_item="videocard_item" v-for="videocard_item in videocard_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import VideocardItem from './VideocardItem.vue';
    export default {
        components: {
            VideocardItem
        },
        data() {
            return {
                videocard_items: []
            }
        },
        methods:{
            async fetchVideocard() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=3').then((res) => {
                    this.videocard_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchVideocard()
        }
}
</script>

<style>

</style>