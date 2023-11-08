<script>
    import axios from 'axios';
  export default {
    data() {
      return {
        data: null,
      };
    },
    methods: {
      async fetchData() {      
       const response =  axios.get("http://127.0.0.1:5000/get_exercise/8").catch(function(error){
        console.log(error);
      });   
        this.data = await response
      },    
    },
    mounted() {
      this.fetchData();
    },
  };
</script>