import Index from "@/pages/Index.vue"
import AddItemToDb from "@/pages/AddItemToDb.vue"
import { createRouter, createWebHashHistory, createWebHistory } from "vue-router"
import Cart from "@/pages/Cart.vue"
import Profile from "@/pages/Profile.vue"
import Cpu from "@/pages/Cpu.vue"
import Case from "@/pages/Case.vue"
import CaseCooler from "@/pages/CaseCooler.vue"
import CpuCooler from "@/pages/CpuCooler.vue"
import Motherboard from "@/pages/Motherboard.vue"
import Psu from "@/pages/Psu.vue"
import Prebuilt from "@/pages/Prebuilt.vue"
import Ram from "@/pages/Ram.vue"
import Thermal from "@/pages/Thermal.vue"
import Videocard from "@/pages/Videocard.vue"

const routes = [
    {
        path: '/',
        component: Index
    },
    {
        path: '/add_item',
        component: AddItemToDb
    },
    {
        path: '/cart',
        component: Cart
    },
    {
        path: '/profile',
        component: Profile
    },
    {
        path: '/cpu',
        component: Cpu
    },
    {
        path: '/case',
        component: Case
    },
    {
        path: '/case_cooler',
        component: CaseCooler
    },
    {
        path: '/cpu_cooler',
        component: CpuCooler
    },
    {
        path: '/motherboard',
        component: Motherboard
    },
    {
        path: '/psu',
        component: Psu
    },
    {
        path: '/prebuilt',
        component: Prebuilt
    },
    {
        path: '/ram',
        component: Ram
    },
    {
        path: '/thermal',
        component: Thermal
    },
    {
        path: '/videocard',
        component: Videocard
    },
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;