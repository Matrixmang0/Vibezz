<script>

export default {
    data() {
				return {
						formData:{
								username: '',
								password: ''
						},
				}
		},

		methods: {
				async login() {
						const response = await fetch('http://127.0.0.1:5000/api/login', {
							method: 'post',
							headers: {
								'Content-Type': 'application/json'
							},
							body: JSON.stringify(this.formData)
						});
						const data = await response.json();
						if (response.status != 200) {
							this.$store.dispatch('showMessage', data.message);
							this.$router.push('/login');
						}
						else{
							localStorage.setItem('token', data.access_token);
							localStorage.setItem('user_id', data.user_id);
							this.$store.dispatch('showMessage', data.msg);
							this.$router.push('/');
					}
				}
		},

		name: 'Login'
}

</script>

<template>
  <div class="container mt-5">
    <h1 class="display-1 text-center"><b>Login</b></h1>

    <div class="card bg-light shadow-lg p-4 rounded w-50 mx-auto">
      <form @submit.prevent="login">
        <div class="mb-3">
          <label for="username-email" class="form-label">Username</label>
          <input
            type="text"
            v-model="formData.username"
            class="form-control"
            id="InputEmail"
            aria-describedby="emailHelp"
          />
          <div id="emailHelp" class="form-text text-muted">
            We'll never share your email with anyone else.
          </div>
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            v-model="formData.password"
            class="form-control"
            id="exampleInputPassword1"
          />
        </div>
        <div class="mb-3 text-center">
          <button type="submit" class="btn btn-success btn-lg" >Login</button>
        </div>
      </form>

      <p class="text-center">Don't have an account? <a href="/register">Register</a></p>
    </div>
  </div>
</template>

<style scoped>
body {
  background-color: #f8f9fa; /* Light gray background */
}

.container {
  width: 900px;
  margin-top: 63px;
  text-align: left;
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
