!<template>
    <div style="overflow-y: auto; margin-bottom: 100px;">
        <case-item :case_item="case_item" v-for="case_item in case_items"/>
    </div>
</template>

<script>
import axios from 'axios';
import CaseItem from '@/components/Case/CaseItem.vue';
    export default {
        components: {
            CaseItem
        },
        data() {
            return {
                case_items: []
            }
        },
        methods:{
            async fetchCase() {
                try {
                    await axios.get('http://localhost:8000/item/?type_id=5').then((res) => {
                    this.case_items = res.data
                    })
                } 
                catch (error) {
                    alert('Error while posting to API')
                }
            }
        },
        beforeMount() {
            this.fetchCase()
        }
}
</script>

<style>

</style>