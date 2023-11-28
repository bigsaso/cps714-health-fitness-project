<template>
<h4> Avg Sleep:</h4>
<p>Hours: {{finalsleep}}</p>
</template>

<script>
import axios from 'axios';
export default{
    name:"todayStep",

    data(){
        return {
            total : 0,
            count:0,
            finalsleep: 0
        }
    },
    
    async mounted(){
    let currentuser = localStorage.getItem('userId');
    let userData = await axios.get(`http://127.0.0.1:5000/sleep_data_api/get_sleep_data/${currentuser}`).catch(function(error){
        console.log(error);
    });
    let dataList = userData.data;
console.log("datalist: " + dataList);

    for(let i in dataList){
        let packet = dataList[i];
        console.log("packet date: " + packet[4]);
              this.count++;
            this.total += parseFloat(packet[1]);
            console.log("finalsteps: " + this.finalsteps);
        

    }
    this.finalsleep = (this.total / this.count).toFixed(2);
    
    }
}


</script>