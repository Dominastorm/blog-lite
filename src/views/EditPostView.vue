<template>
  <div>
    <NavBar />
    <h2>Edit Post</h2>
    <form @submit.prevent="editPost">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="title" required/>
      </div>
      <div>
        <label for="caption">Caption:</label>
        <textarea id="caption" v-model="caption" required></textarea>
      </div>
      <div class="upload">
        <label for="image">Image:</label>
        <input type="url" id="image" v-model="image" required/>
      </div>
      <div>
        <button type="submit">Update</button>
      </div>
    </form>
  </div>
</template>
<script>
import axios from 'axios';

import NavBar from '@/components/NavBar.vue';

export default {
  components: {
    NavBar
  },
  data() {
    return {
      title: '',
      caption: '',
      image: '',
    }
  },
  computed: {
    userId() {
      return localStorage.getItem('userId');
    },
    postId() {
      return window.location.href.split('/').pop();
    }
  },
  created() {
    this.getPostDetails();
  },
  methods: {
    getPostDetails() {
      const path = `http://localhost:5000/post/${this.postId}`;
      axios.get(path)
        .then((response) => {
          const post = response.data.post;
          this.title = post.title;
          this.caption = post.caption;
          this.image = post.image;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editPost() {
      const path = 'http://localhost:5000/editpost';
      const params = "userId=" + this.userId + "&postId=" + this.postId + "&title=" + this.title + "&caption=" + this.caption + "&image=" + this.image;
      axios.post(path, params)
        .then(() => {
          this.$router.push('/post/' + this.postId);
        })
        .catch((error) => {
          console.log(error);
        });
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
  max-width: 900px;
  align-items: left;
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

input[type="text"],
input[type="url"],
textarea {
  padding: 0.5rem;
  font-size: 1rem;
  border: none;
  border-radius: 3px;
  max-width: 98%;
  width: 100%;
  background-color: azure;
}

textarea {
    height: 200px;
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

input[type="file"] {
    padding: 0.5rem;
    /* Dark blue */
    /* color: #fff; */
    border: none;
    border-radius: 3px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    width: auto;
}

.upload {
    display: flex;
    flex-direction: column;
    justify-content: left;
    align-items: left;
     
}

#image {
    color: black;
}

img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
    margin-top: 1rem;
}
</style>  