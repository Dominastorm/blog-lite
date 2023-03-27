<template>
  <div>
    <NavBar user="John Doe" :userId="1" />
    <h2>Feed</h2>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>{{ post.content }}</p>
        <small>By {{ post.author }} on {{ formatDate(post.date) }}</small>
      </li>
    </ul>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  components: {
    NavBar
  },
  data() {
    return {
      posts: []
    }
  },
  created() {
    // Fetch blog posts from your API
    this.posts = [
      {
        id: 1,
        title: 'First post',
        content: 'This is the first post.',
        author: 'John Doe',
        date: '2022-01-01T00:00:00Z'
      },
      {
        id: 2,
        title: 'Second post',
        content: 'This is the second post.',
        author: 'Jane Doe',
        date: '2022-01-02T00:00:00Z'
      }
    ]
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString)
      return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
    }
  }
}
</script>


<style >
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

p {
  font-size: 1.2rem;
  margin-top: 1rem;
}

a {
  color: #fff;
  text-decoration: underline;
}

a:hover {
  color: #eee;
}
</style>
