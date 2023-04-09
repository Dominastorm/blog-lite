<template>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id" class="post">
      <img :src="post.image" alt="Post Image">
      <h4>{{ post.title }}</h4>
      <p>{{ post.caption }}</p>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios'

export default {
  name: 'PostList',
  data() {
    return {
      posts: []
    }
  },
  methods: {
    getPosts(userId) {
      const path = 'http://localhost:5000/feed/' + userId;
      console.log(path);
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.posts = response.data.posts;
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {
    const userId = localStorage.getItem('userId');
    this.getPosts(userId);
  }
}

</script>
  
<style scoped>
.post-list {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-top: 2rem;
}

.post {
  width: 300px;
  /* Light blue */
  background-color: #2980b9;
  border-radius: 5px;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: box-shadow 0.3s ease-in-out;
}

.post:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.post img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 5px;
  margin-bottom: 1rem;
}

.post h4 {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.post p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}
</style>
  