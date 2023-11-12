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
            <a class="nav-link" href="/dashboard"><span class="mb-1 h4">Share</span></a>
        </li>

        <li class="nav-item">
          <div class = "top-buffer"></div>
            <a class="nav-link" href="/"><span class="mb-1 h4">Logout</span></a>
        </li>
      </ul>
    </div>
    
  

    
    <div class="col-sm-9">
      <div class="well">
        <h4>Dashboard</h4>
        <p>Welcome back user!</p>
      </div>
    <div>
      <h3> 
        Weight progress
      </h3>

    </div>
  
      <!-- Weight progress bar -->
      <div class="progress" style="height:30px">
        <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="90"
        aria-valuemin="0" aria-valuemax="100" style="width:88%">
          160lb / 180 lb goal
        </div>
      </div>
    
  

      <div class="container-fluid ">
            <div class = "row">

              <!-- Today's steps data -->
              <div class = "col border">
                
                <todayStep />
              </div>

              <!-- Current calorie data -->
              <div class = "col border">
                <h4>Today's calorie goal</h4>
                <p>2500 cal</p> 
              </div>

              <!-- Sleep average data -->
              <div class = "col border">
                <h4>Hours slept average</h4>
                <p>7 hr</p> 
              </div>

              <!-- Macronutrient data  -->
              <div class = "col border">
                <todayMacros />
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
            <div class = "row">
                <div class = top-buffer></div>
                <div class =chart-wrapper>
                  <CalorieIntakeChart/>
                </div>
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
//import SleepChart from '../charts/SleepTrackChart.vue';
import CalorieIntakeChart from '../charts/CalorieIntakeChart.vue';
import todayMacros from './TodayMacros.vue';
import todayStep from './TodaySteps.vue';

export default{

    name:'MyLanding', 
    components:{
      
      DailyStepsChart,
      todayStep,
      CalorieIntakeChart,
      todayMacros
    },

    
    data(){
      return{
        steps : [],
        workoutlist : [],
     
      };
    },
    async mounted(){
      
      //let workoutdata = await axios.get("http://127.0.0.1:5000/get_exercise/8").catch(function(error){
      //  console.log(error);
      //});
      //let stepsdata = await axios.get("http://127.0.0.1:5000/steptracker_api/get_num_steps/8").catch(function(error){
      //  console.log(error);
      //});

      //Userid is hard coded for now, when testing change last digit on link with userid
      let currentuser = 9;
      
      axios.get(`http://127.0.0.1:5000/steptracker_api/get_num_steps/${currentuser}`).then(response => this.steps = response.data)

      axios.get(`http://127.0.0.1:5000/get_exercise/${currentuser}`).then(response => this.workoutlist = response.data)
      
      
       var today = new Date();
       console.log(today);


      

    },

    create(){
      this.mounted();
    }
} 

</script> 

<style scoped>
.row.content {height: 550px}

.sidenav {
  background-color: #f1f1f1;
  height: 100%;
}

.chart-wrapper {
 
  height: 300px;
  width: 600px;
}

.top-buffer{margin-top:20px;}

.tab {
        tab-size: 4;
    }
</style>