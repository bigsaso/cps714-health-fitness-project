<template>
    <h4> Today's Macronutrients </h4>
    <p>Carbs :{{finalcarbs}} g</p>
    <p>Fat :{{finalfat}} g</p>
    <p>Protein:{{finalprotein}} g</p>
    </template>
    
    <script>
    import axios from 'axios';
    export default{
        name:"todayMacros",
    
        data(){
            return {
                finalcarbs : 0,
                finalfat : 0,
                finalprotein : 0
            }
        },
        
        async mounted(){
        let currentuser = localStorage.getItem('userId');
        let userData = await axios.get(`http://127.0.0.1:5000/calorie_api/get_calorie_intake/${currentuser}`).catch(function(error){
            console.log(error);
        });
        let dataList = userData.data;
        
    
        var today = new Date();
        let todayFormatted = today.toLocaleDateString();
        for(let i in dataList){
            let packet = dataList[i];
            let current = new Date(packet[6]);
            let currentCompare = (current.getUTCMonth() + 1) + "/" + current.getUTCDate() + "/" + current.getUTCFullYear();
            if(currentCompare == todayFormatted){
                this.finalcarbs = packet[2];
                this.finalfat = packet[3];
                this.finalprotein = packet[4];
                continue;
            }
            

    
        }
        
        
        }
    }
    
    </script>
    