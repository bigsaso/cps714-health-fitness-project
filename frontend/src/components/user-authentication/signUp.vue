<template>




  <div class="container">
    <div class ="form-box">
        <h1 ref="title">Sign Up</h1>

  <div v-if="fieldCheck">
        <!-- Display the field check error message if it exists -->
        <h2>{{ fieldCheck }}</h2>
      </div>

           <div v-else-if="posts"> <!-- Display response data if it exists -->
        <h2>{{ posts.message }}</h2>
      </div>

      <div v-else-if="errorData"> <!-- Display error response code if it exists -->
        <h2>{{ errorData.error }}</h2>
      </div>
        
 
        <form @submit.prevent="handleSubmit" > 
       

            <div class = "input-group">

                <div class="input-field" >
                    <input type = "text" v-model = "first_name" placeholder = "First-Name" > 
                </div>

                  <div class="input-field" >
                    <input type = "text" v-model = "last_name" placeholder = "Last-Name" > 
                </div>

  
                <div class="input-field">
                    <input type = "email" v-model = "email" placeholder = "Email"> 
               
                </div>

                <div class="input-field">
                    <input type = "password"  v-model = "password"  placeholder = "Password"> 
                </div>



                
            </div>
        <div class = "btn-field">
                <button class= "invert" id="signupBtn" @click="signUp = !signUp">Sign up</button>
      
             
                </div>
         


 


        </form>


    </div>

</div>






</template>

<script>

import axios from 'axios'
import { generateSalt, getHashedPassword } from './hash';

  export default {
      name: 'signUp',

data(){

return {

first_name: '',
last_name : '',
email: '',
password: '',
salt: '',
posts: null,
errorData: null,
fieldCheck : null



 
}


},





methods:{
 async handleSubmit(){

let salt = generateSalt();

 if (!this.first_name || !this.last_name || !this.email || !this.password) {
      // Display an error message or handle the empty fields as needed
      this.fieldCheck = "All fields must be filled.";
      return;
    }

     if (this.password.length < 8) {
      this.fieldCheck = "Password must be at least 8 characters long.";
      return;
    }


const data = {
first_name: this.first_name,
last_name : this.last_name,
email: this.email,
password: getHashedPassword(this.password, salt),
salt: salt
};





axios
          .post('http://127.0.0.1:5000/create_account_api/create_account', data, {headers: {'Content-Type': 'application/json'}})
             .then((response) => {
              this.posts = response.data;
          this.errorData = null
                    this.fieldCheck = null;

                if (response.status === 201) {
                this.$router.push('/dashboard');
                }  
             })


        //link to dashboard
        
        //-----------------
    
    .catch(error =>  {
  


    if (error.response) {
     console.log(error.response.data);
      console.log(error.response.status);
      console.log(error.response.headers);
     this.posts = null;
      this.errorData = error.response.data;
    this.fieldCheck = null;
      
    }

            });
          
    


// try {
//     const res = await axios.post(
//         'http://127.0.0.1:5000/create_account_api/create_account', {
//          a, headers:{"Content-Type" : "application/json"}}
//         );
// console.log(res.response.data);
// } catch (error) {
//   console.error(error.response.data);     // NOTE - use "error.response.data` (not "error")
// }




      }
  }

  }
</script>


<style scoped>

.container{
    width : 100%;
    height: 100vh;  /*vh stands for viewable height */
    background-color: lightblue; /* can be image too*/
    position : relative;
    background-size: cover;
    background-position: center;
}


.form-box{
    width: 90%;
    max-width: 450px;  /*set a max width*/
   position: absolute; /*positioned relaitve to its position*/
    top: 30%;
    left: 30%;  /*middled using top and left*/
     transform: translate(-10%,-10%); /*translates box based on cordinates*/
    background : #fff;
     padding: 50px 60px 70px;    /*generate space around box*/
    text-align: center;       /*make sure text is centered*/

}

.form-box h1{
    font-size: 30px;
    margin-bottom: 60px; /*spaces it out from the fields*/
    color: #2da000;
    position: relative;

}

.form-box h1::after{  /*  */
    content: '';
    width: 30px;
    height: 4px;
    border-radius: 3px;
    background: #3c00a0;
    position: absolute;
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%)
    ;

}

.input-field{   
  background: #eaeaea;
  margin: 15px 0;   /* create space around text between textboxes */
  border-radius: 3px;  /*closes in margin border*/
  display: flex; /*use flexbox for all items */
  align-items: center; /*center all items in the flexbox*/

  max-height:65px;
  transition: max-height 0.5s; /* provides transition */
  overflow:hidden;

}


input{
width: 100%;
background: transparent;
border: 0;
outline: 0;
padding: 18px 15px; /*make padding of input boxes wider*/
}



form p{
    text-align: left;
    font-size: 13px;
}


form p a {
    text-decoration: none;
    color: #3c00a0;
}


.btn-field{  /* add spaces between flex box buttons */
    width:100%;
    display: flex;
    justify-content: space-between;
}

.btn-field button{ /*provides length for flex button*/
    flex-basis:48% ;
    background: #3c00a0;
    color: #ffff;
    height: 40px; /*increase height of button*/
    border-radius: 20px; /*makes border go in more rounder shape*/
    border:0;   /*get rid of border surrounding button*/
    outline:0; 
    cursor: pointer;
    transition: background 1s;
}

.input-group{ /*add space between input field and button*/
    
    height: 280px;
}

.invert{
    background: #eaeaea;
    color: rgb(85, 85, 85);
}



</style>