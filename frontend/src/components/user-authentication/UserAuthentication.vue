<template>
  <div class="user-authentication">
    <div class="auth-container">
      <div class="form-box">
        <SignIn v-if="currentComponent === 'sign-in'" @switchToSignUp="showSignUp"></SignIn>
        <SignUp v-else-if="currentComponent === 'sign-up'" @switchToSignUp="showSignIn"></SignUp>
        <div class="button-field">
          <button class="b1 larger-button" @click="showSignIn">Sign-in</button>
          <button class="b2 larger-button" @click="showSignUp">Sign-up</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SignIn from './signIn.vue';
import SignUp from './signUp.vue';

export default {
  name: 'UserAuthentication',
  components: {
    SignIn,
    SignUp,
  },
  data() {
    return {
      currentComponent: 'sign-up',
    };
  },
  methods: {
    showSignIn() {
      this.currentComponent = 'sign-in';
    },
    showSignUp() {
      this.currentComponent = 'sign-up';
    },
  },
};
</script>

<style scoped>
/* Existing styles for user-authentication */
/* ... */



.auth-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column; /* Ensure vertical layout */
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
  z-index: 999; /* Ensure the container is on top */
}

.button-field {
  position: fixed;
  top: 90px; /* Adjust the top position as needed */
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  width: 450px; /* Set a specific width for the button container */
  display: flex; /* Use flexbox */
  justify-content: space-between; /* Space buttons evenly */
}

.button-field button {
  width: 50%; /* Keep the button width */
  background-color: white; /* Make the background transparent */
  border: 2px solid black; /* Add a border with your preferred color */
  border-radius: 8px; /* Rounded corners for a softer look */
  color: black; /* Set the text color */
  font-size: 18px; /* Adjust font size */
  padding: 12px 20px; /* Adjust padding for better appearance */
  cursor: pointer; /* Show pointer on hover */
  transition: all 0.3s ease; /* Smooth transition on hover */


}

.button-field button:hover {
  background-size: 100% 2px; /* Expand the gradient on hover */
  color: blue; /* Change text color on hover */
}


/* Other styles for SignUp component's structure */
.sign-up .container {
  position: relative;
  padding-top: 50px; /* Space for the fixed button-field */
}

.sign-up .form-box {
  /* Other styles */
}
</style>
