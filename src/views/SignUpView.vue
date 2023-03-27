<template>
  <div>
    <TopBar authType='login'/>
    <h2>Sign Up</h2>
    <form @submit.prevent="signup">
      <div>
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="name" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <label for="password">Confirm Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <button type="submit">Sign Up</button>
      </div>
    </form>
    <p>Already have an account? <router-link to="/login">Log in</router-link></p>
  </div>
</template>

<script>
import TopBar from '../components/TopBar.vue';

export default {
  components : {
    TopBar
  },
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


<style>
body {
  background-color: #2c3e50; /* Dark blue */
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
  background-color: #2980b9; /* Light blue */
  border-radius: 5px;
}

label {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  padding: 0.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 3px;
}

button[type="submit"] {
  padding: 0.5rem;
  background-color: #2c3e50; /* Dark blue */
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
  background-color: #34495e; /* Slightly darker shade of dark blue */
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
}
</style>
