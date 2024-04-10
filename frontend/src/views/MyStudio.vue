<template>
  <div v-if="albumExists">
    <div class="container mt-5">
      <h1 class="display-3 mb-4 text-center">My Albums</h1>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h2 class="text-muted">Albums</h2>
        <router-link to="/create-album" class="btn btn-success btn-lg">
          <i class="fas fa-plus"></i> Add Album
        </router-link>
      </div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Album ID</th>
            <th>Album Cover</th>
            <th>Title</th>
            <th>No of Songs</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="album in albums" :key="album.id">
            <td>{{ album.id }}</td>
            <td>
              <img :src="'http://127.0.0.1:5000/album/' + album.id" alt="Album Cover" style="width: 100px; height: 100px;" />
            </td>
            <td>{{ album.title }}</td>
            <td>{{ getNumberOfSongs(album) }}</td> 
            <td>
              <a :href="'/album/' + album.id" class="btn btn-info me-2">
                  <i class="fas fa-search"></i> Show
              </a>
              <a :href="'/album/edit/' + album.id" class="btn btn-warning me-2">
                <i class="fas fa-edit"></i> Edit
              </a>
              <button type="button" class="btn btn-danger" @click="deleteAlbum(album.id)">
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
      <h1 class="display-3 text-center">Welcome to MyStudio</h1>
      <p class="lead text-center">You have not created any albums yet. Click the button below to create your first album.</p>
      <div class="d-flex justify-content-center">
        <router-link to="/create-album" class="btn btn-success btn-lg">Create Album</router-link>
      </div>
    </div>
  </div>
</template>



<script>

export default {

  data() {
				return {
          user_id: localStorage.getItem('user_id'),

          albums: this.$route.meta.data,

          albumExists: this.$route.meta.albumExists
          
        }
		},
    

		methods: {
        getNumberOfSongs(album) {
          if (album.songs && album.songs.length) {
            return album.songs.length;
          } else {
            return 0; // Return 0 if album.songs is undefined or empty
          }
        },
				async deleteAlbum(id) {
          try {
            const token = localStorage.getItem('token');
            const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/albums/${id}/delete`, {
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

		name: 'MyStudio'
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