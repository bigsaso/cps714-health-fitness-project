import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

//import 'bootstrap/dist/css/bootstrap.min.css'

import VueSocialSharing from 'vue-social-sharing'

import { library } from '@fortawesome/fontawesome-svg-core';

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faTwitter } from '@fortawesome/free-brands-svg-icons';


library.add(faTwitter);


import App from './App.vue'

import MyLanding from './components/landing-page/Landing.vue';
import DataInputPage from './components/data-input/DataInputPage.vue';
import UserAuthentication from './components/user-authentication/UserAuthentication.vue';
import EditProfile from './components/edit-profile/EditProfile.vue';
import PasswordReset from './components/user-authentication/setNewPassword.vue';



const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/dashboard', component: MyLanding },
        { path: '/update-progress', component: DataInputPage },
        { path: '/edit-profile', component: EditProfile },
        { path: '/', component: UserAuthentication },
        { path: '/password-reset', component: PasswordReset }
    ]
});

const app = createApp(App)

app.use(router);
app.use(VueSocialSharing);

app.component(('font-awesome-icon', FontAwesomeIcon));
app.mount('#app');



