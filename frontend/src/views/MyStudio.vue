<template>
  <div v-if="albumExists">
    <div class="container mt-5">
      <h1 class="display-3 mb-4 text-center">My Albums</h1>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h2 class="text-muted">Albums</h2>
        <a href="/create-album" class="btn btn-success btn-lg">
          <i class="fas fa-plus"></i> Add Album
        </a>
      </div>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Album ID</th>
            <th>Title</th>
            <th>No of Songs</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="album in albums" :key="album.id">
            <td>{{ album.id }}</td>
            <td>{{ album.title }}</td>
            <td>{{ album.description | length }}</td> 
            <td>
              <a href="" class="btn btn-info me-2">
                <i class="fas fa-search"></i> Show
              </a>
              <a href="" class="btn btn-warning me-2">
                <i class="fas fa-edit"></i> Edit
              </a>
              <button type="button" class="btn btn-danger" data-bs-toggle="modal" :data-bs-target="'#deleteModal' + album.id">
                <i class="fas fa-trash"></i> Delete
              </button>

              <!-- Delete Modal -->
                <!-- <div class="modal fade" id="deleteModal{{ genre.id }}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true"> -->
                  <!-- <div class="modal-dialog modal-dialog-centered"> -->
                    <!-- <div class="modal-content"> -->
                      <!-- <div class="modal-header"> -->
                        <!-- <h5 class="modal-title" id="deleteModalLabel">Delete {{ genre.name }}</h5> -->
                        <!-- <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button> -->
                      <!-- </div> -->
                      <!-- <div class="modal-body"> -->
                        <!-- Are you sure you want to delete the genre {{ genre.name }}? -->
                      <!-- </div> -->
                      <!-- <div class="modal-footer"> -->
                        <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button> -->
                        <!-- <a href="{{ url_for("delete_genre", id=genre.id) }}" type="button" class="btn btn-danger" method="post"> -->
                          <!-- <i class="fas fa-trash"></i> Delete -->
                        <!-- </a> -->
                      <!-- </div> -->
                    <!-- </div> -->
                  <!-- </div> -->
                <!-- </div> -->
              <!-- End Delete Modal -->


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
        <a href="/create-album" class="btn btn-success btn-lg">Create Album</a>
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
    

		// methods: {
		// 		async update() {

    //         const token = localStorage.getItem('token');
		// 				const response = await fetch('http://127.0.0.1:5000/api/user/'+localStorage.getItem('user_id'), {
		// 					method: 'put',
		// 					headers: {
		// 						'Content-Type': 'application/json',
    //             'Authorization': 'Bearer ' + token
		// 					},
		// 					body: JSON.stringify(this.profData)
		// 				});
		// 				const data = await response.json();
		// 				this.$store.dispatch('showMessage', data.message);
		// 		},
    // },

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