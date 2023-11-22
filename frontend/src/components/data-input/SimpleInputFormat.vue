<template>
    <header>
        <form @submit="onSubmit">
            <div :key="question.name" v-for="question in currentInputType.format.questions">
                <label>{{question.prompt}}&nbsp;</label>
                <div v-if="question.inputType === 'text'">
                    <input type="text" class="textInput inputBox" v-model="amounts[question.name]" name="amount" required/>
                </div>
                <div v-else>
                    <input type="number" class="numInput inputBox" v-model="amounts[question.name]" name="amount" min="0" :max="question.max" :step="question.step" onkeydown="return event.keyCode !== 69" required/>
                </div>
                <label>&nbsp;{{question.unit}}</label>
                <br>
            </div>
            <br>

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
        name: 'Simple-Input-Format',
        props: {
            currentInputType: Object,
            inputList: Array
        },
        data() {
            return {
                inputId: String,
                amounts: {},
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
            for (var input in this.inputList) {
                var questions = this.inputList[input].format.questions;
                for (var question in questions) {
                    if (questions[question].inputType === "number") {
                        this.amounts[questions[question].name] = 0;
                    }
                }
            }
        },
        methods: {
            onSubmit(e) {
                e.preventDefault();

                const currentInputs = this.currentInputType.format.questions.map(q => q.name);
                const currentAmounts = {};
                for (var name in currentInputs) {
                    currentAmounts[currentInputs[name]] = toRaw(this.amounts)[currentInputs[name]];
                }
                
                const inputData = JSON.parse(JSON.stringify({
                    inputId: this.currentInputType.id,
                    values: currentAmounts,
                    date: this.date
                }));

                this.$emit("submit-data", inputData);

                //no need to reset the input type or the date
                for (var attr in this.amounts) {
                    if (typeof this.amounts[attr] === "string") {
                        this.amounts[attr] = "";
                    } else {
                        this.amounts[attr] = 0;
                    }
                }
            }
        }
    }
</script>

<style scoped>
    div {
        display: inline;
    }

    .inputBox {
        display: inline;
        min-width: 200px;
    }
</style>