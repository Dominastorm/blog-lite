<template>
  <div>
    <NavBar user="John Doe" :userId="1" />
    <h2>Followers</h2>
    <div class="box">
      <ul>
        <div v-for="follower in followers" :key="follower.id" class="list-item">
          <router-link class="link" :to="'/profile/' + follower.id">{{ follower.username }}</router-link>
          <button class="button follow" v-if="!follower.followed" @click="follow(follower.id)">Follow</button>
          <button class="button unfollow" v-else @click="unfollow(follower.id)">Unfollow</button>
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
        }
        // Add more followers here
      ]
    }
  },
  mounted() {
    // Make an API call to get the IDs of all followers that the logged-in user is currently following
    const followedIds = [1] // Replace with actual API response

    // Loop through the followers array and update the followed property of each follower accordingly
    this.followers.forEach((follower) => {
      follower.followed = followedIds.includes(follower.id)
    })
  },
  methods: {
    follow(userId) {
      // Send an API request to follow the user with the given ID
      console.log('Following user', userId)

      // Update the followed property of the respective follower to true
      const follower = this.followers.find((follower) => follower.id === userId)
      if (follower) {
        follower.followed = true
      }
    },
    unfollow(userId) {
      // Send an API request to unfollow the user with the given ID
      console.log('Unfollowing user', userId)

      // Update the followed property of the respective follower to false
      const follower = this.followers.find((follower) => follower.id === userId)
      if (follower) {
        follower.followed = false
      }
    }
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

.unfollow:hover {
  background-color: #d81616;
}

.follow:hover {
  background-color: #06690e;
}

</style>