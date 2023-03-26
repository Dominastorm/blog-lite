<template>
    <div>
      <h2>Sign Up</h2>
      <form @submit.prevent="signup">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="name" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div></div>
          <label for="password">Confirm Password:</label>
          <input type="password" id="password" v-model="password" required>
        <div>
          <button type="submit">Sign Up</button>
        </div>
      </form>
        <p>Already have an account? <router-link to="/login">Log in</router-link>.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: ''
      }
    },
    methods: {
      signup() {
        // Your signup logic goes here
        console.log('Signing up...')
      }
    }
  }
  </script>
  