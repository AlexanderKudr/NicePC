import Index from "@/pages/Index.vue"
import Cpu from "@/pages/Cpu.vue"
import SendCpu from "@/pages/SendCpu.vue"
import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"
import Cart from "@/pages/Cart.vue"

const routes = [
    {
        path: '/',
        component: Index
    },
    {
        path: '/cpu',
        component: Cpu
    },
    {
        path: '/add_cpu',
        component: SendCpu
    },
    {
        path: '/cart',
        component: Cart
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;