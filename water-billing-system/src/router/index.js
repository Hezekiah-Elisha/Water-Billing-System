import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TestView from '../views/TestView.vue'
import OneSupervisorViewVue from '@/views/OneSupervisorView.vue';


function guardMyRoute (to, from, next){
  //this route requires auth, check if logged in
  //if not, redirect to login page
  var isAuthenticated = false;

  if (localStorage.getItem('token') != null){
    isAuthenticated = true;
  } else {
    isAuthenticated = false;
  }

  if(isAuthenticated){
    next() //allow to enter route
  }else{
    next('/login') //go to '/login';
  }
}


const routes = [
  {
    path: '/home',
    name: 'home',
    // beforeEnter: guardMyRoute,
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/',
    name: 'dashboard',
    beforeEnter: guardMyRoute,
    component: () => import('../views/DashboardView.vue')
  }
  ,
  {
    path: '/:notFound(.*)',
    name: 'notFound',
    component: () => import('../views/404View.vue')
  }
  ,{
    path: '/users',
    name: 'users',
    component: () => import('../views/UsersView.vue')
  },
  {
    path: '/supervisors',
    name: 'supervisors',
    beforeEnter: guardMyRoute,
    component: () => import('../views/SupervisorView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/supervisor/:id',
    name: 'supervisor',
    beforeEnter: guardMyRoute,
    component: OneSupervisorViewVue
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
