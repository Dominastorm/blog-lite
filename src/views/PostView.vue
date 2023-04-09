<template>
  <NavBar />
  <!-- if myUserId is same as userId, display edit, delete and export buttons -->
  <div class="post-container">
    <div class="buttons">
      <button v-if="myUserId == userId" class="edit button" v-on:click="$router.push('/editpost/' + postId)">Edit</button>
      <button v-if="myUserId == userId" class="delete button" v-on:click="deletePost">Delete</button>
      <button class="export button" v-on:click="$router.push('/export/' + postId)">Export</button>
    </div>
    <h2>{{ title }}</h2>
    <img class="post-image" :src="image" alt="Post image">
    <br />
    <p class="post-info">Posted by: <router-link class="link" :to="'/profile/' + userId">{{ username }}</router-link></p>
    <p class="post-info">Created on: {{ timestamp.split(' ')[0] }}</p>
    <br />
    <div class="post-caption" v-html="caption"></div>
  </div>
</template>

<script>
import axios from 'axios';

import NavBar from '@/components/NavBar.vue';

export default {
  components: {
    NavBar
  },
  computed: {
    postId() {
      return window.location.href.split('/').pop();
    },
    myUserId() {
      return localStorage.getItem('userId');
    }
  },
  data() {
    return {
      userId: 0,
      title: '',
      image: '',
      caption: '',
      username: '',
      timestamp: ''
    }
  },
  methods: {
    getPost(postId) {
      const path = `http://localhost:5000/post/${postId}`;
      axios.get(path)
        .then(response => {
          const post = response.data.post;
          this.userId = post.userId;
          this.title = post.title;
          this.image = post.image;
          this.caption = post.caption;
          this.username = post.username;
          this.timestamp = post.timestamp;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deletePost() {
      const path = `http://localhost:5000/deletepost/`;
      const params = "userId=" + this.userId + "&postId=" + this.postId;
      axios.post(path, params)
        .then(response => {
          console.log(response);
          this.$router.push('/');
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getPost(this.postId);
  }
}

</script>

<style>
.post-container {
  margin: 0 auto;
  padding: 20px;
  max-width: 80%;
  max-height: 100%;
  background-color: rgb(206, 212, 219);
  box-shadow: 0px 0px 10px #ccc;
  border-radius: 5px;
}

.post-image {
  display: block;
  max-width: 100%;
  /* margin: 20px 0; */
  margin-right: auto;
  margin-left: auto;
  border-radius: 5px;
  box-shadow: 0px 0px 10px #ccc;
}

.post-info {
  text-align: center;
  display: block;
  font-size: 16px;
  color: #5d5d5d;
}

.post-caption {
  font-size: 18px;
  line-height: 1.5;
  margin-top: 20px;
  font-size: 26px;
  color: #000000;
  text-align: center;
}

body {
  /* Dark blue */
  background-color: #2c3e50;
  font-family: sans-serif;
}

h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-align: center;
}

.buttons {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.button {
  width: 125px;
  /* margin-right: rem; */
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

.edit:hover {
  background-color: #4CAF50;
}

.delete:hover {
  background-color: #f44336;
}

.export:hover {
  background-color: #008CBA;
}

</style>  
