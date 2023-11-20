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
                inputData: Object,
                userId: null
            }
        },
        methods: {
            async onSubmit(inputData) {
                var result;
                this.userId = localStorage.getItem('userId');

                switch (inputData.inputId) {
                    case 0: //steps
                        result = await axios.post("http://localhost:5000/steptracker_api/add_num_steps", {
                            userId: this.userId,
                            numSteps: inputData.values.steps,
                            time: inputData.date
                        });
                        break;
                    case 1: //calorie intake
                        result = await axios.post("http://localhost:5000/calorie_api/add_calorie_intake", {
                            userId: this.userId,
                            calorie_amount: inputData.values.calories,
                            carbohydrate: inputData.values.carbs,
                            fat: inputData.values.fat,
                            protein: inputData.values.protein,
                            date: inputData.date
                        });
                        break;
                    case 2: //sleep
                        result = await axios.post("http://localhost:5000/sleep_data_api/add_sleep_data", {
                            userId: this.userId,
                            hoursSlept: inputData.values.hoursOfSleep,
                            numDaysTracked: 1,
                            date: inputData.date
                        });
                        break;
                    case 3: //exercise
                        result = await axios.post("http://localhost:5000/add_exercise", {
                            inputId: this.userId,
                            reps: inputData.values.reps,
                            sets: inputData.values.sets,
                            name: inputData.values.name,
                            date: inputData.date
                        });
                        break;
                    case 4: //mood
                        result = await axios.post("http://localhost:5000/mood_api/add_user_mood", {
                            user_id: this.userId,
                            user_happiness: inputData.values.happiness,
                            user_motivation: inputData.values.motivation,
                            date: inputData.date
                        });
                        break;
                    case 5: //goals
                        result = await axios.post("http://localhost:5000/goals_api/add_user_goals", {
                            user_id: this.userId,
                            weight_goal: inputData.values.weightGoal,
                            daily_calorie_burn: inputData.values.calorieGoal,
                            date: inputData.date
                        });
                        break;
                    default:
                        console.log("Invalid input ID " + inputData.inputId + ". Nothing was updated");
                }
                
                console.log(result);
            }
        }
    }
</script>

<style scoped>
    div {
        display: inline;
    }

    input {
        display: inline;
    }
</style>