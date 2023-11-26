<template>
    <ShareNetwork
      v-for="network in networks"
      :network="network.network"
      :key="network.network"
      :style="{backgroundColor: network.color}"
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
          { network: 'facebook', name: 'Facebook', icon: 'fab fah fa-lg fa-facebook-f', color: '#1877f2' },
          { network: 'linkedin', name: 'LinkedIn', icon: 'fab fah fa-lg fa-linkedin', color: '#007bb5' },
          { network: 'reddit', name: 'Reddit', icon: 'fab fah fa-lg fa-reddit-alien', color: '#ff4500' },
          { network: 'twitter', name: 'Twitter', icon: 'fa-brands fa-twitter', color: '#1da1f2' }
        ],
        networkicons:[
          { network: 'facebook', name: 'Facebook', icon: 'fab fah fa-lg fa-facebook-f', color: '#1877f2' },
          { network: 'linkedin', name: 'LinkedIn', icon: 'fab fah fa-lg fa-linkedin', color: '#007bb5' },
          { network: 'reddit', name: 'Reddit', icon: 'fab fah fa-lg fa-reddit-alien', color: '#ff4500' },
          { network: 'twitter', name: 'Twitter', icon: 'fa-brands fa-twitter', color: '#1da1f2' }

        ]
      }
    }
  }
  </script>