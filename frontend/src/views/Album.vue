<template>
  <div v-if="songExists">
    <div class="container mt-5">
      <h1 class="display-3 mb-4 text-center">{{ album.title }}</h1>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h2 class="text-muted">Songs</h2>
        <router-link to="/create-song" class="btn btn-success btn-lg">
          <i class="fas fa-plus"></i> Add Song
        </router-link>
      </div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Song ID</th>
            <th>Song Cover</th>
            <th>Title</th>
            <th>Genre</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="song in songs" :key="song.id">
            <td>{{ song.id }}</td>
            <td>
              <img :src="'http://127.0.0.1:5000/song/cover/' + song.id" alt="Song Cover" style="width: 100px; height: 100px;" />
            </td>
            <td>{{ song.title }}</td>
            <td>{{ song.genre }}</td> 
            <td>
              <a :href="'/song/edit/'+song.id" class="btn btn-warning me-2">
                <i class="fas fa-edit"></i> Edit
              </a>
              <button type="button" class="btn btn-danger" @click="deleteSong(song.id)">
                <i class="fas fa-trash"></i> Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div v-else>
    <div class="container new">
      <h1 class="display-3 text-center">{{ album.title }}</h1>
      <p class="lead text-center">You have not created any songs yet. Click the button below to create your first song in this album.</p>
      <div class="d-flex justify-content-center">
        <router-link to="/create-song" class="btn btn-success btn-lg">Create Song</router-link>
      </div>
    </div>
  </div>
</template>



<script>

export default {

  data() {
				return {
          user_id: localStorage.getItem('user_id'),

          songs: this.$route.meta.data,

          songExists: this.$route.meta.songExists,

          album: this.$route.meta.album
        }
		},
    

		methods: {
				async deleteSong(id) {
          try {
            const token = localStorage.getItem('token');
            const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/songs/${id}/delete`, {
              method: 'delete',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
              },
            });

            if (!response.ok) {
              // Handle non-successful response (status code other than 2xx)
              const errorData = await response.json();
              throw new Error(errorData.message || 'Failed to delete album');
            }

            const data = await response.json();
            this.$store.dispatch('showMessage', data.message);
            this.$router.go();
          } catch (error) {
            console.error('Error deleting album:', error);
            // Optionally, show an error message to the user
            this.$store.dispatch('showMessage', 'Failed to delete album');
          }
        }
    },

		name: 'Album'
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
  }

  .btn-success:hover {
    background-color: #218838; 
    border-color: #218838;
  }

  h2 {
    margin : 30px 0 30px 0;
  }
</style>