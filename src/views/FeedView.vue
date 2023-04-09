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
