!<template>
    <div style="overflow-y: auto;">
        <prebuilt-item :prebuilt_item="prebuilt_item" v-for="prebuilt_item in prebuilt_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import PrebuiltItem from '@/components/PrebuiltPC/PrebuiltItem.vue';
    export default {
        components: {
            PrebuiltItem
        },
        data() {
            return {
                prebuilt_items: []
            }
        },
        methods:{
            async fetchPrebuilt() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=10').then((res) => {
                    this.prebuilt_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchPrebuilt()
        }
}
</script>

<style>

</style>