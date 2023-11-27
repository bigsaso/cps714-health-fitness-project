<template>
    <header>
        <h5>Calorie Intake chart</h5>
        <h6>Your calorie, fat, carb, and protein intake over the past week</h6>
        <canvas id="calorieChart"></canvas>
    </header>
</template>

<script>
    import Chart from 'chart.js/auto';
    import axios from 'axios';
    import calorieIntakeChartData from '../../scripts/charts/CalorieIntakeChartData';

    export default {
        name: 'CalorieIntakeChart',
        data() {
            return {
                calorieIntakeChartData: calorieIntakeChartData
            }
        },
        async mounted() {
            let currentuser = localStorage.getItem('userId');
            let userData = await axios.get(`http://localhost:5000/calorie_api/get_calorie_intake/${currentuser}`).catch(function(error) {
                console.log(error);
            });
            if (userData != undefined) {
                let dataList = userData.data; //list of data for user n
                let datasets = calorieIntakeChartData.data.datasets;
                datasets[0].data = [0, 0, 0, 0, 0, 0, 0];
                datasets[1].data = [0, 0, 0, 0, 0, 0, 0];
                datasets[2].data = [0, 0, 0, 0, 0, 0, 0];
                datasets[3].data = [0, 0, 0, 0, 0, 0, 0];

                Date.prototype.subtractDays = function(days) {
                    var date = new Date(this.valueOf());
                    date.setDate(date.getDate() - days);
                    return date;
                }

                var today = new Date();
                let listOfDates = [];
                let dateLabels = [];
                for (let i = 0; i < 7; i++) {
                    let dayToUse = today.subtractDays(i);
                    listOfDates[7 - 1 - i] = dayToUse.toLocaleDateString();
                    dateLabels[7 - 1 - i] = dayToUse.toLocaleString('default', { month: 'long', day: 'numeric' })
                }

                for (let i in dataList) {
                    let packet = dataList[i];
                    let dataSendDate = new Date(packet[6]);
                    if (dataSendDate == null) {
                        continue;
                    }
                    let formattedDataSendDate = (dataSendDate.getUTCMonth() + 1) + "/" + dataSendDate.getUTCDate() + "/" + dataSendDate.getUTCFullYear();
                    let index = listOfDates.indexOf(formattedDataSendDate);
                    if (index != -1) {
                        datasets[0].data[index] += packet[1]; //calories
                        datasets[1].data[index] += packet[3]; //fat
                        datasets[2].data[index] += packet[2]; //carbs
                        datasets[3].data[index] += packet[4]; //protein
                    }
                }

                dateLabels[5] = "Yesterday (" + dateLabels[5] + ")";
                dateLabels[6] = "Today (" + dateLabels[6] + ")";
                calorieIntakeChartData.data.labels = dateLabels;
            }
            const ctx = document.getElementById('calorieChart');
            new Chart(ctx, this.calorieIntakeChartData);
        }
    }
</script>
