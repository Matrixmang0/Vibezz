<template>
  <div class="main-container">
    <div class="carousel">
      <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active" data-bs-interval="3000">
            <div class="carousel-image"><img src='http://127.0.0.1:5000/carousel/1' class="d-block w-100" alt="..."></div>
            <div class="carousel-caption d-none d-md-block">
              <div class="text-white carousel-text">
                <h2>Discover Your Sound</h2>
                <p>Pump up the Volume with Our Diverse Music Library</p>
              </div>
            </div>
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <div class="carousel-image"><img src='http://127.0.0.1:5000/carousel/2' class="d-block w-100" alt="..."></div>
            <div class="carousel-caption d-none d-md-block">
              <div class="text-white carousel-text">
                <h2>A World of Music Awaits</h2>
                <p>Indulge Your Ears with Endless Musical Delights</p>
              </div>
            </div>
          </div>
          <div class="carousel-item" data-bs-interval="3000">
            <div class="carousel-image"><img src='http://127.0.0.1:5000/carousel/3' class="d-block w-100" alt="..."></div>
            <div class="carousel-caption d-none d-md-block">
              <div class="text-white carousel-text">
                <h2>Explore Infinite Beats</h2>
                <p>Your Gateway to Music: Listen, Love, Repeat</p>
              </div>
            </div>
          </div>
        </div>
        <div class="carousel-controls">
          <div class="left-button">
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
          </div>
          <div class="right-button">
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="showcase-albums">
      <div v-for="album in filtered_albums" class="album-container">
        <a :href="'user/album/' + album.id">
          <h2 class="album-title">{{ album.title }}</h2>
        </a>
        <div class="flex-container">
          <div class="arrow arrow-left" onclick="scrollList('left')"><i class="fa-solid fa-arrow-left"></i></div>
          <div class="scroll-container">
            <div v-for="song in album.songs" class="card">
              <a :href="'/play/song/'+song.id">
                <img :src="'http://127.0.0.1:5000/song/cover/'+ song.id " class="card-img-top" height="200px" width="300px" alt="...">
              </a>
              <div class="card-body">
                <a :href="'/play/song/'+song.id">
                  <h6 class="card-title"><strong>{{ song.title }}</strong></h6>
                </a>
                <div class="card-buttons">
                  <!-- {% if book.quantity > 0 %}
                    <a href="" method="post" class="btn btn-success btn-sm">Add to cart</a>
                    <button class="btn btn-primary btn-sm">Borrow</button>            
                  {% else %}
                    <button class="btn btn-outline-danger btn-sm" disabled><i class="fa-solid fa-x"></i>  Out of stock</button>
                  {% endif %} -->
                </div>
              </div>
            </div>
          </div>
          <div class="arrow arrow-right" onclick="scrollList('right')"><i class="fa-solid fa-arrow-right"></i></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      albums: this.$route.meta.albums,
      f_albums: ''
    }
  },
  computed: {
    ...mapState(['searchQuery', 'selectedParameter']),

    filtered_albums() {
      const parameter = this.$store.state.selectedParameter;
      const query = this.$store.state.searchQuery.toLowerCase();

      if (parameter == 0 && query) {
        this.f_albums = this.albums.filter(album => album.title.toLowerCase().includes(query));
      } else if (parameter == 1 && query) {
        this.f_albums = this.albums.map(album => {
          return {
            ...album,
            songs: album.songs.filter(song => song.title.toLowerCase().includes(query))
          };
        }).filter(album => album.songs.length > 0);
      } else {
        this.f_albums = this.albums;
      }

      return this.f_albums;
    },
  },

  name: 'Home',
}
</script>

<style scoped>
.main-container {
  background-color: #f4f4f4;
  padding: 20px;
}

.carousel {
  margin-bottom: 40px;
}

.carousel-image {
  width: 100%;
  height: 420px;
}

.carousel-text {
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.showcase-albums {
  display: flex;
  flex-direction: column;
}

.album-container {
  margin-bottom: 40px;
}

.album-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #333;
}

.flex-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.scroll-container {
  display: flex;
  overflow-x: auto;
  flex-wrap: nowrap;
  width: 95%;
  margin: 0 auto;
}

.scroll-container::-webkit-scrollbar {
  display: none;
}

.card {
  flex: 0 0 auto;
  margin: 0 10px;
  width: 12rem;
  height: 16rem;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.card:hover {
  transform: translateY(-5px);
}

.card-body {
  padding: 10px;
}

.card-title {
  font-size: 14px;
  margin-bottom: 10px;
  color: #333;
}

.card-buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.arrow {
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  font-size: 20px;
  color: #333;
  margin-left: 5px;
  margin-right: 5px;
}

.arrow-left {
  right: 5px;
}

.arrow-right {
  left: 5px;
}

a {
  color: inherit;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
  color: #007bff;
}
</style>