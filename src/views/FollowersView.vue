<template>
    <div>
      <h2>Followers</h2>
      <ul>
        <li v-for="follower in followers" :key="follower.id">
          <router-link :to="'/profile/' + follower.id">{{ follower.username }}</router-link>
          <button v-if="!follower.followed" @click="follow(follower.id)">Follow</button>
          <button v-else @click="unfollow(follower.id)">Unfollow</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        followers: [
          {
            id: 1,
            username: 'exampleuser1',
            followed: false
          },
          {
            id: 2,
            username: 'exampleuser2',
            followed: false
          },
          // Add more followers here
        ]
      }
    },
    mounted() {
      // Make an API call to get the IDs of all followers that the logged-in user is currently following
      const followedIds = [1]; // Replace with actual API response
  
      // Loop through the followers array and update the followed property of each follower accordingly
      this.followers.forEach(follower => {
        follower.followed = followedIds.includes(follower.id);
      });
    },
    methods: {
      follow(userId) {
        // Send an API request to follow the user with the given ID
        console.log('Following user', userId);
  
        // Update the followed property of the respective follower to true
        const follower = this.followers.find(follower => follower.id === userId);
        if (follower) {
          follower.followed = true;
        }
      },
      unfollow(userId) {
        // Send an API request to unfollow the user with the given ID
        console.log('Unfollowing user', userId);
  
        // Update the followed property of the respective follower to false
        const follower = this.followers.find(follower => follower.id === userId);
        if (follower) {
          follower.followed = false;
        }
      }
    }
  }
  </script>
  