<template>
<h4> Today's steps </h4>
<p>Steps: {{finalsteps}}</p>
</template>

<script>
import axios from 'axios';
export default{
    name:"todayStep",

    data(){
        return {
            finalsteps : null
        }
    },
    
    async mounted(){
    let currentuser = localStorage.getItem('userId');
    let userData = await axios.get(`http://127.0.0.1:5000/steptracker_api/get_num_steps/${currentuser}`).catch(function(error){
        console.log(error);
    });
    let dataList = userData.data;
    

    var today = new Date();
    let todayFormatted = today.toLocaleDateString();
    for(let i in dataList){
        let packet = dataList[i];
        let current = new Date(packet[3]);
        let currentCompare = (current.getUTCMonth() + 1) + "/" + current.getUTCDate() + "/" + current.getUTCFullYear();
        if(currentCompare == todayFormatted){
            this.finalsteps = packet[1];
            continue;
        }

    }
    
    
    }
}


</script>
