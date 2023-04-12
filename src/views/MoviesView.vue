<template> 
    <div class="movies">
        <h1>Movies</h1>
        <div class="movie-cards">
            <div v-for="movie in movies" :key="movie.id" class="movie-card">
                <img :src="movie.poster" alt="Movie poster" />
                <h2>{{ movie.title }}</h2>
                <p>{{ movie.description }}</p>
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

const fetchMovies= () =>{
    fetch("/api/v1/movies", {
        method: 'GET'
    })
    .then(function (response) {
    return response.json();
    })
    .then(function (data) {
    // display a success message
    console.log(data);
    movies.value=data;
    })
    .catch(function (error) {
    console.log(error);
    });
    }

onMounted(fetchMovies);


</script>

<style scoped>
.movies {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.movie-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 20px;
}

.movie-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
}

.movie-card img {
  max-width: 100%;
  height: auto;
  margin-bottom: 10px;
}
</style>


