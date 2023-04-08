<template>
    <div>
        <NavBar />
        <h2 for="search">Search</h2>
        <div class="box">
            <div class="search-container">
                <input type="text" id="search" v-model="searchText" @input="searchUsers" />
                <span class="search-placeholder" v-show="!searchText"> Search users...</span>
            </div>
            <ul>
                <div class="list-item" v-for="user in users" :key="user.id">
                    <router-link class="link" :to="'/profile/' + user.id">{{ user.name }}</router-link>
                    <button class="button" @click="follow(user)">{{ following.includes(user.id) ? 'Unfollow' : 'Follow' }}</button>
                </div>
            </ul>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'

import NavBar from '@/components/NavBar.vue'

export default {
    components: {
        NavBar
    },
    data() {
        return {
            searchText: '',
            users: [],
            following: [],
        }
    },
    computed: {
        userId() {
            return localStorage.getItem('userId')
        },
    },
    methods: {
        searchUsers() {
            const path = 'http://localhost:5000/search/' + this.userId + '/' + this.searchText;
            axios
                .get(path)
                .then((response) => {
                    this.users = response.data.searchResults;
                })
                .catch(() => {
                    this.users = [];
                })
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