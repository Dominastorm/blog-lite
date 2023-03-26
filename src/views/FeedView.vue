<template>
    <div>
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
  export default {
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
  