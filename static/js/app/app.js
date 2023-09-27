new Vue({
    el: '#app',
    data() {
        return {
            msg: 'hi django from APP vue.js',
            events: [],
            token: false,
        }
    },
    mounted() {
        axios.get('api/v1/app/events/')
            .then(response => (
                this.events = response.data
            ))
    }
})