<template>
    <div>
      <h2>Following</h2>
      <ul>
        <li v-for="user in following" :key="user.id">
          <router-link :to="'/profile/' + user.id">{{ user.username }}</router-link>
          <button @click="unfollow(user.id)">Unfollow</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        following: [
          {
            id: 1,
            username: 'exampleuser1'
          },
          {
            id: 2,
            username: 'exampleuser2'
          },
          // Add more followed users here
        ]
      }
    },
    methods: {
      unfollow(userId) {
        // Send an API request to unfollow the user with the given ID
        console.log('Unfollowing user', userId);
      }
    }
  }
  </script>
  