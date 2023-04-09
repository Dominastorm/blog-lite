<template>
  <div>
    <NavBar />
    <h2>Feed</h2>
    <PostList view="feed"/>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from '@/components/NavBar.vue'
import PostList from '../components/PostList.vue';

export default {
  components: {
    NavBar,
    PostList
  },
  computed: {
      userId() {
        return localStorage.getItem('userId');
    }
  },
  methods: {
    sendMesage(userId) {
      const path = 'http://localhost:5000/mylatestpost/' + userId;
      axios.get(path)
        .then((response) => {
          let postedTime = Date.parse(response.data.post.timestamp);
          let currentTime = new Date().getTime();
          console.log(typeof(postedTime));
          console.log(currentTime);
          console.log(currentTime - postedTime);
        })
        .catch((error) => {
          console.log(error);
        });

        let timeDiff = Math.abs(this.currentTime - this.postedTime);
        timeDiff = Number(timeDiff);
        let notPostedToday = timeDiff < 86400000;
        notPostedToday = true;
      
        if (notPostedToday) {
          let data = { "text": "You have not posted today" }
          fetch("https://chat.googleapis.com/v1/spaces/AAAA4dtClys/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=LnsiHVVy4qIokEI6_GqXFk7Z-IsBqs0IEN5fYF6HcZo%3D", {
            method: "POST",
            body: JSON.stringify(data)
          }).then(r => r.json()).then(d => console.warn(d)).catch(e => console.warn("Err", e))
        }
    },
  },
  created() {
    this.interval = setInterval(() => {
      this.sendMesage(this.userId)
    }, 10000)
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
