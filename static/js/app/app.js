new Vue({
    // delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            all_events: [],
            detail_event: {},
            user_events: [],
            flag: false,
            user_info: {},
            show_detail_even_block: true,
            show_user_info: false,
        }
    },
    methods: {
        get_participate_or_stop(x) {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            id_event = this.detail_event.id + '/'
            axios.patch('/api/v1/app/event/' + id_event)
                .then(response => (
                    this.detail_event = response.data
                ))

        },
        close() {
            // hide user info block and show an event
            this.show_user_info = false
            this.show_detail_even_block = true
        },
        get_user_info(user) {
            this.user_info = user
            this.show_detail_even_block = false
            this.show_user_info = true
        },
        get_event(ev) {
            this.detail_event = ev
            this.flag = true
            this.close()

        },
        logout() {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            axios.post('/accounts/logout/', { 'revoke_token': true })
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