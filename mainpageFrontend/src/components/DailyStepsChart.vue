<template>
    <div>
      <canvas id="daily-steps"></canvas>
    </div>
  </template>
  

  <script>
  import Chart from 'chart.js/auto'
  import dailyStepsData from '../DailySteps-data.js'
  
  export default {
    name: 'DailyStepsChart',
    data(){
        return{
            dailyStepsData: dailyStepsData
        }
    },
    mounted(){
        const ctx = document.getElementById('daily-steps');
        new Chart(ctx,this.dailyStepsData);
    }
  }
  </script>