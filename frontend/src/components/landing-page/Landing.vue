<template>
<head>
  <title>Fitness home</title>

</head>

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav hidden-xs">
      <h2>Welcome</h2>

      <!-- Dashboard links -->
      <ul class="nav flex-column">
        <li class="nav-item">
          <div class = "top-buffer"></div>
           <a class="nav-link" href="/update-progress"><span class="mb-1 h4">Update Progress</span></a>
        </li>

        <li class="nav-item">
          <div class = "top-buffer"></div>
            <a class="nav-link" href="/dashboard"><span class="mb-1 h4">See Progress</span></a>
        </li>

        <li class="nav-item">
          <div class = "top-buffer"></div>
            <a class="nav-link" href="/edit-profile"><span class="mb-1 h4">Edit Profile</span></a>
        </li>

        
          <div class = "top-buffer"></div>
            <shareNetworks />
      

        <li class="nav-item">
          <div class = "top-buffer"></div>
            <a class="nav-link" href="/"><span class="mb-1 h4">Logout</span></a>
        </li>
      </ul>
    </div>
    
    
    <div class="col-sm-9">
      
      <div class="well">
        <h4>Dashboard</h4>
        
        <h2>Welcome back {{currentName}}</h2>
      </div>
    <div>
      <div class = "top-buffer"></div>
      <h3> 
        Weight progress
      </h3>

    </div>
  
      <!-- Weight progress bar -->
       <currentWeight/>
      <div class = "top-buffer"></div>
    
  

      <div class="container-fluid ">
        <div class ="background-heading">
            <div class = "row">
              

              <!-- Today's steps data -->
              <div class = "col border">
                
                <todayStep />
              </div>

              <!-- Current calorie data -->
              <div class = "col border">
                
                <todayCalBurned />
              </div>

              <!-- Sleep average data -->
              <div class = "col border">
                <h4>Hours slept average</h4>
                <p>{{this.averageSleep}} hours</p>
              </div>

              <!-- Macronutrient data  -->
              <div class = "col border">
                <todayMacros />
              </div>
              </div>
              
            </div>
            <!-- Daily steps chart -->
            <div class = row>
                <div class = "col border">
                  <div class =chart-wrapper>

                    <DailyStepsChart/>
              
                  </div>
                </div>
                <!-- Workout table  -->
                <div class = "col border">
                  <table class="table">
                    <thead class="thead-dark">
                      <tr>
                        <th scope="col">Exercise</th>
                        <th scope="col">Sets</th>
                        <th scope="col">Reps</th>
                      </tr>
                      <tr v-for="item in workoutlist" v-bind:key = "item.id">
                        
                          <td>{{ item[4] }}</td>
                          <td>{{ item[2] }}</td>
                          <td>{{ item[1] }}</td>
                      </tr>

                    </thead>

                  </table>

                </div>
              </div>
            <!-- Need to fix sleep chart formatting -->
            <div class = "row ">
                <div class = top-buffer></div>
                
                <div class =chart-wrapper pull-left >
                  <div class = "col" >
                    <CalorieIntakeChart/>
                  </div>
                </div>

                <div class = top-buffer></div>
                <div class = "col">
                  <div class =chart-wrapper pull-left>
                    <moodChart />
                  </div>
                </div>
              </div>

      </div>

    <div class = "row">
                <div class =chart-wrapper>
                  <SleepTrackChart/>
                </div>
            </div>
      

    </div>
  </div>
    

</div>

<body></body>

        
  
</template>

  


<script>
import axios from 'axios';
import DailyStepsChart from '../charts/DailyStepsChart.vue';
import SleepTrackChart from '../charts/SleepTrackChart.vue';
import CalorieIntakeChart from '../charts/CalorieIntakeChart.vue';
import moodChart from '../charts/MoodChart.vue';
import todayMacros from './TodayMacros.vue';
import todayStep from './TodaySteps.vue';
import todayCalBurned from './TodaysCalorieBurn.vue';
import shareNetworks from './ShareNet.vue';
import currentWeight from './WeightGoals.vue';


export default{

    name:'MyLanding', 
    components:{
      
      DailyStepsChart,
      todayStep,
      CalorieIntakeChart,
      todayMacros,
      todayCalBurned,
      SleepTrackChart,
      moodChart,
      shareNetworks,
      currentWeight
    },

    
    data(){
      return{
        steps : [],
        workoutlist : [],
        averageSleep: 0, // Add this property to store the average sleep data
        currentName : '',

      };
    },

 created() {
    // Dynamically import Bootstrap only when this component is created
    import('bootstrap/dist/css/bootstrap.min.css')
      .then(() => {
        console.log('Bootstrap has been imported for MyLanding.vue');
      })
      .catch((error) => {
        console.error('Error importing Bootstrap:', error);
      });
  },

    async mounted(){

      let currentuser = localStorage.getItem('userId');
      this.currentName = localStorage.getItem('firstName');

      this.averageSleep = localStorage.getItem('sleep');

      axios.get(`http://127.0.0.1:5000/get_exercise/${currentuser}`).then(response => this.workoutlist = response.data)
      
      
     

    },
    


    create(){
      this.mounted();
    },
    
} 

</script> 

<style scoped>
.row.content {height: 550px}

.sidenav {
  background-color: #f1f1f1;
  height: 100%;
}

.chart-wrapper {
 
  height: 400px;
  width: 600px;
  border: 1px solid #ddd;
}

.top-buffer{margin-top:40px;}

.tab {
        tab-size: 4;
    }

.background-heading {
background-color: lightblue; /* Use your preferred color code */
}

</style>