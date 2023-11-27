<template>
    <header>
        <h5>Mood chart</h5>
        <h6>Your mood over the past week</h6>
        <canvas id="moodChart"></canvas>
    </header>
</template>

<script>
    import Chart from 'chart.js/auto';
    import axios from 'axios';
    import moodChartData from '../../scripts/charts/MoodChartData';

    export default {
        name: 'moodChart',
        data() {
            return {
                moodChartData: moodChartData
            }
        },
        async mounted() {
            let currentuser = localStorage.getItem('userId');
            let userData = await axios.get(`http://localhost:5000/mood_api/get_user_mood/${currentuser}`).catch(function(error) {
                console.log(error);
            });
            if (userData != undefined) {
                let dataList = userData.data["user_mood"]; //list of data for user n
                let datasets = moodChartData.data.datasets;
                datasets[0].data = [0, 0, 0, 0, 0, 0, 0];
                datasets[1].data = [0, 0, 0, 0, 0, 0, 0];

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
                    let dataSendDate = new Date(packet[4]);
                    if (dataSendDate == null) {
                        continue;
                    }
                    let formattedDataSendDate = (dataSendDate.getUTCMonth() + 1) + "/" + dataSendDate.getUTCDate() + "/" + dataSendDate.getUTCFullYear();
                    let index = listOfDates.indexOf(formattedDataSendDate);
                    if (index != -1) {
                        datasets[0].data[index] = packet[1]; //happiness
                        datasets[1].data[index] = packet[2]; //motivation
                    }
                }

                dateLabels[5] = "Yesterday (" + dateLabels[5] + ")";
                dateLabels[6] = "Today (" + dateLabels[6] + ")";
                moodChartData.data.labels = dateLabels;
            }
            const ctx = document.getElementById('moodChart');
            new Chart(ctx, this.moodChartData);
        }
    }
</script>
