<template>
    <div class="SleepChart">
      
      <h1>{{ msg }}</h1>
      <canvas id="myChart" width = "400" height = "400"></canvas>
  
    </div>
  </template>
  
  <script>
  import Chart from 'chart.js/auto';
  
  export default {
    name: 'SleepChart',
    props: {
      msg: String
    },
    mounted(){
      console.log('Component mounted.')
  
    const ctx = document.getElementById('myChart');
  
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
          datasets: [{
              label: 'Sleep Hours',
              data: [12, 8, 3, 5, 2, 3],
              backgroundColor: [
                  'rgba(71, 183,132,.5)',
    
              ],
              borderColor: [
                  '#47b784',
              ],
              borderWidth: 3
          }]
      },
  
  
      options: {
        responsive: true,
          scales: {
              yAxes: [{
                  ticks: {
                      beginAtZero: true
                  }
              }]
          }
      }
  });
  
  myChart;
  
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->

  