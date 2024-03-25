<script>

export default {

    data() {
				return {
						formData:{
								username: '',
								password: '',
                confirm_password: '',
                email: '',
                name: ''
						},
				}
		},

		methods: {
				async register() {
						const response = await fetch('http://127.0.0.1:5000/api/users', {
							method: 'post',
							headers: {
								'Content-Type': 'application/json'
							},
							body: JSON.stringify(this.formData)
						});
						const data = await response.json();
						if (response.status === 404) {
							this.$store.dispatch('showMessage', data.message);
							this.$router.push('/register');
						}
						else{
							this.$store.dispatch('showMessage', data.message);
							this.$router.push('/login');
					}
				}
		},

    name: 'Registration',
}
</script>

<template>
  <div class="container mt-5">
    <h1 class="display-1 text-center">Registration</h1>

    <div class="card bg-light shadow-lg p-4 rounded w-50 mx-auto">
      <form  @submit.prevent="register">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" name="username" class="form-control" v-model="formData.username" required />
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input type="email" name="email" class="form-control" v-model="formData.email" required />
          <div id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input type="text" name="name" class="form-control" v-model="formData.name" required />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" name="password" class="form-control" aria-describedby="passwordHelpBlock" v-model="formData.password" required />
          <div id="passwordHelpBlock" class="form-text text-muted">
            Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
          </div>
        </div>
        <div class="mb-3">
          <label for="confirm_password" class="form-label">Confirm Password</label>
          <input type="password" name="confirm_password" class="form-control" v-model="formData.confirm_password" required />
        </div>
        <div class="mb-3 text-center">
          <button type="submit" class="btn btn-primary btn-lg">Register</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
  body {
    background-color: #f8f9fa; /* Light gray background */
  }

  .container {
    width: 1000px;
    margin-top: 15px;
    text-align: left;
  }

  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
</style>