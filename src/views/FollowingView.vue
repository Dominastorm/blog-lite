<template>
  <div>
    <NavBar />
    <h2>Following</h2>
    <div class="box">
      <ul>
        <div v-for="user in following" :key="user.id" class="list-item">
          <router-link class="link" :to="'/profile/' + user.id">{{ user.name }}</router-link>
          <button class="button follow" v-if="!user.followed" @click="follow(user.id)">Follow</button>
          <button class="button unfollow" v-else @click="unfollow(user.id)">Unfollow</button>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import NavBar from '@/components/NavBar.vue'

export default {
  name: 'FollowingView',
  components: {
    NavBar
  },
  data() {
    return {
      following: [],
    }
  },
  mounted() {
    // Make an API call to get the IDs of all users that the logged-in user is currently following
    // TODO: Replace with actual API response
    const followingIds = [2, 3]

    // Loop through the following array and update the followed property of each user accordingly
    this.following.forEach((user) => {
      user.followed = followingIds.includes(user.id)
    })

  },
  methods: {
    unfollow(userId) {
      // Send an API request to unfollow the user with the given ID
      console.log('Unfollowing user', userId)

      // Update the followed property of the respective user to false
      const user = this.following.find((user) => user.id === userId)
      if (user) {
        user.followed = false
      }
    },
    getFollowing(userId) {
      const path = 'http://localhost:5000/following/' + userId;
      console.log(path)
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.following = response.data.following;
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    const userId = localStorage.getItem('userId')
    this.getFollowing(userId);
  }
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
  margin-right: 2rem;
  margin-bottom: 1rem;
  padding: 0.5rem 2rem;
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

.button:hover {
  background-color: #d81616;
}
</style>