import axios from "axios"

export default {
    state() {
        return {
            credentials: {
                token: localStorage.getItem('token') || null,
                username: localStorage.getItem('username') || null
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

        setUsername(state, username) {
            state.credentials.username = username
            localStorage.setItem('username', username)
        },

        // setUserRole(state, userRole) {
        //     state.credentials.userRole = userRole
        //     localStorage.setItem('userRole', userRole)
        // },

        deleteToken(state) {
            state.credentials.token = null
            localStorage.removeItem('token')
        },

        deleteUsername(state) {
            state.credentials.username = null
            localStorage.removeItem('username')
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
                commit('setUsername', res.data.username)
                // commit('setUserRole', res.userRole)
                

            })

        },

        onLogout({commit}) {
            commit('deleteToken')
            commit('deleteUsername')
            // commit('deleteUserRole')
        }
    }
}
