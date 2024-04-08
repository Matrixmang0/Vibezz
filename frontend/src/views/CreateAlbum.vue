<template>
  <div class="container mt-5">
    <h1 class="display-3 mb-4" style="text-align: center;">New Album</h1>

    <form class="row g-3" @submit.prevent="submitForm">
      <div class="col-md-8">
        <label for="name" class="form-label">Album Name</label>
        <input type="text" class="form-control" id="name" name="name" v-model="formData.title" required>
      </div>
      <div class="col-12">
        <label for="description" class="form-label">Description</label>
        <textarea class="form-control" id="description" name="description" rows="8" v-model="formData.description" required></textarea>
      </div>
      <div class="col-12">
        <label for="image" class="form-label">Album Cover Image</label>
        <input type="file" class="form-control" id="image" name="image" accept="image/*" @change="handleImageChange">
        <img v-if="imageUrl" :src="imageUrl" alt="Selected Image" style="max-width: 100%; margin-top: 10px;">
      </div>
      <div class="col-12 mt-4" style="text-align: center;">
        <button type="submit" class="btn btn-success">
          <i class="fas fa-plus me-2"></i> Add Album
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
        title: "",
        description: "",
        // imageData: null
      },
      imageUrl: null,
      user_id: localStorage.getItem('user_id')
    };
  },
  methods: {
    handleImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.imageUrl = URL.createObjectURL(file);
        // this.formData.imageData = file;
      }
    },
    async submitForm() {
      const token = localStorage.getItem('token');
      const response = await fetch('http://127.0.0.1:5000/api/'+localStorage.getItem('user_id')+'/new-album', {
							method: 'post',
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
  },
  name: "CreateAlbum"
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

</style>