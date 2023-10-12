<template>
    <header>
        <button @click="onClick(input.id)">{{input.type}}</button>
    </header>
</template>

<script>
    export default {
        name: 'Input-Choice',
        props: {
            input: Object
        },
        methods: {
            onClick(id) {
                this.$emit('open-input-box', id)
            }
        }
    }
</script>