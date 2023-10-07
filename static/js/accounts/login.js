console.log('<<<<< Helloo worlf >>>>>>')
new Vue({
    // delimiters: ['[[', ']]'],
    el: '#login-app',
    data() {
        return {
            username: '',
            password: '',
            errors: {},
        }
    },
    methods: {
        myclick() {
            console.log('click on button')
        },
        login() {
            payload = {'login': this.username, 'password': this.password}
            axios.post('/accounts/login/', body=payload)
            .then(response => (
                console.log(response.data),
                // window.location.reload()
                window.location.href = '/'
            ))
            .catch(error => {
                this.errors = error.response.data
            })
        },
    }
})

