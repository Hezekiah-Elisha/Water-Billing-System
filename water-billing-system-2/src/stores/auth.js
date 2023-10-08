import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: '',
        user: {},
    }),
    getters: {
        isLoggedIn: (state) => !!state.token,
    },
    actions: {
        login(token, user) {
        this.token = token
        this.user = user
        },
        logout() {
        this.token = ''
        this.user = {}
        },
    },
});

    // ```
    // - `useAuthStore` is a function that returns a store object. The first argument is the name of the store, and the second argument is an object with the store's state, getters, and actions.
    // - The `state` function returns an object with the store's state. In this case, the state has two properties: `token` and `user`.
    // - The `getters` object contains the store's getters. In this case, there is only one getter, `isLoggedIn`, which returns a boolean value indicating whether the user is logged in.
    // - The `actions` object contains the store's actions. In this case, there are two actions: `login` and `logout`.
    // - The `login` action takes two arguments: `token` and `user`. The `token` argument is a string containing the user's authentication token, and the `user` argument is an object containing the user's information.
    // - The `logout` action takes no arguments.
    // - The `useAuthStore` function returns a store object with the following properties:
    // - `state`: An object containing the store's state.
    // - `getters`: An object containing the store's getters.
    // - `actions`: An object containing the store's actions.
