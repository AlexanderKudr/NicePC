import axios from "axios"

export const AuthModule = {
    namespaced: true,


    state() {
        return {
            credentials: {
                token: localStorage.getItem('token') || null,
                // userRole: localStorage.getItem('userRole') || userRoles.Guest
            }
        }
    },
    getters: {
        // getUserRole: (state) => state.credentials.userRole,
    },

    mutations: {
        setToken(state, token) {
            state.credentials.token = token
            localStorage.setItem('token', token)
        },

        // setUserRole(state, userRole) {
        //     state.credentials.userRole = userRole
        //     localStorage.setItem('userRole', userRole)
        // },

        deleteToken(state) {
            state.credentials.token = null
            localStorage.removeItem('token')
        },

        // deleteUserRole(state) {
        //     state.credentials.userRole = null
        //     localStorage.removeItem('userRole')
        // }
    },

    actions: {
        async onLogin({commit}, {login, password}) {
            var qs = require('qs')
            await axios.post('http://127.0.0.1:8000/login', qs.stringify({'username': login, 'password': password})).then((res) => {
                commit('setToken', res.data.access_token)
                // commit('setUserRole', res.userRole)
                axios.defaults.headers.common['authorization'] = `Bearer ${res.data.access_token}`
            })

        },

        onLogout({commit}) {
            commit('deleteToken')
            // commit('deleteUserRole')
        }
    }
}
