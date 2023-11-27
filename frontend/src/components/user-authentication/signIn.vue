<template>




  <div class="container">
    <div class ="form-box">
        <h1 ref="title">Sign In</h1>
 
        <form @submit.prevent="handleSubmit" > 
       

            <div class = "input-group">



                <div class="input-field">
                    <input type = "email" v-model = "email" placeholder = "Email"> 
               
                </div>

                <div class="input-field">
                    <input type = "password"  v-model = "password"  placeholder = "Password"> 
                </div>

                
            </div>
        <div class = "btn-field">
                <button class= "invert" id="signupBtn" @click="signUp = !signUp">Sign In</button>
      
             
                </div>
         





        </form>


    </div>

</div>


</template>

<script>
import axios from 'axios'
import { checkPassword } from './hash';

  export default {
      name: 'signIn',

data(){

return {

email: '',
password: ''
}
},


methods:{
 async handleSubmit(){

const data = {
email: this.email,
password: this.password
};
    


// try {
//     const res = await axios.post(
//         'http://127.0.0.1:5000/login_api/login?Email=zachf@testing.com&Password=Password1', {
//          data

//         });
// }
// catch (error){
//     console.log(error.response.data);
// }
    
axios.post('http://127.0.0.1:5000/login_api/login', {email: data.email}, {headers: {'Content-Type': 'application/json'}})
     .then((response) => {
        console.log(response);
        
        //link to dashboard
        
        if(checkPassword(data.password, response.data.password, response.data.salt)) {
            if (response.status === 200) {
         localStorage.setItem('userId', response.data.userId); 
         localStorage.setItem('firstName',response.data.firstName);
                let link = document.createElement('a');
                link.href = "/dashboard";
                link.click();
             }
        } else {
            console.log("Password was not valid")
        }
        //-----------------
    });

          console.log(data.email);

      }
  }

  }
</script>


<style scoped>
/* Align sign-in component's styles with the sign-up component */

.container {
  width: 100vw;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: lightblue;
  position: relative;
  border: none;
  margin: 0;
  padding: 0;
  overflow: auto;
}

.form-box {
  width: 90%; /* Same as the sign-up component */
  max-width: 450px; /* Same as the sign-up component */
  position: absolute;
  top: 50%; /* Same as the sign-up component */
  left: 50%; /* Same as the sign-up component */
  transform: translate(-50%, -50%);
  background: #fff;
  padding: 50px 60px; /* Same as the sign-up component */
  text-align: center;
  border: none !important;
  margin: 0 !important;
  box-sizing: border-box;
}

.form-box h1 {
  font-size: 30px; /* Same as the sign-up component */
  margin-bottom: 60px; /* Same as the sign-up component */
  color: #2da000;
  position: relative;
}

.form-box h1::after {
  content: '';
  width: 30px;
  height: 4px;
  border-radius: 3px;
  background: #3c00a0;
  position: absolute;
  bottom: -12px;
  left: 50%;
  transform: translateX(-50%);
}

.input-field {
  background: #eaeaea;
  margin: 15px 0;
  border-radius: 3px;
  display: flex;
  align-items: center;
  max-height: 65px;
  transition: max-height 0.5s;
  overflow: hidden;
}

input {
  width: 100%;
  background: transparent;
  border: 0;
  outline: 0;
  padding: 18px 15px;
}

form p {
  text-align: left;
  font-size: 13px;
}

form p a {
  text-decoration: none;
  color: #3c00a0;
}

.btn-field {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

.btn-field button {
  flex-basis: 48%;
  background: #3c00a0;
  color: #ffff;
  height: 40px;
  border-radius: 20px;
  border: 0;
  outline: 0;
  cursor: pointer;
  transition: background 1s;
}

.input-group {
  height: 280px;
}

.invert {
  background: #eaeaea;
  color: rgb(85, 85, 85);
}
</style>
