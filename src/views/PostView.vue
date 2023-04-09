<template>
  <div>
    <NavBar />
    <h2>{{ title }}</h2>
    <img :src="image" alt="Post image">
    <p>Posted by: {{ username }}</p>
    <p>Created on: {{ timestamp.split(' ')[0] }}</p>
    <p>{{ body }}</p>
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
    }
  }, 
  data() {
    return {
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
          this.title = post.title;
          this.image = post.image;
          this.caption = post.caption;
          this.username = post.username;
          this.timestamp = post.timestamp;
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

img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
    margin-top: 1rem;
}
</style>  
