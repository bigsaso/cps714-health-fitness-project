<template>
    <header>
        <h5>Sleep data chart</h5>
        <canvas id="sleepChart"></canvas>
    </header>
</template>


<script>
    import Chart from 'chart.js/auto';
    import axios from 'axios';
    import sleepData from '../../scripts/charts/SleepData';

    export default {
        name: 'SleepTrackChart',
        data() {
            return {
                sleepData: sleepData,
                avgSleep : 0,
                sum:0,
                i : 0,
                userId: null
            }
        },
        async mounted() {

   this.userId = localStorage.getItem('userId');

                 console.log("userId: " + this.userId);


            let userData = await axios.get(`http://localhost:5000/sleep_data_api/get_sleep_data/${this.userId}`).catch(function(error) {
                console.log(error);




            });

            console.log("userdata: "  + userData)
            if (userData != undefined) {
                let dataList = userData.data; //list of data for user n
                console.log("datalist: " + dataList);
                let datasets = sleepData.data.datasets;
                console.log("datasetssss: " + datasets);
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
                    let dataSendDate = new Date(packet[4]);

console.log("datasenddate: " + dataSendDate);

                    if (dataSendDate == null) {
                        continue;
                    }



      


                    let formattedDataSendDate = (dataSendDate.getUTCMonth() + 1) + "/" + dataSendDate.getUTCDate() + "/" + dataSendDate.getUTCFullYear();



console.log("listofdates: " + listOfDates);

console.log("formatteddata: " + formattedDataSendDate);

                    let index = listOfDates.indexOf(formattedDataSendDate);


  console.log("index: " + index);
  console.log("datsets: " +  packet[1]);


 
                    if (index != -1) {
                        datasets[0].data[index] += packet[1]; //sleep
                    
                       this.sum += parseFloat(packet[1]);
                       this.i++;
                       
                    }
                    console.log("packet: " + packet[1])
                    this.avgSleep = (this.sum / this.i);
                    console.log("i: " + this.i);
                }

                dateLabels[5] = "Yesterday (" + dateLabels[5] + ")";
                dateLabels[6] = "Today (" + dateLabels[6] + ")";
                sleepData.data.labels = dateLabels;
                
                console.log("avgsleep: ", this.avgSleep);
                localStorage.setItem("sleep",this.avgSleep);
            }
            const ctx = document.getElementById('sleepChart');
            new Chart(ctx, this.sleepData);
        }
    }
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
