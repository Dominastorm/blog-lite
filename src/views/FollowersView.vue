<template>
  <div>
    <NavBar /> 
    <h2>Followers</h2>
    <div class="box">
      <ul>
        <div v-for="follower in followers" :key="follower.id" class="list-item">
          <router-link class="link" :to="'/profile/' + follower.id">{{ follower.name }}</router-link>
          <FollowToggle
            :followed="follower.followed"
            @toggle-follow="follower.followed = !follower.followed"
          />
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import NavBar from '@/components/NavBar.vue'

import FollowToggle from '@/components/FollowToggle.vue'

export default {
  name: 'FollowersView',
  components: {
    NavBar,
    FollowToggle
  },
  data() {
    return {
      followers: [],
    }
  },
  methods: {
    getFollowers(userId) {
      const path = 'http://localhost:5000/followers/' +  userId;
      console.log(path)
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.followers = response.data.followers;
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    const userId = localStorage.getItem('userId')
    this.getFollowers(userId);
  }
}
</script>

<style>
body {
    background-color: #2c3e50;
    /* D    # login_user(user, remember=remember)ark blue */
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
</style>