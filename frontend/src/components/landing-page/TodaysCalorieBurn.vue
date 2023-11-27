<template>
    <h4>Today's calorie goal</h4>
    <p>{{calBurned}} calories</p>
    </template>
    
    <script>
    import axios from 'axios';
    export default{
        name:"todayCalBurned",
    
        data(){
            return {
                calBurned : 0,
            }
        },
        
        async mounted(){
        let currentuser = localStorage.getItem('userId');
        let userData = await axios.get(`http://127.0.0.1:5000/goals_api/get_user_goals/${currentuser}`).catch(function(error){
            console.log(error);
        });
        let dataList = userData.data["user_goals"];
        
    
        var today = new Date();
        let todayFormatted = today.toLocaleDateString();
        for(let i in dataList){
            let packet = dataList[i];
            let current = new Date(packet[4]);
            let currentCompare = (current.getUTCMonth() + 1) + "/" + current.getUTCDate() + "/" + current.getUTCFullYear();
            if(currentCompare == todayFormatted){
                this.calBurned = packet[2];
                continue;
            }
            

    
        }
        
        
        }
    }
    
    </script>
    