<template>
  <div class="buttons">
    <button class="export button" v-on:click="exportAllPosts">Export All</button>
  </div>
  <div class="post-list">
    <div v-for="post in posts" :key="post.id" class="post">
      <router-link :to="'/post/' + post.id" style="text-decoration: none; color: white;">
        <img :src="post.image" alt="Post Image">
        <h4>{{ post.title }}</h4>
        <p v-html="post.caption"></p>
      </router-link>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios'

export default {
  name: 'PostList',
  props: {
    view: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      posts: []
    }
  },
  methods: {
    getPosts(userId) {
      const path = `http://localhost:5000/${this.view}/${userId}`;
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
    },
    exportAllPosts() {
      // Define the header for the CSV file
      const header = "Title,Image,Caption,Username,Timestamp\n";

      // Initialize the CSV content string with the header
      let csvContent = header;

      // Loop through all the posts and append their data to the CSV content string
      for (const post of this.posts) {
        const data = `"${post.title}","${post.image}","${post.caption}","${post.username}","${post.timestamp}"\n`;
        csvContent += data;
      }

      // Create a download link for the CSV file
      const encodedUri = encodeURI("data:text/csv;charset=utf-8," + csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "all_posts.csv");
      document.body.appendChild(link);

      // Trigger a click on the download link to initiate the download
      link.click();
    }
  },
  created() {
    const userId = localStorage.getItem('userId');
    this.getPosts(userId);
  },
  async mounted() {
    this.interval = setInterval(() => {
      this.exportAllPosts()
    }, 10000)
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

.export:hover {
  background-color: #d89e00ee;
}
</style>
