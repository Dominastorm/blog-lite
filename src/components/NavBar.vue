<template>
  <div class="top-bar">
    <div class="top-bar-left">
      <h2>Welcome {{ userName }}</h2>
    </div>
    <div class="top-bar-right">
      <router-link to="/">Home</router-link>
      <router-link to="/createpost">Create Post</router-link>
      <router-link to="/search">Search</router-link>
      <router-link :to="/profile/ + userId">My Profile</router-link>
      <a href="/login" @click="logout">Logout</a>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    userId() {
      return localStorage.getItem('userId')
    },
    userName() {
      return localStorage.getItem('userName')
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('userId')
      localStorage.removeItem('userName')
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
  gap: 2rem;
}

.top-bar-right > *:not(:last-child)::after {
  content: "";
  border-right: 1px solid white;
  margin-left: 2rem;
  height: 1rem;
  align-self: center;
}

.top-bar-right *::last {
  margin-left: 1rem;
}

.top-bar-right a {
  color: #fff;
  text-decoration: none;
}
</style>
