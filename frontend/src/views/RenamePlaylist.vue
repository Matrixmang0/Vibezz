<template>
  <div class="container mt-5">
    <h1 class="display-3 mb-4 text-center">Rename Playlist</h1>
    <form class="row g-3 bg-white p-4 rounded shadow" @submit.prevent="submitForm">
      <div class="col-md-8">
        <label for="title" class="form-label" ><strong>Playlist Title</strong></label>
        <input type="text" class="form-control" id="title" name="title" v-model="formData.title" required>
      </div>
      <div class="col-12 d-flex justify-content-center">
        <button type="submit" class="btn btn-primary">
          <i class="fas fa-plus me-2"></i> Edit Playlist
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        title: this.$route.meta.playlist.title,
        id: this.$route.meta.playlist.id
      },
      user_id: localStorage.getItem('user_id')
    };
  },
  methods: {
    async submitForm() {
      if (this.formData.title == ""){
        this.$store.dispatch('showMessage', 'Please fill in all fields');
        return;
      }
      else{
        const token = localStorage.getItem('token');
        const response = await fetch('http://127.0.0.1:5000/api/'+localStorage.getItem('user_id')+'/playlist/'+this.formData.id, {
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
                this.$router.push('/playlists');
            }
      }
    }
  },
  name: "RenamePlaylist"
};
</script>

<style scoped>

.container {
  max-width: 700px;
  text-align: left;
}

.form-control {
  border-color: #ced4da;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.form-control:focus {
  border-color: #80bdff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
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

.bg-white {
  background-color: #fff !important;
}

.rounded {
  border-radius: 0.5rem !important;
}

.shadow {
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15) !important;
}

</style>