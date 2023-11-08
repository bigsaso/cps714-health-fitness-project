<template>
    <header>
        <p>What would you like to input?</p>
        <InputChoices @open-input-box="openInputBox" :inputs="inputs"/>
        <br><br><br><br>
        <InputBox :currentInputType="currentInputType" :inputList="inputs"/>
    </header>
</template>

<script>
    import InputChoices from './InputChoices'
    import InputBox from './InputBox'

    export default {
        name: 'Data-Input-Page',
        components: {
            InputChoices,
            InputBox
        },
        data() {
            return {
                inputs: [],
                currentInputType: Object
            }
        },
        methods: {
            openInputBox(id) {
                this.currentInputType = (this.inputs.filter((input) => input.id === id))[0];
            }
        },
        created() {
            this.inputs = require('../../config/inputs.json');
            this.currentInputType = this.inputs[0];
        }
    }
</script>

<style scoped>
    header {
        line-height: 1.5;
    }
</style>