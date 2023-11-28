<template>
  <template v-if="weightPercentage === 100">
      <h5>Share your achievement!</h5>
      <div @click="handleShareClick" style="display: flex; flex-direction: column;">
    <ShareNetwork
      v-for="network in networks"
      :network="network.network"
      :key="network.network"
      :url="sharing.url"
      :title="computedTitle"
      :description="sharing.description"
      :quote="sharing.quote"
      :hashtags="sharing.hashtags"
      :twitterUser="sharing.twitterUser"
    >
    
      <i :class="network.icon"></i>
      <span>{{ network.name }}</span>
    </ShareNetwork>
  </div>
  </template>
    <template v-else>
        <h4>Share</h4>
        <p>Share will only be avaible after hitting your weight goal!</p>

    </template>
  </template>
  

  <script>
  
  export default {
    name:"shareNetworks",
    props: ['weightPercentage','goalWeight'],
    data () {
      return {
        sharing: {
          url: 'my.ryerson.ca',
          title: "`With this health fitness website, I was able to hit my weight goal of ${goalWeight}`",
          description: 'This site is amazing! You guys got to check this out! Its simple to sign up and displays everything you need!',
          quote: '',
          hashtags: 'health,fitness,tmu',
          twitterUser: ''
        },
        networks: [
          { network: 'facebook', name: 'Facebook', icon: 'fa-brandsfa-lg fa-facebook-f' },
          { network: 'linkedin', name: 'LinkedIn', icon: 'fa-brands fa-lg fa-linkedin'},
          { network: 'reddit', name: 'Reddit', icon: 'fa-brands fa-lg fa-reddit-alien'},
          { network: 'twitter', name: 'Twitter', icon: 'fa-brands fa-twitter'}
        ],
        //weightPercentage: localStorage.getItem('goal'),
      }

    },
    computed: {
    computedTitle() {
      return `With this health fitness website, I was able to hit my weight goal of ${this.goalWeight}lb`;
    },
  },
  methods: {
    handleShareClick() {
      // Emit an event named 'shareClicked'
      this.$emit('shareClicked');
    },
  },


  };
  </script>