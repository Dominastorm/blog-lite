<template>
    <div>
        <NavBar user="John Doe" :userId="1" />
        <h2 for="search">Search</h2>
        <div class="box">
            <div class="search-container">
                <input type="text" id="search" v-model="searchText" @input="searchUsers" />
                <span class="search-placeholder" v-show="!searchText"> Search users...</span>
            </div>
            <ul>
                <div class="list-item" v-for="user in filteredUsers" :key="user.id">
                    <router-link class="link" :to="'/profile/' + user.id">{{ user.username }}</router-link>
                    <button class="button" @click="follow(user)">{{ following.includes(user.id) ? 'Unfollow' : 'Follow' }}</button>
                </div>
            </ul>
        </div>
    </div>
</template>
  
<script>
import NavBar from '@/components/NavBar.vue'

export default {
    components: {
        NavBar
    },
    data() {
        return {
            users: [
                { id: 1, username: 'user1' },
                { id: 2, username: 'user2' },
                { id: 3, username: 'user3' },
                { id: 4, username: 'user4' },
                { id: 5, username: 'user5' },
            ],
            following: [1, 3, 5],
            searchText: '',
        }
    },
    computed: {
        filteredUsers() {
            if (this.searchText) {
                return this.users.filter((user) =>
                    user.username.toLowerCase().includes(this.searchText.toLowerCase())
                )
            } else {
                return this.users
            }
        },
    },
    methods: {
        follow(user) {
            if (this.following.includes(user.id)) {
                this.following.splice(this.following.indexOf(user.id), 1)
            } else {
                this.following.push(user.id)
            }
        },
        searchUsers() {
            // You can make an API call to search for users based on the searchText
            // and update the users array accordingly
        },
    },
}
</script>
  
<style>
body {
    background-color: #2c3e50;
    /* Dark blue */
    color: #fff;
    font-family: sans-serif;
}

h2 {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
    text-align: center;
}

.box {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    width: 100%;
    margin: 0 auto;
    padding: 2rem;
    /* Light blue */
    background-color: #2980b9;
    border-radius: 5px;
}

.list-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.link {
    flex-grow: 1;
    margin-bottom: 1rem;
    font-size: 1.25rem;
    color: black;
    text-decoration: none;
}

.button {
    width: 125px;
    margin-right: 2rem;
    margin-bottom: 1rem;
    padding: 0.5rem 1rem;
    border-radius: 3px;
    border: none;
    color: #fff;
    background-color: #413d40;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-left: 1rem;
}

input[type="text"] {
    padding: 0.5rem;
    font-size: 1rem;
    border: none;
    border-radius: 3px;
    width: 95%;
    background-color: azure;
}

.search-container {
    position: relative;
}

.search-icon {
    position: absolute;
    top: 50%;
    right: 8px;
    transform: translateY(-50%);
    color: #ccc;
}

.search-placeholder {
    position: absolute;
    top: 50%;
    left: 10px;
    transform: translateY(-50%);
    color: #ccc;
    pointer-events: none;
}
</style>