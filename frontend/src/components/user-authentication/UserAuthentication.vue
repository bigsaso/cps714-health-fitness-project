<template>


<div class=button-field>


<component v-bind:is="component"></component>
<button class=b1 v-on:click="component='sign-in'">Sign-in</button>
<button class=b2 v-on:click="component='sign-up'">Sign-up</button>




  

</div>



</template>

<script>
/* eslint-disable vue/no-unused-components */
import signIn from './signIn.vue';
import signUp from './signUp.vue';



export default {
  name: 'App',
  components: {
    'sign-in':signIn,
    'sign-up':signUp
  },

  data(){
    return{
      component: 'sign-up'
    }
  }

}
</script>

<style>

.button-field b1{
  position: relative;
  right:200px;
  up:1000px;
  
}


</style>
