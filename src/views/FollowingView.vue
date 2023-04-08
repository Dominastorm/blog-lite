<template>
  <div>
    <NavBar />
    <h2>Following</h2>
    <div class="box">
      <ul>
        <div v-for="following in followings" :key="following.id" class="list-item">
          <router-link class="link" :to="'/profile/' + following.id">{{ following.name }}</router-link>
          <FollowToggle
            :followed="following.followed"
            :followerId="following.id"
            @toggle-follow="following.followed = !following.followed"
          />
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import NavBar from '../components/NavBar.vue'
import FollowToggle from '../components/FollowToggle.vue';

export default {
  name: 'FollowingView',
  components: {
    NavBar,
    FollowToggle
},
  data() {
    return {
      followings: [],
    }
  },
  methods: {
    getFollowing(userId) {
      const path = 'http://localhost:5000/following/' + userId;
      console.log(path)
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.followings = response.data.following;
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