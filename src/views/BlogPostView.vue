<template>
  <div>
    <h2>Create a new Blog/Post</h2>
    <form @submit.prevent="createPost">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="title" required />
      </div>
      <div>
        <label for="caption">Caption:</label>
        <input type="text" id="caption" v-model="caption" required />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea id="content" v-model="content" required></textarea>
      </div>
      <div>
        <label for="image">Image:</label>
        <input type="file" id="image" @change="handleImageUpload" />
      </div>
      <div>
        <button type="submit">Create Post</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      content: '',
      image: null
    }
  },
  methods: {
    createPost() {
      // Your create post logic goes here
      console.log('Creating post...')
    },
    handleImageUpload(event) {
      this.image = event.target.files[0]
    }
  }
}
</script>
