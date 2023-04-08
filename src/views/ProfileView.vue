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
        <div>Following: <router-link :to="/following/ + userId" style="color: white">{{ followingCount }}</router-link></div>
        <div>Followers: <router-link :to="/followers/ + userId" style="color: white">{{ followersCount }}</router-link></div>
      </div>
    </div>
    <h3>My Posts</h3>
    <PostList :posts="posts" />
  </div>
</template>

<script>
import axios from 'axios';

import PostList from '../components/PostList.vue';
import NavBar from '../components/NavBar.vue';

export default {
  components: {
    PostList,
    NavBar
  },
  computed: {
    userId() {
      return window.location.href.split('/').pop();
    }
  },
  data() {
    return { 
      profileImage: '/assets/dominastorm.jpeg', // replace with your profile image URL
      totalPosts: 0, 
      followingCount: 0, 
      followersCount: 0,
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
    getProfile(userId) {
      const path = 'http://localhost:5000/profile/' + userId;
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          const profileDetails = response.data.profileDetails;
          this.totalPosts = profileDetails.totalPosts;
          this.followingCount = profileDetails.followingCount;
          this.followersCount = profileDetails.followersCount;
          console.log(response.data.profileDetails)
        })
        .catch((error) => {
          console.log(error)
        })  
    }
  },
  created() {
    this.getProfile(this.userId);
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
  