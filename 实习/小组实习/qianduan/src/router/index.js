import VueRouter from 'vue-router';

const routes = [
    {
        path:'/',
        name:'Home',
        component:()=>import('../components/login')
    },{
        path:'/mapcomponent',
        name:'mapcomponent',
        component:()=>import('../components/mapcomponent')
    }
]

const router = new VueRouter({
    mode:'history',
    routes
})

export function resetRouter() {
    router.matcher = new VueRouter({
        mode:'history',
        routes: []
    }).matcher
}
const VueRouterPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (to) {
    return VueRouterPush.call(this, to).catch(err => err)
}
export  default router;