!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <case-cooler-item :case_cooler_item="case_cooler_item" v-for="case_cooler_item in case_cooler_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import CaseCoolerItem from '@/components/CoolerForCase/CaseCoolerItem.vue';
    export default {
        components: {
            CaseCoolerItem
        },
        data() {
            return {
                case_cooler_items: []
            }
        },
        methods:{
            async fetchCaseCooler() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=8').then((res) => {
                    this.case_cooler_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchCaseCooler()
        }
}
</script>

<style>

</style>