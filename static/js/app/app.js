new Vue({
    el: '#app',
    data() {
        return {
            msg: 'hi django from APP vue.js',
            events: [],
            token: false,
        }
    },
    methods: {
        logout() {
            console.log('logout')
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios.post('/accounts/logout/', {'revoke_token': true})
            .then(response => (
                console.log(response.data),
                window.location.reload()
            ))
        }
    },
    mounted() {
        axios.get('api/v1/app/events/')
            .then(response => (
                this.events = response.data
            ))
    }
})