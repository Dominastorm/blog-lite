<template>
  <button
    :class="{'button follow': !followed, 'button unfollow': followed}"
    @click="toggleFollow"
  >
    {{ followed ? 'Unfollow' : 'Follow' }}
  </button>
</template>

<script>
export default {
  props: {
    followed: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    toggleFollow() {
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
