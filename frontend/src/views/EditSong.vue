<template>
  <div class="container mt-5">
    <h1 class="display-3 mb-4 text-center">Edit Song</h1>

    <form @submit.prevent="submitForm" enctype="multipart/form-data" method="post" class="row g-3" >
      <div class="col-md-6">
        <div class="mb-4">
          <label for="title" class="form-label"><strong class="text-muted">Song Title</strong></label>
          <input type="text" class="form-control" id="title" name="title" v-model="formData.title" required>
        </div>

        <div class="mb-4">
          <label for="genre" class="form-label"><strong class="text-muted">Genre</strong></label>
          <input type="text" class="form-control" id="genre" name="genre" v-model="formData.genre" required>
        </div>

        <div class="mb-4">
          <label for="album_id" class="form-label"><strong class="text-muted">Album</strong></label>
          <select class="form-select" id="album_id" name="album_id" v-model="formData.album_id">
            <option v-for="album in albums" :key="album.id" :value="album.id">{{ album.title }}</option>
          </select>
        </div>

        <div class="mb-4">
          <label for="image" class="form-label"><strong class="text-muted">Cover Image</strong></label>
                  <img :src="'http://127.0.0.1:5000/song/cover/' + formData.id" class="song-image" alt="Album Cover" style="width: 200px; height: 300px;">
        </div>

        <div class="mb-4">
          <label for="image" class="form-label"><strong class="text-muted">New Cover Image</strong></label>
          <input type="file" class="form-control" name="image" @change="handleImageChange" required>
        </div>
      </div>

      <div class="col-md-6">
        <div class="mb-4">
          <label for="lyrics" class="form-label"><strong class="text-muted">Lyrics</strong></label>
          <textarea class="form-control" id="lyrics" name="lyrics" rows="18" v-model="formData.lyrics" required></textarea>
        </div>

        <div class="mb-4">
          <label for="content" class="form-label"><strong class="text-muted">Audio</strong></label>
          <input type="file" class="form-control" name="audio" @change="handleAudioChange" required>
        </div>

        <div class="mb-4">
          <label for="audio" class="form-label"><strong class="text-muted">Song Audio</strong></label>

          <audio controls controlsList="nodownload">
            <source :src="'http://127.0.0.1:5000/song/audio/' + formData.id" type="audio/mpeg">
          </audio>
        </div>
      </div>

      <div class="mt-4 text-center">
          <button type="submit" class="btn btn-success">
            <i class="fa-solid fa-pen-to-square"></i> Edit Song
          </button>
        </div>
    </form>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        id: this.$route.meta.song.id,
        title: this.$route.meta.song.title,
        genre: this.$route.meta.song.genre,
        album_id: this.$route.meta.song.album_id,
        lyrics: this.$route.meta.song.lyrics,
      },
      fileData: {
        image: null,
        audio: null
      },
      albums: this.$route.meta.albums,
      user_id: localStorage.getItem('user_id')
    };
  },
  methods: {
    handleImageChange(event) {
      this.fileData.image = event.target.files[0];
    },
    handleAudioChange(event) {
      this.fileData.audio = event.target.files[0];
    },
    async submitForm() {
      if (this.formData.title == "" | this.formData.genre == "" | this.formData.lyrics == "" | this.formData.album_id == ""){
        this.$store.dispatch('showMessage', 'Please fill in all fields');
        return;
      }
      else if (this.fileData.image == null | this.fileData.audio == null){
        this.$store.dispatch('showMessage', 'Please select an image');
        return;
      }
      else{
        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5000/api/'+localStorage.getItem('user_id')+'/edit-song/'+this.formData.id, {
                method: 'put',
                headers: {
                  'Content-Type': 'application/json',
                  'Authorization': 'Bearer ' + token,
                },
                body: JSON.stringify(this.formData)
              });
              const data = await response.json();
              if (response.status != 201) {
                this.$store.dispatch('showMessage', data.message);
              }
              else{
                this.$store.dispatch('showMessage', data.message);
                this.$router.push('/album/'+this.formData.album_id);
            }

        const fd = new FormData();
        fd.append('image', this.fileData.image, this.fileData.image.name);
        fd.append('audio', this.fileData.audio, this.fileData.audio.name);
        fd.append('title', this.formData.title);

        axios.post(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/songs/upload-image`, fd, {
          headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log('Image and Audio uploaded successfully')
        })
        .catch(error => {
          console.log(error);
        });
      }
    }
  },
  name: "EditSong"
};
</script>

<style scoped>

  body {
    background-color: #f8f9fa; /* Light gray background */
    text-align: left;
  }
  .container {
    max-width: 1000px;
    text-align: left;
  }
  .btn-success {
    background-color: #28a745; /* Bootstrap success button color */
    border-color: #28a745; /* Bootstrap success button border color */
  }
  .btn-success:hover {
    background-color: #218838; /* Darker shade on hover */
    border-color: #218838; /* Darker shade on hover */
  }
  .display-3 {
    margin-bottom: 50px /* Dark gray heading */
  }
  .song-image {
    margin-left: 60px; /* Adjust as needed */
  }
  audio {
    width: 100%; /* Adjust the width as needed */
  }

</style>