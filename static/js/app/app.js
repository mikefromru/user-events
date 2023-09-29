new Vue({
    // delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            all_events: [],
            detail_event: {},
            user_events: [],
            flag: false,
        }
    },
    methods: {
        get_event(ev) {
            this.detail_event = ev
            this.flag = true
            
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
                this.all_events = response.data
            ))
        axios.get('api/v1/app/')
            .then(response => (
                this.user_events = response.data
                // console.log(response.data)
            ))
    }
})