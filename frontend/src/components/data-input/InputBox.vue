<template>
    <header>
        <div v-if="currentInputType.format.type === 'SimpleInputFormat'">
            <SimpleInputFormat @submit-data="onSubmit" :currentInputType="currentInputType" :inputList="inputList"/>
        </div>
        <div v-else-if="currentInputType.format.type === 'SliderFormat'">
            <SliderFormat @submit-data="onSubmit" :currentInputType="currentInputType" :inputList="inputList"/>
        </div>
    </header>
</template>

<script>
    import SimpleInputFormat from './SimpleInputFormat';
    import SliderFormat from './SliderFormat';
    export default {
        name: 'Input-Box',
        props: {
            currentInputType: Object,
            inputList: Array
        },
        components: {
            SimpleInputFormat,
            SliderFormat
        },
        data() {
            return {
                inputData: Object
            }
        },
        methods: {
            onSubmit(inputData) {
                console.log(inputData); //send to backend when it is implemented
            }
        }
    }
</script>