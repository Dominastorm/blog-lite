<template>
    <div>
      <NavBar user="John Doe" :userId="1" />
      <h2>Following</h2>
      <div class="box">
        <ul>
          <div v-for="user in following" :key="user.id" class="list-item">
            <div class="link">{{ user.username }}</div>
            <button class="button" @click="unfollow(user.id)">Unfollow</button>
          </div>
        </ul>
      </div>
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
            following: [
                {
                    id: 1,
                    username: 'exampleuser1'
                },
                {
                    id: 2,
                    username: 'exampleuser2'
                },
                // Add more followed users here
            ]
        }
    },
    methods: {
        unfollow(userId) {
            // Send an API request to unfollow the user with the given ID
            console.log('Unfollowing user', userId);
        }
    }
}
</script>
  

<style>
body {
    background-color: #2c3e50;
    /* Dark blue */
    color: #fff;
    font-family: sans-serif;
}

h2 {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
    text-align: center;
}

.box {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    width: 100%;
    margin: 0 auto;
    padding: 2rem;
    /* Light blue */
    background-color: #2980b9;
    border-radius: 5px;
}


router-link {
    flex-grow: 1;
    margin-right: 10px;
}

button {
    flex-shrink: 0;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.link {
  flex-grow: 1;
  margin-bottom: 1rem;
}

.button {
  margin-right: 2rem;
  margin-bottom: 1rem;
  padding: 0.5rem 2rem;
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

.button:hover {
  background-color: #d81616;
}

</style>