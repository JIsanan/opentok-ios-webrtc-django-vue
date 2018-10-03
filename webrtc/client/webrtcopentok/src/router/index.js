import Vue from 'vue'
import Router from 'vue-router'
import OpenTok from '@/components/OpenTok'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'OpenTok',
      component: OpenTok
    }
  ]
})
