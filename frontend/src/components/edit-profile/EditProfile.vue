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
                        <input type="number" id="age" class="inputBox" v-model="newData['age']" min="1" onkeydown="return event.keyCode !== 69 && event.keyCode !== 190"/>
                    </td>
                </tr>
                <tr id="updateHeight">
                    <td class="rightAlign">
                        <label>Height:&nbsp;</label>
                    </td>
                    <td>
                        <input type="number" id="height" class="inputBox" v-model="newData['height']" min="1" max="999" step="0.01" onkeydown="return event.keyCode !== 69"/>
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
                        <input type="number" id="weight" class="inputBox" v-model="newData['weight']" min="1" max="999" step="0.01" onkeydown="return event.keyCode !== 69"/>
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
        <button @click="resetChanges">Reset</button>
        &nbsp;&nbsp;
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
            this.setAllAttributesFromDB();
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
                
                let newMessage = "";
                if (updatedKeys.length == 0) {
                    newMessage = "No data was changed";
                    this.setAllAttributes(updatedData);
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
                    newMessage = `Successfully updated your ${updatedKeysString}`;
                    this.setAllAttributes(updatedData);
                } else {
                    newMessage = "Error: Couldn't update your data";
                }
                this.setStatusMessage(newMessage);
            },
            async resetChanges() {
                this.setAllAttributesFromDB();
                this.setStatusMessage("");
            },
            async setAllAttributes(dataObj) {
                this.newData['age'] = dataObj['age'];
                this.newData['height'] = parseFloat(dataObj['height']);
                this.newData['weight'] = parseFloat(dataObj['weight']);
            },
            async setAllAttributesFromDB() {
                var currentData = (await axios.get(`http://127.0.0.1:5000/user_api/get_user_data/${localStorage.getItem('userId')}`))['data']['user_data'][0];
                this.setAllAttributes({
                    age: currentData[0],
                    height: currentData[1],
                    weight: currentData[2]
                });
            },
            async setStatusMessage(newMessage) {
                document.querySelector("#message").innerHTML = newMessage;
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

    .inputBox {
        display: inline;
        min-width: 200px;
    }
</style>