<template>
    <header>
        <div :key="input.id" v-for="input in inputs">
            <InputChoice @open-input-box="$emit('open-input-box', input.id)" :input="input"/>
        </div>
    </header>
</template>

<script>
    import InputChoice from './InputChoice'
    export default {
        name: 'Input-Choices',
        props: {
            inputs: Array
        },
        components: {
            InputChoice
        },
        emits: [
            'open-input-box'
        ]
    }
</script>

<style scoped>
    * {
        display: inline;
    }
</style>