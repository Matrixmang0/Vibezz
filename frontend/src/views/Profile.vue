<script>

export default {

  data() {
				return {
          profData: {
            name: this.$route.meta.data.name,
            username: this.$route.meta.data.username,
            email: this.$route.meta.data.email,
            profile_img: this.$route.meta.data.profile_img
          }
        }
		},
    

		methods: {
				async update() {

            const token = localStorage.getItem('token');
						const response = await fetch('http://127.0.0.1:5000/api/user/'+localStorage.getItem('user_id'), {
							method: 'put',
							headers: {
								'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
							},
							body: JSON.stringify(this.profData)
						});
						const data = await response.json();
						this.$store.dispatch('showMessage', data.message);
				}
		},

    computed: {
      
    },

		name: 'Profile'
}
</script>


<template>
  
  <div class="container mt-5">
  
        <div class="align-items-center mb-4 text-center">
          <h1 class="display-3 me-3">
            Welcome
            <span class="text-muted">{{ profData.username }}</span>
          </h1>
          <img :src="profData.profile_img" class="profile-image" alt="Profile Image" />
        </div>
  
        <div class="alert alert-info" role="alert">
          <strong>Info:</strong> You can update your profile here
        </div>
  
        <!-- Form to update Profile -->
        <form @submit.prevent="update" class="form p-4 border rounded">
          <div class="mb-3">
            <label for="name" class="form-label">Name</label>
            <input type="text" name="name" class="form-control" v-model="profData.name" required />
          </div>
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" name="username" class="form-control" v-model="profData.username" required />
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" name="email" class="form-control" v-model="profData.email" required />
          </div>
          <div class="d-flex flex-column gap-3">
            <a class="btn btn-warning" href="" role="button">Change Password</a>
            <button type="submit" class="btn btn-info">Save</button>
          </div>
        </form>
      </div>

</template>

<style scoped>

  .profile-image {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 2px solid #000;
    margin-left: 20px;
  }

  .alert-info {
    margin-top: 20px;
    text-align: center;
  }

  .form {
    background-color: #f8f9fa; /* Light gray background */
  }

  .container {
    max-width: 600px;
    text-align: left;
  }

</style>