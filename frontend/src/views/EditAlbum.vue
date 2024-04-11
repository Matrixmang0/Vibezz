<template>

    <div class="container mt-5">
    <h1 class="display-3 mb-4" style="text-align: center;">Edit Album</h1>

    <form class="row g-3" @submit.prevent="submitForm">
      <div class="col-md-8">
        <label for="title" class="form-label">Album Title</label>
        <input type="text" class="form-control" id="title" name="title" v-model="formData.title" required>
      </div>
      <div class="col-12">
        <label for="description" class="form-label">Description</label>
        <textarea class="form-control" id="description" name="description" rows="8" v-model="formData.description" required></textarea>
      </div>
      <div class="col-12">
        <label for="image" class="form-label">Album Cover Image</label>
        <img :src="'http://127.0.0.1:5000/album/' + formData.id" class="album-image" alt="Album Cover" style="width: 200px; height: 300px;">
      </div>
      <div class="col-12">
        <label for="image" class="form-label">New Cover Image</label>
        <input type="file" class="form-control" id="image" name="image" accept="image/*" @change="handleImageChange">
      </div>
      <div class="col-12 mt-4" style="text-align: center;">
        <button type="submit" class="btn btn-success" @click="onUpload">
          <i class="fa-solid fa-pen-to-square"></i> Edit Album
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
        id: this.$route.meta.album.id,
        title: this.$route.meta.album.title,
        description: this.$route.meta.album.description
      },
      image: null,
      user_id: localStorage.getItem('user_id')
    };
  },
  methods: {
    handleImageChange(event) {
      this.image = event.target.files[0];
    },
    onUpload() {

      if (this.formData.title == "" | this.formData.description == ""){
        this.$store.dispatch('showMessage', 'Please fill in all fields');
        return;
      }
      else if (this.image == null){
        return;
      }
      else{

        const fd = new FormData();
        fd.append('image', this.image, this.image.name);
        fd.append('title', this.formData.title);

        const token = localStorage.getItem('token');

        axios.post(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/albums/upload-image`, fd, {
          headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          console.log('Image uploaded successfully')
        })
        .catch(error => {
          console.log(error);
        });
      }
    },
    async submitForm() {
      if (this.formData.title == "" | this.formData.description == ""){
        this.$store.dispatch('showMessage', 'Please fill in all fields');
        return;
      }
      else{
        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5000/api/'+localStorage.getItem('user_id')+'/edit-album/'+this.formData.id, {
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
                this.$router.push('/studio');
            }
      }
    }
  },
  name: "EditAlbum"
};
</script>

<style scoped>

    .container {
      max-width: 700px;
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

    .album-image {
      margin-top: 10px;
      margin-left: 40px; /* Adjust as needed */
    }

</style>