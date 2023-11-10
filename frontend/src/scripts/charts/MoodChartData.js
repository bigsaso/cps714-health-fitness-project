export const moodChartData = {
    type: "line",
    data: {
      labels: ["October 23", "October 24", "October 25", "October 26", "October 27", "Yesterday", "Today"],
      datasets: [
        {
          label: "Happiness",
          data: [0, 0, 0, 0, 0, 0, 0],
          borderWidth: 3
        },
        {
          label: "Motivation",
          data: [0, 0, 0, 0, 0, 0, 0],
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 0,
      scales: {
        y: {
            suggestedMin: 0,
            suggestedMax: 10
        },
        yAxis: [
          {
            ticks: {
                padding: 25,
            },
          }
        ]
      }
    }
  };
  
  export default moodChartData;