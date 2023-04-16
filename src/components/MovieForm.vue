

<template>
    <form @submit.prevent="saveMovie" method="post" id="movieForm" class="row g-3" >
        <h1>Upload Movie Form</h1>
        <div class="alert alert-danger" v-if="errorM">
            <ul>
                <li v-for="aError in errorM" v-bind:key="aError.id" >
                    {{ aError }}
                </li>
            </ul>
        </div>
        <div class="alert alert-success" v-if="successM">
            {{successM}}
        </div>
        <div class="form-group mb-3">
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control" placeholder="Movie Title here..." />
        </div>
        <div class="form-group mb-3">
            <label for="description" class="form-label">Movie Description</label>
            <input type="text" name="description" class="form-control" placeholder="Movie Description here..." />
        </div>
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Movie Poster</label>
            <input type="file" name="poster" class="form-control" />
        </div>
        <div class="col-12">
            <button class="btn btn-primary" type="submit">Add Movie</button>
        </div>
    </form>

</template>


<script setup>

    import { ref, onMounted } from 'vue';
    let csrf_token = ref("");
    let successM = ref("");
    let errorM =ref("");

    const saveMovie=() => {

        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
    
        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
            'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
        return response.json();
        })
        .then(function (data) {
        // display a success message
        if("message" in data){
            console.log(data);
            successM.value =data.message
            clearForm();

        }else if ("errors" in data){
            console.log(data);
            errorM.value=data.errors
        }
        
        })
        .catch(function (error) {
        console.log(error);
        });

    }
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }

    onMounted(() => {
        getCsrfToken();
    });


</script>

<style scoped>

.form-label{
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight:500;
}

.form-control{
    border: 2px solid rgb(19, 19, 135)
}
</style>
