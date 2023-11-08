export const dailyStepsData = {
    type: "line",
    data: {
      labels: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      datasets: [
        {
          label: "Steps Progress",
          data: [10000,9000,8800,4000,6700,5000,4300],
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