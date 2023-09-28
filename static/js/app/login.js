console.log('fuck you motherfucker')

new Vue({
    // delimiters: ['[[', ']]'],
    el: '#login-app',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        myclick() {
            console.log('click on button')
        },
        login() {
            payload = {'login': 'admin', 'password': 'admin'}
            axios.post('accounts/login/', body=payload)
            .then(response => (
                // this.lst = response.data
                console.log(response.data),
                window.location.reload(),
                console.log('fucking log')
            ))
            .catch(function (error) {
                if (error.response) {
                    console.log('error.response.data')
                    if (error.response.status == 401) {
                        console.log('401')
                        // window.location.href = '/login/';

                    }

                }
            })
        },
    }
})

