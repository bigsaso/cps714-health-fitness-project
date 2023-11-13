export const dailyStepsData = {
    type: "line",
    data: {
      labels: ["October 23", "October 24", "October 25", "October 26", "October 27", "Yesterday", "Today"],
      datasets: [
        {
          label: "Steps Progress",
          data: [0,0,0,0,0,0,0],
          backgroundColor: "rgba(54,73,93,.5)",
          borderColor: "#36495d",
          borderWidth: 3
        }
      ]
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
  
  export default dailyStepsData;