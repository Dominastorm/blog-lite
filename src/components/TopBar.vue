<template>
    <div class="top-bar">
      <div class="top-bar-left">
        <h2>Blog Lite</h2>
      </div>
      <div class="top-bar-right">
        <router-link :to="authLink">{{ authButtonText }}</router-link>
      </div>
    </div>
  </template>
  <script>
  export default {
    props: {
      authType: {
        type: String,
        required: true,
        validator: value => ['login', 'signup'].includes(value)
      }
    },
    computed: {
      authLink() {
        return this.authType === 'login' ? '/login' : '/signup';
      },
      authButtonText() {
        return this.authType === 'login' ? 'Login' : 'Sign Up';
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
  In this implementation, the authButtonText computed property returns either "Login" or "Sign Up" based on the value of the authType prop. The navbar shows a link to the Login page with the text "Login" if authType is "login", and a link to the Sign Up page with the text "Sign Up" if authType is "signup". You can use this navbar component in your Login and Sign Up pages, passing the appropriate authType prop to control the button that's shown.
  
  
  
  