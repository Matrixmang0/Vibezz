<template>
  <div class="playlist-container">
    <div class="playlist-header">
      <h1 class="playlist-title">{{ playlist.title }}</h1>
    </div>

    <div class="playlist-content">
      <div class="playlist-songs" v-if="playlist.songs.length > 0">
        <div class="playlist-header">
          <h2 class="section-title">Songs in Playlist</h2>
          <button class="btn btn-primary" @click="shuffleSongs">
            <i class="fas fa-random"></i> Shuffle
          </button>
        </div>
        <table class="song-table">
          <thead>
            <tr>
              <th class="song-title-header">Title</th>
              <th class="song-title-header">Album</th>
              <th class="song-genre-header">Genre</th>
              <th class="song-artist-header">Artist</th>
              <th class="song-actions-header">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr class="song-row" v-for="song in shuffledSongs" :key="song.id">
              <td class="song-title">{{ song.title }}</td>
              <td class="song-title">{{ song.album.title }}</td>
              <td class="song-genre">{{ song.genre }}</td>
              <td class="song-artist">{{ song.artist.name }}</td>
              <td class="song-actions">
                <a :href="'/play/song/'+song.id">
                  <button class="btn btn-success">
                    <i class="fas fa-play"></i>
                  </button>
                </a>
                <button class="btn btn-danger" @click="deleteSong(song.id)">
                  <i class="fas fa-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="add-songs" v-else>
        <h2 class="section-title">Add Songs to Playlist</h2>
        <p>Please select the songs you would like to add to the playlist below.</p>
      </div>
    </div>

    <h1 class="playlist-title">Album Library</h1>

    <div class="album-container" v-for="album in filteredAlbums" :key="album.id">
      <h2 class="album-title">{{ album.title }}</h2>
      <table class="song-table">
        <thead>
          <tr>
            <th class="song-checkbox-header"></th>
            <th class="song-title-header">Title</th>
            <th class="song-genre-header">Genre</th>
            <th class="song-artist-header">Artist</th>
          </tr>
        </thead>
        <tbody>
          <tr class="song-row" v-for="song in album.songs" :key="song.id">
            <td class="song-checkbox">
              <input type="checkbox" v-model="selectedSongs" :value="song.id" />
            </td>
            <td class="song-title">{{ song.title }}</td>
            <td class="song-genre">{{ song.genre }}</td>
            <td class="song-artist">{{ album.artist.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <button class="add-button" @click="addSongsToPlaylist">
      <i class="fas fa-plus"></i> Add Songs
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      playlist: this.$route.meta.playlist,
      albums: this.$route.meta.albums,
      user_id: localStorage.getItem('user_id'),
      selectedSongs: [],
      shuffledSongs: [],
    };
  },
  created() {
    this.shuffledSongs = [...this.playlist.songs];
  },
  computed: {
    filteredAlbums() {
      return this.albums.filter(album => {
        return !this.playlist.songs.some(song => song.album_id === album.id);
      });
    },
  },
  methods: {
    async addSongsToPlaylist() {
      const token = localStorage.getItem('token');
      const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/${this.playlist.id}/add_songs`, {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token,
        },
        body: JSON.stringify({ song_ids: this.selectedSongs }),
      });
      const data = await response.json();
      if (response.status !== 201) {
        this.$store.dispatch('showMessage', data.message);
      } else {
        this.$store.dispatch('showMessage', data.message);
        this.$router.push('/playlists');
      }
    },
    async deleteSong(id) {
      const token = localStorage.getItem('token');
      const response = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/${this.playlist.id}/add_songs`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + token,
        },
        body: JSON.stringify({ song_id: id }),
      });
      const data = await response.json();
      if (response.status !== 201) {
        this.$store.dispatch('showMessage', data.message);
      } else {
        this.$router.go(0);
        this.$store.dispatch('showMessage', data.message);
      }
    },
    shuffleSongs() {
      this.shuffledSongs = this.shuffleArray([...this.playlist.songs]);
    },
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
    },
  },
  name: 'PlaylistSongs',
};
</script>

<style scoped>
.song-actions {
  text-align: center;
  padding: 0.75rem 0.5rem;
}

.playlist-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f8f8f8;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.playlist-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.playlist-title {
  font-size: 2.5rem;
  font-weight: bold;
}

.add-button {
  display: flex;
  align-items: center;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.add-button:hover {
  background-color: #45a049;
}

.add-button i {
  margin-right: 0.5rem;
  text-align: center;
}

.playlist-content {
  margin-bottom: 2rem;
}

.playlist-songs,
.add-songs {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  margin-bottom: 2rem;
}

.album-container {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  margin-bottom: 2rem;
}

.section-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.song-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
}

.song-title-header,
.song-genre-header,
.song-artist-header,
.song-actions-header,
.song-checkbox-header {
  text-align: center;
  padding: 0.75rem 0.5rem;
  font-weight: bold;
  background-color: #f2f2f2;
}

.song-row {
  border-bottom: 1px solid #ddd;
}

.song-title,
.song-genre,
.song-artist,
.song-checkbox {
  padding: 0.75rem 0.5rem;
}
</style>