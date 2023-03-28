<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SharkMessage',
    data() {
        return {
            msg: ''
        }
    },
    methods: {
        getResponse() {
            const path = 'http://localhost:5000/shark';
            axios.get(path)
                .then(response => {
                    console.log(response.data)
                    this.msg = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
    created() {
        this.getResponse();
    }
}
</script>