new Vue({
    // delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            events: [],
            my_event: {},
            token: false,
        }
    },
    methods: {
        get_event(ev) {
            this.my_event = ev
            console.log(ev)
            
        },
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