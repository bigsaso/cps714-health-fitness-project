<template>
  <div class="container">
    <div class="form-box">
      <h1 ref="title">Sign Up</h1>

      <div v-if="fieldCheck">
        <!-- Display the field check error message if it exists -->
        <h2>{{ fieldCheck }}</h2>
      </div>

      <div v-else-if="posts">
        <!-- Display response data if it exists -->
        <h2>{{ posts.message }}</h2>
      </div>

      <div v-else-if="errorData">
        <!-- Display error response code if it exists -->
        <h2>{{ errorData.error }}</h2>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="input-group">
          <div class="input-field">
            <input type="text" v-model="first_name" placeholder="First-Name">
          </div>

          <div class="input-field">
            <input type="text" v-model="last_name" placeholder="Last-Name">
          </div>

          <div class="input-field">
            <input type="email" v-model="email" placeholder="Email">
          </div>

          <div class="input-field">
            <input type="password" v-model="password" placeholder="Password">
          </div>
        </div>

        <div class="btn-field">
          <button class="invert" id="signupBtn" @click="signUp = !signUp">Sign up</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { generateSalt, getHashedPassword } from './hash';

export default {
  name: 'SignUp',
  data() {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      salt: '',
      posts: null,
      errorData: null,
      fieldCheck: null
    };
  },
  methods: {
    async handleSubmit() {
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
        last_name: this.last_name,
        email: this.email,
        password: getHashedPassword(this.password, salt),
        salt: salt
      };

      axios.post('http://127.0.0.1:5000/create_account_api/create_account', data, { headers: { 'Content-Type': 'application/json' } })
        .then((response) => {
          this.posts = response.data;
          this.errorData = null;
          this.fieldCheck = null;
        })
        .catch(error => {
          if (error.response) {
            this.posts = null;
            this.errorData = error.response.data;
            this.fieldCheck = null;
          }
        });
    }
  }
};
</script>

<style scoped>
/* Reset or default styling for SignUp component */
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
  width: 90%;
  max-width: 450px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #fff;
  padding: 50px 60px;
  text-align: center;
  border: none !important;
  margin: 0 !important;
  box-sizing: border-box;
}

.form-box h1 {
  font-size: 30px;
  margin-bottom: 60px;
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
