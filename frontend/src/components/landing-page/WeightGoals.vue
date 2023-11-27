
<template>
    <!-- Weight progress bar -->
    <div class="container">
    <div class="panel panel-default">
  <div class="class=flex-container"><p>Current progress : {{currentWeight}}lbs/{{goalWeight}}lbs</p></div>
  <p>Keep it up, your {{ weightPercentage }}% away from completing your goal!</p>
    </div>
  </div>
 


</template>

<script>
import axios from 'axios';
    export default{
        name:"currentWeight",
    
        data(){
            return {
                currentWeight : null,
                goalWeight : null,
                weightPercentage : null
                
                
            }
        },  
        computed: {
         progressBarStyle() {
          return { width: this.weightPercentage + '%' };
            },
          },
        async mounted(){
        let currentuser = localStorage.getItem('userId');
        let currentUserData = await axios.get(`http://127.0.0.1:5000/user_api/get_user_data/${currentuser}`).catch(function(error){
            console.log(error);
        });
        let currentGoals = await axios.get(`http://127.0.0.1:5000/goals_api/get_user_goals/${currentuser}`).catch(function(error){
            console.log(error);
          });

        //Getting current goals for today
        let goalsList = currentGoals.data["user_goals"];
        var today = new Date();
        let todayFormatted = today.toLocaleDateString();
        for(let i in goalsList){
            let packet = goalsList[i];
            let current = new Date(packet[4]);
            let currentCompare = (current.getUTCMonth() + 1) + "/" + current.getUTCDate() + "/" + current.getUTCFullYear();
            if(currentCompare == todayFormatted){
                this.goalWeight = packet[1];
                continue;
            }
         }

        //Getting current weight of today
        let weightList = currentUserData["data"]["user_data"][0][2];
        this.currentWeight = weightList
        
        if(this.currentWeight<this.goalWeight){
          let progressCalc = Math.round((this.currentWeight/this.goalWeight)*100);
          this.weightPercentage = progressCalc
          console.log(this.weightPercentage);
        }
        else if(this.currentWeight>this.goalWeight){
          let progressCalc = Math.round(((this.currentWeight-this.goalWeight)/this.currentWeight)*100);
          this.weightPercentage = progressCalc
        }
        else{
          this.weightPercentage = 0;
        }
        
    }
  }
</script>