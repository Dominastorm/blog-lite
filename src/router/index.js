import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/FeedView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUpView.vue')
    },
    {
      path: '/feed',
      name: 'feed',
      component: () => import('../views/FeedView.vue')
    },
    {
      path: '/profile/:userId',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/following/:userId',
      name: 'following',
      component: () => import('../views/FollowingView.vue')
    },
    {
      path: '/followers/:userId',
      name: 'followers',
      component: () => import('../views/FollowersView.vue')
    },
    {
      path: '/search',
      name: 'search',
      component: () => import('../views/SearchView.vue')
    },
    {
      path: '/post/:postId',
      name: 'post',
      component: () => import('../views/PostView.vue')
    },
    {
      path: '/createpost',
      name: 'createpost',
      component: () => import('../views/CreatePostView.vue')
    },
    {
      path: '/editpost/:postId',
      name: 'editpost',
      component: () => import('../views/EditPostView.vue')
    }
  ]
})

export default router
