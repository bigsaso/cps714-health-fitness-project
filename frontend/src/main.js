import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import 'bootstrap/dist/css/bootstrap.min.css'
import App from './App.vue'

import MyLanding from './components/landing-page/Landing.vue';
import DataInputPage from './components/data-input/DataInputPage.vue';
import UserAuthentication from './components/user-authentication/UserAuthentication.vue';
import EditProfile from './components/edit-profile/EditProfile.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/dashboard', component: MyLanding },
        { path: '/update-progress', component: DataInputPage },
        { path: '/edit-profile', component: EditProfile },
        { path: '/', component: UserAuthentication }
    ]
});

const app = createApp(App)

app.use(router);
app.mount('#app');
