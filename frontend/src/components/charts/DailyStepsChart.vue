<template>
    <div>
      <h6>Your steps over the past week</h6>
      <canvas id="daily-steps"></canvas>
    </div>
  </template>
  

  <script>
  import Chart from 'chart.js/auto';
  import axios from 'axios';
  import dailyStepsData from '../../scripts/charts/DailySteps-data.js';
  
  export default {
    name: 'DailyStepsChart',
    data() {
        return{
            dailyStepsData: dailyStepsData
        }
    },
    async mounted() {
        let currentuser = 9;
        let userData = await axios.get(`http://localhost:5000/steptracker_api/get_num_steps/${currentuser}`).catch(function(error){
          console.log(error);
        });
        if (userData != undefined) {
                let dataList = userData.data; //list of data for user n
                let datasets = dailyStepsData.data.datasets;
                datasets[0].data = [0, 0, 0, 0, 0, 0, 0];

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
                    let dataSendDate = new Date(packet[3]);
                    if (dataSendDate == null) {
                        continue;
                    }
                    let formattedDataSendDate = (dataSendDate.getUTCMonth() + 1) + "/" + dataSendDate.getUTCDate() + "/" + dataSendDate.getUTCFullYear();
                    let index = listOfDates.indexOf(formattedDataSendDate);
                    if (index != -1) {
                        datasets[0].data[index] += packet[1]; //Number of steps
                    }
                }

                dateLabels[5] = "Yesterday (" + dateLabels[5] + ")";
                dateLabels[6] = "Today (" + dateLabels[6] + ")";
                dailyStepsData.data.labels = dateLabels;
            }

        const ctx = document.getElementById('daily-steps');
        new Chart(ctx,this.dailyStepsData);
    }
  }
  </script>