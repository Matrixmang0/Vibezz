<template>
  <div class="container mt-5">
  <div class="row justify-content-center">
    <div class="col-md-6">
      <h1 class="display-3 text-center mb-5">Change Password</h1>
      <form @submit.prevent="update" class="form border rounded p-4" style="background-color: #f8f9fa;">
        <div class="mb-3">
          <label for="cpassword" class="form-label">Current Password</label>
          <input type="password" name="cpassword" class="form-control" v-model="passData.currentPassword" />
        </div>
        <div class="mb-3">
          <label for="npassword" class="form-label">New Password</label>
          <input type="password" name="npassword" class="form-control" v-model="passData.newPassword"/>
        </div>
        <div class="mb-3">
          <label for="rnpassword" class="form-label">Re-enter New Password</label>
          <input type="password" name="rnpassword" class="form-control" v-model="passData.reNewPassword"/>
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-primary"><i class="fa-solid fa-arrows-rotate"></i> Update</button>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>

export default {

  data() {
				return {
          passData: {
            currentPassword: '',
            newPassword: '',
            reNewPassword: ''
          }
        }
		},
    

		methods: {
				async update() {

            const token = localStorage.getItem('token');
						const response = await fetch('http://127.0.0.1:5000/api/user/'+localStorage.getItem('user_id')+'/edit-pass', {
							method: 'put',
							headers: {
								'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
							},
							body: JSON.stringify(this.passData)
						});
						const data = await response.json();
						this.$store.dispatch('showMessage', data.message);
				},
    },

		name: 'Profile'
}

</script>

<style scoped>
  .container {
    justify-content: center;
    text-align: left;
  }
</style>