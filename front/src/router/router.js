import Index from "@/pages/Index.vue"
import Cpu from "@/pages/Cpu.vue"
import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"

const routes = [
    {
        path: '/',
        component: Index
    },
    {
        path: '/cpu',
        component: Cpu
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;