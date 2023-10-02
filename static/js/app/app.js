new Vue({
    // delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            all_events: [],
            detail_event: {},
            user_events: [],
            name_button: '',
            currrent_user_id: null,
            flag: false,
            user_info: {},
            show_detail_even_block: true,
            show_user_info: false,
        }
    },
    methods: {
        participate_or_stop(x) {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            id_event = this.detail_event.id + '/'
            axios.patch('/api/v1/app/event/' + id_event)
                .then(response => {
                    this.detail_event = response.data
                    let index = this.all_events.findIndex(x => x.id === this.detail_event.id)
                    if (index !== -1) {
                        this.all_events[index] = this.detail_event
                        console.log('updated successfuly')
                    }else{
                        console.log('Nothing changed')
                    }
                })

            exists = this.detail_event.participants.some(obj => obj.id == this.currrent_user_id)
            if (exists) {
                this.name_button = 'Принять участие'
            }else{
                this.name_button = 'Отказаться от участия'
            }

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
        get_name_for_button(ev) {
            let exists = ev.participants.some(obj => obj.id == this.currrent_user_id)
            if (exists) {
                this.name_button = 'Отказаться от участия'
            }else{
                this.name_button = 'Принять участие'
            }

        },
        get_event(ev) {
            this.detail_event = ev
            this.flag = true
            this.close()
            this.get_name_for_button(ev)
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
        this.currrent_user_id = JSON.parse(document.getElementById('user_id').textContent);
    }
})