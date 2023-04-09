<template>
  <div>
    <NavBar />
    <h2>My Profile</h2>
    <div class="profile-info">
      <div class="profile-image">
        <img :src="profileImage" alt="Profile Image">
      </div>
      <div class="table-container">
        <table>
          <tr>
            <th>Total Posts</th>
            <th><router-link :to="/following/ + userId" style="text-decoration: none; color: white;">Following</router-link></th>
            <th><router-link :to="/followers/ + userId" style="text-decoration: none; color: white;">Followers</router-link></th>
          </tr>
          <tr>
            <td>{{ totalPosts }}</td>
            <td><router-link :to="/following/ + userId" style="text-decoration: none; color: white;">{{ followingCount }}</router-link></td>
            <td><router-link :to="/followers/ + userId" style="text-decoration: none; color: white;">{{ followersCount }}</router-link></td>
          </tr>
        </table>
      </div>
    </div>
    <h2>My Posts</h2>
    <PostList view="myposts" />
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
}

.profile-info {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #2980b9;
  padding: 20px;
  margin: 50px;
  border-radius: 10px;
}

.profile-image img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
}

.profile-stats {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-left: 50px;
  color: #fff;
  font-size: 1.2em;
  width: 400px;
}

.profile-stats div {
  margin: 10px 0;
}

.profile-stats div:first-child {
  font-size: 1.5em;
}

.profile-stats a {
  color: #fff;
  text-decoration: none;
}

.profile-stats a:hover {
  text-decoration: underline;
}

.table-container {
  padding: 10px;
  justify-content: center;
  align-items: center;
  margin-left: 50px;
}

table {
  border-collapse: collapse;
  width: 100%;
  color: white; /* set text color to white */
  font-size: 20px; /* increase font size to 16px */
}

th {
  padding: 10px;
  text-align: center;
}

td {
  padding: 10px;
  text-align: center;
}
</style>
  