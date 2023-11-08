export const calorieIntakeChartData = {
    type: "bar",
    data: {
      labels: ["October 23", "October 24", "October 25", "October 26", "October 27", "Yesterday", "Today"],
      datasets: [
        {
          label: "Calorie Intake (calories)",
          data: [0, 0, 0, 0, 0, 0, 0],
          borderWidth: 3
        },
        {
          label: "Fat Intake (grams)",
          data: [0, 0, 0, 0, 0, 0, 0],
          borderWidth: 3
        },
        {
          label: "Carbohydrate Intake (grams)",
          data: [0, 0, 0, 0, 0, 0, 0],
          borderWidth: 3
        },
        {
          label: "Protein Intake (grams)",
          data: [0, 0, 0, 0, 0, 0, 0],
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
  
  export default calorieIntakeChartData;