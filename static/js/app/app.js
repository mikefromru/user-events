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
                    // participants = this.detail_event.participants.find(obj => obj.id == 2),
                    // let event_ = this.all_events.find(obj => obj.id == 2)
                    // if (event_) {
                        // console.log(event_, ' event')
                    this.detail_event = response.data
                    let index = this.all_events.findIndex(x => x.id === 2)
                    console.log(index, ' kak')
                    if (index !== -1) {
                        console.log(this.all_events[index], ' << index')
                        console.log(this.detail_event, ' << detail event')
                        this.all_events[index] == this.detail_event
                        console.log('updated successfuly')
                        console.log(this.all_events, ' new')

                        // this.all_events[event_] = {}
                        // console.log(this.all_events[event_], ' must be changed')
                        // this. this.all_events[event_], ' must be changed')

                        // console.log(this.detail_event, ' this')
                        // console.log('I have it ', ' this')
                    }else{

                        console.log('NOOOO')
                    }
                    




                    // console.log(this.all_events, ' ALL EVENTS'),
                    // this.detail_event = response.data,
                    // item = this.detail_event.participants.find(obj => obj.id == this.currrent_user_id),
                    // console.log(item, ' ITEM'),
                    // console.log(this.all_events[item], ' first one'),
                    // this.all_events[item] == this.detail_event,
                    // console.log(this.all_events[item], ' second one')

                    // this.all_events = []
                })

            
            // console.log(this.detail_event, ' this is tmp')
            // item = this.detail_event.participants.find(obj => obj.id == this.currrent_user_id),

            // if (index !== -1) {
            //     console.log(this.all_events[index], ' << index')
            //     console.log(this.detail_event, ' << detail event')
            //     this.all_events[index] == this.detail_event
            //     console.log('updated successfuly')
            // }else{
            //     console.log('it not found')
            // }


            console.log('--------------')
            console.log(this.all_events)

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