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
        <img :src="'http://127.0.0.1:5000/album/' + album.id" alt="Album Cover">
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