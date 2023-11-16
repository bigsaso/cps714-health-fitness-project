export const sleepData = {
    type: 'bar',
    data: {
        labels: ["October 23", "October 24", "October 25", "October 26", "October 27", "Yesterday", "Today"],
        datasets: [{
            label: 'Sleep Hours',
            data: [0,0,0,0,0,0,0],
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
        lineTension: 1,
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                padding: 25
              }
            }
          ]
        }
      }
    };







export default sleepData;

