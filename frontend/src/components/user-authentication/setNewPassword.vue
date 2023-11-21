<template>
    <div class="container">
        <div class="form-box">
            <h1 ref="title">Set New Password</h1>
            <h2> {{ posts.message }} </h2>
            <form @submit.prevent="handleSubmit">
                <div class="input-group">
                    <div class="input-field">
                        <input
                            type="email"
                            v-model="email"
                            placeholder="Email"
                        >
                    </div>
                    <div class="input-field">
                        <input
                            type="password"
                            v-model="password"
                            placeholder="New Password"
                        >
                    </div>
                </div>
                <div class="btn-field">
                    <button
                        class="invert"
                        id="submitBtn"
                        @click="handleSubmit('resetPassword')"
                    >Submit New Password</button>
                    <button
                        class="invert"
                        id="signupBtn"
                        @click="handleSubmit('signUp')"
                    >Logout</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { generateSalt, getHashedPassword, checkPassword } from './hash';

export default {
    name: 'setNewPassword',

    data() {
        return {
            email: '',
            password: '',
            salt: '',
            posts: []
        }
    },

    methods: {
        async handleSubmit(action) {
            if (action === "signUp") {
                this.$router.push('/');
            } else {
                let salt = generateSalt();

                const data = {
                    email: this.email,
                    password: getHashedPassword(this.password, salt),
                    salt: salt
                };

                axios.post('http://127.0.0.1:5000/login_api/reset', data, { headers: { 'Content-Type': 'application/json' } })
                    .then((response) => {
                        console.log(response);

                        //link to dashboard
                        if (response.status === 200) {
                            // localStorage.setItem('userId', response.data.userId);
                            // alert(`New password has been set for ${data.email}`);

                            axios.post('http://127.0.0.1:5000/login_api/login', { email: data.email }, { headers: { 'Content-Type': 'application/json' } })
                                .then((response) => {
                                    console.log(response);

                                    //link to dashboard

                                    if (checkPassword(this.password, response.data.password, response.data.salt)) {
                                        if (response.status === 200) {
                                            localStorage.setItem('userId', response.data.userId);
                                            this.$router.push('/dashboard');
                                        }
                                    } else {
                                        console.log("Password was not valid")
                                    }
                                    //-----------------
                                });
                          
                        }
                        //-----------------
                    })
                    .catch(error => {
                        if (error.response) {
                            console.log(error.response.data);
                            console.log(error.response.status);
                            console.log(error.response.headers);
                        }
                    });
            }
        }
    }

}
</script>

<style scoped>
.container {
    width: 100%;
    height: 100vh;
    /*vh stands for viewable height */
    background-color: lightblue;
    /* can be image too*/
    position: relative;
    background-size: cover;
    background-position: center;
}

.form-box {
    width: 90%;
    max-width: 450px;
    /*set a max width*/
    position: absolute;
    /*positioned relaitve to its position*/
    top: 30%;
    left: 30%;
    /*middled using top and left*/
    transform: translate(-10%, -10%);
    /*translates box based on cordinates*/
    background: #fff;
    padding: 50px 60px 70px;
    /*generate space around box*/
    text-align: center;
    /*make sure text is centered*/

}

.form-box h1 {
    font-size: 30px;
    margin-bottom: 60px;
    /*spaces it out from the fields*/
    color: #2da000;
    position: relative;
}

.form-box h1::after {
    /*  */
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
    /* create space around text between textboxes */
    border-radius: 3px;
    /*closes in margin border*/
    display: flex;
    /*use flexbox for all items */
    align-items: center;
    /*center all items in the flexbox*/
    max-height: 65px;
    transition: max-height 0.5s;
    /* provides transition */
    overflow: hidden;
}

input {
    width: 100%;
    background: transparent;
    border: 0;
    outline: 0;
    padding: 18px 15px;
    /*make padding of input boxes wider*/
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
    /* add spaces between flex box buttons */
    width: 100%;
    display: flex;
    justify-content: space-between;
}

.btn-field button {
    /*provides length for flex button*/
    flex-basis: 48%;
    background: #3c00a0;
    color: #ffff;
    height: 50px;
    /*increase height of button*/
    border-radius: 20px;
    /*makes border go in more rounder shape*/
    border: 0;
    /*get rid of border surrounding button*/
    outline: 0;
    cursor: pointer;
    transition: background 1s;
}

.input-group {
    /*add space between input field and button*/
    height: 280px;
}

.invert {
    background: #eaeaea;
    color: rgb(85, 85, 85);
}</style>