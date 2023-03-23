import Vue from 'vue'
import VueRouter from 'vue-router'
import UserList from '../components/UserList.vue'
import RoleList from '../components/RoleList.vue'
import PermissionList from '../components/PermissionList.vue'
import RolePermissionList from '../components/RolePermissionList.vue'
import AssignPermission from '../components/AssignPermission.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/users',
    name: 'UserList',
    component: UserList
  },
  {
    path: '/roles',
    name: 'RoleList',
    component: RoleList
  },
  {
    path: '/permissions',
    name: 'PermissionList',
    component: PermissionList
  },
  {
    path: '/roles/:role_id',
    name: 'RolePermissionList',
    component: RolePermissionList
  },
  {
    path: '/assign_permission',
    name: 'AssignPermission',
    component: AssignPermission
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router