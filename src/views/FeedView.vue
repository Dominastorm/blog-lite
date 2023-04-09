<template>
  <div>
    <NavBar />
    <h2>Feed</h2>
    <PostList view="feed"/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import PostList from '../components/PostList.vue';

export default {
  components: {
    NavBar,
    PostList
  },
  data() {
    return { 
      username: 'exampleuser',
      userId: 1, // replace with your user ID
      profileImage: '/assets/dominastorm.jpeg', // replace with your profile image URL
      totalPosts: 10, // replace with your total posts count
      followingCount: 5, // replace with your following count
      followersCount: 8, // replace with your followers count
      posts: [
        {
          id: 1,
          title: 'First Post',
          caption: 'My first post',
          content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
          image: '/assets/one.jpg' // replace with your post image URL
        },
        {
          id: 2,
          title: 'Second Post',
          caption: 'My second post',
          content: 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
          image: '/assets/two.jpg' // replace with your post image URL
        },
        // Add more posts here
      ]
    }
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString)
      return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`
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
