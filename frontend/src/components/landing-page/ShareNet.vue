<template>
  <h5>Share this website!</h5>
    <ShareNetwork
      v-for="network in networks"
      :network="network.network"
      :key="network.network"
      :url="sharing.url"
      :title="sharing.title"
      :description="sharing.description"
      :quote="sharing.quote"
      :hashtags="sharing.hashtags"
      :twitterUser="sharing.twitterUser"
    >
    
      <i :class="network.icon"></i>
      <span>{{ network.name }}</span>
    </ShareNetwork>
  </template>
  

  <script>
  
  export default {
    name:"shareNetworks",
    data () {
      return {
        sharing: {
          url: 'my.ryerson.ca',
          title: 'With this health and fitness website, I was able to track my health and set my goals!',
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
      }
    }
    //methods:{
     // getFontAwesomeIcon(network){
      //  const iconMap ={
        //  facebook : 'fa-brands fa-lg fa-facebook-f',
          //linkedin : 'fa-brands fa-lg fa-linkedin',
          //reddit : 'fa-brands fa-lg fa-reddit-alien',
          //twitter : 'fa-brands fa-lg fa-twitter'
        //};
     //   return iconMap[network] || 'fas fa-lg fa-question';
      //}


   // }
  };
  </script>