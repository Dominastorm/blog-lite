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

    <v-dialog v-model="showDialog" persistent max-width="290">
      <v-card>
        <v-card-text>Incorrect credentials</v-card-text>
        <v-card-actions>
          <v-btn color="danger" text @click="showDialog = false">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import TopBar from '@/components/TopBar.vue'

export default {
  name: 'LoginView',
  components: {
    TopBar
  },
  data() {
    return {
      email: '',
      password: '',
      showDialog: false
    }
  },
  methods: {
  login() {
    const path = 'http://localhost:5000/login'
    const credentials = "email=" + this.email + "&password=" + this.password 
    axios.post(path, credentials)
      .then((response) => {
        console.log(response)
        console.log()
        // Save the token in local storage
        localStorage.setItem('token', response.data.token)

        // Save the user id in local storage
        localStorage.setItem('userId', response.data.userId)

        // Redirect the user to the home page
        this.$router.push('/')
      })
      .catch((error) => {
        console.log(error)
        this.showDialog = true
      })
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
  background-color: azure;
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
