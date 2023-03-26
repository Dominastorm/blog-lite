import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/LoginView.vue'),
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
      path: '/profile/:id',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/following/:id',
      name: 'following',
      component: () => import('../views/FollowingView.vue')
    },
    {
      path: '/followers/:id',
      name: 'followers',
      component: () => import('../views/FollowersView.vue')
    },
    {
      path: '/blogpost',
      name: 'blogpost',
      component: () => import('../views/BlogPostView.vue')
    }
  ]
})

export default router
