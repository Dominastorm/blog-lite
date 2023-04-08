<template>
  <button
    :class="{'button follow': !followed, 'button unfollow': followed}"
    @click="toggleFollow"
  >
    {{ followed ? 'Unfollow' : 'Follow' }}
  </button>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    followed: {
      type: Boolean,
      required: true,
    },
    followerId : {
      type: String,
      required: true,
    }
  },
  computed: {
    userId() {
      return localStorage.getItem('userId')
    },
  },
  methods: {
    follow() {
      const path = `http://localhost:5000/follow`
      const params = "followerId=" + this.followerId + "&userId=" + this.userId
      axios.post(path, params)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    unfollow() {
      const path = `http://localhost:5000/unfollow`
      const params = "followerId=" + this.followerId + "&userId=" + this.userId
      axios.post(path, params)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    toggleFollow() {
      if (this.followed) {
        this.unfollow()
      } else {
        this.follow()
      }
      this.$emit('toggle-follow')
    },
  },
}
</script>

<style>
.button {
  width: 125px;
  margin-right: 2rem;
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

.unfollow:hover {
  background-color: #d81616;
}

.follow:hover {
  background-color: #06690e;
}
</style>
