<template>
    <div class="post-list">
        <div v-for="post in posts" :key="post.id" class="post">
            <img :src="post.image" alt="Post Image">
            <h4>{{ post.title }}</h4>
            <p>{{ post.caption }}</p>
            <p>{{ post.content }}</p>
        </div>
    </div>
</template>
  
<script>
export default {
    name: 'PostList',
    props: {
        posts: {
            type: Array,
            required: true
        }
    }
}
</script>
  
<style scoped>
.post-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.post {
    width: 30%;
    margin-bottom: 30px;
    border: 1px solid #ccc;
    padding: 20px;
}

.post img {
    width: 100%;
    margin-bottom: 10px;
}

.post h4 {
    font-size: 18px;
    margin-bottom: 10px;
}

.post p {
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 10px;
}
</style>
  