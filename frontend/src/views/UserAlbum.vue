<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-4 text-center">
        <img :src="'http://127.0.0.1:5000/album/' + album.id" alt="Album Cover" class="album-cover shadow" />
      </div>
      <div class="col-md-8">
        <h1 class="display-3 mb-4">{{ album.title }}</h1>
        <h2 class="mt-4 text-muted"><strong>Artist:</strong> {{ album.artist.name }}</h2>
      </div>
    </div>
    <p class="lead mt-4">{{ album.description }}</p>
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h2 class="text-muted">Songs</h2>
    </div>
    <div class="table-responsive">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>Song ID</th>
            <th>Song Cover</th>
            <th>Title</th>
            <th>Genre</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="song in album.songs" :key="song.id">
            <td>{{ song.id }}</td>
            <td>
              <img :src="'http://127.0.0.1:5000/song/cover/' + song.id" alt="Song Cover" class="song-cover shadow" />
            </td>
            <td>{{ song.title }}</td>
            <td>{{ song.genre }}</td>
            <td>
              <a :href="'/play/song/'+song.id" class="btn btn-success me-2">
                <i class="fa-solid fa-play"></i>
              </a>
              <button type="button" class="btn btn-primary">
                <i class="fa-solid fa-plus"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id: localStorage.getItem('user_id'),
      album: this.$route.meta.album
    }
  },
  name: 'UserAlbum'
}
</script>

<style scoped>
.container {
  margin-top: 50px;
  max-width: 1200px;
}

.new {
  margin-top: 250px;
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
  transition: background-color 0.3s, border-color 0.3s;
}

.btn-success:hover {
  background-color: #218838;
  border-color: #218838;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  transition: background-color 0.3s, border-color 0.3s;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-danger {
  background-color: #dc3545;
  border-color: #dc3545;
  transition: background-color 0.3s, border-color 0.3s;
}

.btn-danger:hover {
  background-color: #c82333;
  border-color: #c82333;
}

h2 {
  margin: 30px 0 30px 0;
}

.album-cover {
  width: 300px;
  height: 300px;
  border-radius: 10px;
  margin: 0 auto 20px;
}

.song-cover {
  width: 100px;
  height: 100px;
  border-radius: 5px;
}

.table {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f8f9fa;
}

.table-hover > tbody > tr:hover {
  background-color: #e9ecef;
}

.shadow {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1) !important;
}
</style>