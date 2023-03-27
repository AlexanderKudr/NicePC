<template>
    <div class="dialog" v-if="show" @click="hideDialog">
        <div @click.stop class="dialog__content">
            <slot/>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'my-login',
        props: {
            show: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            hideDialog() {
                this.$emit('update:show', false)
            }
        }
    }
</script>

<style scoped>
.dialog {
    left: 0;
    top: 0;
    bottom: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.5);
    position: fixed;
    display: flex;
    z-index: 2;
}
.dialog__content {
    margin: auto;
    background: white;
    border-radius: 12px;
    min-height: 460px;
    min-width: 480px;
    padding: 20px;

}


</style>