<template>
    <header>
        <form @submit="onSubmit">
            <div :key="question.name" v-for="question in currentInputType.format.questions">
                <label>{{question.prompt}}&nbsp;</label>
                <input type="number" class="showValue" min="1" max="10" v-model="valueMap[question.name]" onkeydown="return event.keyCode !== 69" readonly="readonly"/>
                <br>
                <label>{{question.lowLabel}}&nbsp;</label>
                <input type="range" class="slider" min="1" max="10" step="1" v-model="valueMap[question.name]"/>
                <label>&nbsp;{{question.highLabel}}</label>
                <br><br>
            </div>

            <div class="date">
                <label>{{currentInputType.format.labels.date}}&nbsp;</label>
                <input type="date" class="dateInput" v-model="date" name="date"/>
            </div>
            &nbsp;
            <input type="submit" :value="currentInputType.format.labels.add"/>
        </form>

    </header>
</template>

<script>
    import { toRaw } from 'vue';
    export default {
        name: "Slider-Format",
        props: {
            currentInputType: Object,
            inputList: Array
        },
        data() {
            return {
                valueMap: {},
                date: (function(defaultDateOffset) {
                    var today = new Date();
                    today.setDate(today.getDate() + defaultDateOffset);
                    var dd = String(today.getDate()).padStart(2, '0');
                    var mm = String(today.getMonth() + 1).padStart(2, '0');
                    var yyyy = today.getFullYear();
                    return yyyy + '-' + mm + '-' + dd;
                })(0)
            }
        },
        created() {
            var questions = this.currentInputType.format.questions;
            for (var question in questions) {
                this.valueMap[questions[question].name] = 1;
            }
        },
        methods: {
            onSubmit(e) {
                e.preventDefault();

                const currentInputs = this.currentInputType.format.questions.map(q => q.name);
                const currentAmounts = {};
                for (var name in currentInputs) {
                    currentAmounts[currentInputs[name]] = parseInt(toRaw(this.valueMap)[currentInputs[name]]);
                }
                
                const inputData = JSON.parse(JSON.stringify({
                    inputId: this.currentInputType.id,
                    values: currentAmounts,
                    date: this.date
                }));

                this.$emit("submit-data", inputData);

                //no need to reset the input type or the date
                for (var attr in this.valueMap) {
                    this.valueMap[attr] = 1;
                }
            }
        }
    }
</script>

<style scoped>
    .showValue {
        width: 40px;
    }

    .slider {
        width: 25%;
    }

    div {
        display: inline;
    }
</style>
