<template>
  <div>
    <TopBar authType="signup" />
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
    <p>Don't have an account? <router-link to="/signup">Sign up</router-link></p>
  </div>
</template>

<script>
import TopBar from '@/components/TopBar.vue';

export default {
  components: {
    TopBar
  },
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    login() {
      // Your login logic goes here
      console.log('Logging in...')
    }
  }
}
</script>

<style>
body {
  /* Dark blue */
  background-color: #2c3e50;
  color: #fff;
  font-family: sans-serif;
}

h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 400px;
  align-items: center;
  width: 100%;
  margin: 0 auto;
  padding: 2rem;
  /* Light blue */
  background-color: #2980b9;
  border-radius: 5px;
}

label {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input[type="email"],
input[type="password"] {
  padding: 0.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 3px;
}

button[type="submit"] {
  padding: 0.5rem;
  /* Dark blue */
  background-color: #2c3e50;
  color: #fff;
  border: none;
  border-radius: 3px;
  font-size: 1.2rem;
  font-weight: bold;
  cursor: pointer;
  display: block;
  margin: 0 auto;
}

button[type="submit"]:hover {
  /* Slightly darker shade of dark blue */
  background-color: #34495e;
}

p {
  font-size: 1.2rem;
  margin-top: 1rem;
  text-align: center;
}

a {
  color: #fff;
  text-decoration: underline;
}

a:hover {
  color: #eee;
}</style>
