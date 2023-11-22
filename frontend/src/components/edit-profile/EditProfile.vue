<template>
    <header>
        <h2>Edit Profile</h2>
        <p>What would you like to update?</p>
        <form @submit="onSubmit">
            <table>
                <tr id="updateAge">
                    <td class="rightAlign">
                        <label>Age:&nbsp;</label>
                    </td>
                    <td>
                        <input type="number" id="age" v-model="newData['age']" min="1" onkeydown="return event.keyCode !== 69 && event.keyCode !== 190"/>
                    </td>
                </tr>
                <tr id="updateHeight">
                    <td class="rightAlign">
                        <label>Height:&nbsp;</label>
                    </td>
                    <td>
                        <input type="number" id="height" v-model="newData['height']" min="1" onkeydown="return event.keyCode !== 69"/>
                    </td>
                    <td class="leftAlign">
                        <label>&nbsp;inches</label>
                    </td>
                </tr>
                <tr id="updateWeight">
                    <td class="rightAlign">
                        <label>Weight:&nbsp;</label>
                    </td>
                    <td>
                        <input type="number" id="weight" v-model="newData['weight']" min="1" onkeydown="return event.keyCode !== 69"/>
                    </td>
                    <td class="leftAlign">
                        <label>&nbsp;pounds</label>
                    </td>
                </tr>
                    </table><br>
            
            <input type="submit" value="Submit"/><br><br>
        </form>
            
        <p id="message"></p>
        <br><br>
        <a href="/dashboard"><button>Back</button></a>
    </header>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'edit-profile',
        data() {
            return {
                newData: {}
            }
        },
        async created() {
            var oldData = (await axios.get(`http://127.0.0.1:5000/user_api/get_user_data/${localStorage.getItem('userId')}`))['data']['user_data'][0];
            this.newData['age'] = oldData[0];
            this.newData['height'] = oldData[1];
            this.newData['weight'] = oldData[2];
        },
        methods: {
            async onSubmit(e) {
                e.preventDefault();

                var oldData = (await axios.get(`http://127.0.0.1:5000/user_api/get_user_data/${localStorage.getItem('userId')}`))['data']['user_data'][0];
                var updatedData = {};
                var keys = ['age', 'height', 'weight'];
                var updatedKeys = [];
                for (var i = 0; i < keys.length; i++) {
                    let key = keys[i];
                    if (this.newData[key] === undefined || this.newData[key] === null || this.newData[key] === "" || this.newData[key] == oldData[i]) {
                        updatedData[key] = oldData[i];
                    } else {
                        updatedData[key] = this.newData[key];
                        updatedKeys.push(key);
                    }
                }

                let result = await axios.put("http://localhost:5000/user_api/update_user_data", {
                    user_id: localStorage.getItem('userId'),
                    user_age: updatedData.age,
                    user_height: updatedData.height,
                    user_weight: updatedData.weight
                });
                console.log(result);
                if (updatedKeys.length == 0) {
                    document.querySelector("#message").innerHTML = "No data was changed";
                } else if (result.status === 200) {
                    let updatedKeysString = "";
                    if (updatedKeys.length === 1) {
                        updatedKeysString = updatedKeys[0];
                    } else if (updatedKeys.length === 2) {
                        updatedKeysString = updatedKeys.join(" and ");
                    } else {
                        let finalKey = updatedKeys.pop();
                        updatedKeysString = updatedKeys.join(", ") + ", and " + finalKey;
                    }
                    //for (i in updatedKeys) {}
                    document.querySelector("#message").innerHTML = `Successfully updated your ${updatedKeysString}`;
                } else {
                    document.querySelector("#message").innerHTML = "Error: Couldn't update your data";
                }
            }
        }
    }
</script>

<style scoped>
    table {
        margin: auto;
    }

    .leftAlign {
        text-align: left;
    }

    .rightAlign {
        text-align: right;
    }
</style>