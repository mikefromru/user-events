new Vue({
    el: '#sign-up',
    data() {
        return {
            username: '',
            first_name: '',
            last_name: '',
            password: '',
            password_confirm: '',
            errors: {},
        }
    },
    methods: {
        register() {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            payload = {
                'username': this.username,
                'first_name': this.first_name,
                'last_name': this.last_name,
                'password': this.password,
                'password_confirm': this.password_confirm,
            }
            axios.post('/accounts/register/', body=payload)
            .then(response => (
                window.location.href = '/'
            ))
            .catch(error => {
                this.errors = error.response.data
                // console.log(this.errors_, ' <<< error')
            })
        }
    }
})