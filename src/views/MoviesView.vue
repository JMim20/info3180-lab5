<template> 
  <div class="container">
    <h1>Movies</h1>
    <div class="row g-5 justify-content-evenly">
      <div v-for="movie in movies" :key="movie.id" class="col-6">
        <div class="card " >
          <div class="row g-0">
            <div class="col-6 col-md-5">
              <img :src="movie.poster" alt="movie.title"  class="card-img img-fluid"/>
            </div>
            <div class="col-6  col-md-7">
              <div class="card-body d-flex flex-column">
                <div class="h-100">
                  <h5 class="card-title">{{ movie.title }}</h5>
                  <p class="card-text">{{ movie.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
    <!-- <div class="movies">
        <h1>Movies</h1>
        <div class="movie-cards">
            <div v-for="movie in movies" :key="movie.id" class="movie-card">
                <img :src="movie.poster" alt="movie.title" />
                <h5>{{ movie.title }}</h5>
                <p>{{ movie.description }}</p>
            </div>
        </div>
    </div> -->
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
    movies.value=data.Addedmovies;
    })
    .catch(function (error) {
    console.log(error);
    });
    }

onMounted(fetchMovies);


</script>

<style scoped>

.card-img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0px;
}

.card{
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
}

/* .movies {
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
} */
</style>


