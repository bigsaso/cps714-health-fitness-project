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
    import axios from 'axios';
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
            async onSubmit(inputData) {console.log(inputData);
                if (inputData.inputId === 1) {
                    let result = await axios.post("http://localhost:5000/calorie_api/add_calorie_intake", {
                        user_id: 5,
                        calorie_amount: inputData.values.calories,
                        carbohydrate: inputData.values.carbs,
                        fat: inputData.values.fat,
                        protein: inputData.values.protein,
                        time: inputData.date
                    });
                    console.log(result);
                } else if (inputData.inputId === 4) {
                    let result = await axios.post("http://localhost:5000/mood_api/add_user_mood", {
                        user_id: 5,
                        mood_scale: inputData.values.happiness,
                        time: inputData.date
                    });
                    console.log(result);
                } else {
                    console.log(inputData);
                }
            }
        }
    }
</script>