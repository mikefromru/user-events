new Vue({
    el: '#app',
    data() {
        return {
            msg: 'Hi Django from Vue.js',
            lst: [],
        }
    },
    mounted() {
        axios.get('api/v1/app/events/')
        .then(response => (
            this.lst = response.data
        ))
        .catch(function (error) {
            if (error.response) {
                // console.log(error.response.data)
                if (error.response.status == 401) {
                    console.log('401')
                    // window.location.href = '/login/';

                }

            }
        })
    }
})