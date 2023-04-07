<template>
  <div>
    <NavBar />
    <h2>My Profile</h2>
    <div class="profile-info">
      <div class="profile-image">
        <img :src="profileImage" alt="Profile Image">
      </div>
      <div class="profile-stats">
        <div>Total Posts: {{ totalPosts }}</div>
        <div>Following: <router-link to="/following/">{{ followingCount }}</router-link></div>
        <div>Followers: <router-link to="/followers/">{{ followersCount }}</router-link></div>
      </div>
    </div>
    <h3>My Posts</h3>
    <PostList :posts="posts" />
  </div>
</template>

<script>
import PostList from '../components/PostList.vue';
import NavBar from '../components/NavBar.vue';

export default {
  components: {
    PostList,
    NavBar
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
.profile-info {
  display: flex;
  align-items: center;
}

.profile-image {
  margin-right: 20px;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}

.profile-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.post-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
}

.post {
  border: 1px solid #ccc;
  padding: 10px;
}

.post img {
  width: 100%;
  height: auto;
  object-fit: cover;
}</style>
  