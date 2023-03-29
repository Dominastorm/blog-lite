<template>
  <div class="top-bar">
    <div class="top-bar-left">
      <h2>Welcome {{ user }}</h2>
    </div>
    <div class="top-bar-right">
      <router-link to="/search">Search</router-link>
      <router-link :to="'/profile/' + userId">My Profile</router-link>
      <a href="/login" @click="logout">Logout</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: String,
      required: true
    },
    userId: {
      type: String,
      required: true
    }
  },
  methods: {
    logout() {
      // Your logout logic goes here
      console.log('Logging out...')
    }
  }
}
</script>

<style>
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}
.top-bar-right {
  display: flex;
  gap: 1rem;
}
.top-bar-right a {
  color: #fff;
  text-decoration: none;
}
</style>
