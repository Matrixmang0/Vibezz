<template>
  <div v-if="playlistExists">
    <div class="container mt-5">
      <h1 class="display-3 mb-4 text-center">My Albums</h1>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h2 class="text-muted">Albums</h2>
        <router-link to="/create-album" class="btn btn-primary btn-lg">
          <i class="fas fa-plus"></i> Add Album
        </router-link>
      </div>
      <div class="table-responsive">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th>Song ID</th>
              <th>Album Cover</th>
              <th>Title</th>
              <th>Genre</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="album in albums" :key="album.id">
              <td>{{ album.id }}</td>
              <td>
                <img :src="'http://127.0.0.1:5000/album/' + album.id" alt="Album Cover" class="album-cover" />
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
  </div>
  <div v-else>
    <div class="container new">
      <h1 class="display-3 text-center">Welcome to Playlists</h1>
      <p class="lead text-center">You have not created any playlists yet. Click the button below to create your first playlist.</p>
      <div class="d-flex justify-content-center">
        <router-link to="/create-album" class="btn btn-primary btn-lg">Create Album</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_id: localStorage.getItem('user_id'),
      aplaylists: this.$route.meta.playlist,
      playlistExists: this.$route.meta.playlistExists
    }
  },
  methods: {
    getNumberOfSongs(album) {
      if (album.songs && album.songs.length) {
        return album.songs.length
      } else {
        return 0
      }
    },
    async deleteAlbum(id) {
      try {
        const token = localStorage.getItem('token')
        const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/albums/${id}/delete`, {
          method: 'delete',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
          }
        })
        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.message || 'Failed to delete album')
        }
        const data = await response.json()
        this.$store.dispatch('showMessage', data.message)
        this.$router.go()
      } catch (error) {
        console.error('Error deleting album:', error)
        this.$store.dispatch('showMessage', 'Failed to delete album')
      }
    }
  },
  name: 'Playlists'
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

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  transition: background-color 0.3s, border-color 0.3s;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

h2 {
  margin: 30px 0 30px 0;
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

.album-cover {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 4px;
}
</style>