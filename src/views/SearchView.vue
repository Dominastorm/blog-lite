<template>
    <div>
        <label for="search">Search:</label>
        <input type="text" id="search" v-model="searchText" @input="searchUsers" />
        <ul>
            <li v-for="user in filteredUsers" :key="user.id">
                <router-link :to="'/profile/' + user.id">{{ user.username }}</router-link>
                <button @click="follow(user)">{{ following.includes(user.id) ? 'Unfollow' : 'Follow' }}</button>
            </li>
        </ul>
    </div>
</template>
  
<script>
export default {
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
  