<script>
export default {
  data() {
    return {
      profData: {
        name: this.$route.meta.data.name,
        username: this.$route.meta.data.username,
        email: this.$route.meta.data.email
      },
      user_id: localStorage.getItem('user_id')
    }
  },
  methods: {
    async update() {
      const token = localStorage.getItem('token');
      const response = await fetch('http://127.0.0.1:5000/api/user/' + localStorage.getItem('user_id'), {
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
  name: 'Profile'
}
</script>

<template>
  <div class="container mt-5">
    <div class="align-items-center mb-4 text-center">
      <h1 class="display-3 me-3">Welcome <span class="text-muted">{{ profData.username }}</span></h1>
      <div class="profile-image-container">
        <img :src="'https://api.dicebear.com/7.x/pixel-art/svg?seed='+user_id" class="profile-image" alt="Profile Image" />
      </div>
    </div>
    <div class="alert alert-info alert-dismissible fade show" role="alert">
      <strong>Info:</strong> You can update your profile here
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <form @submit.prevent="update" class="form p-4 border rounded shadow">
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
        <a class="btn btn-warning" href="/change-password" role="button">Change Password</a>
        <button type="submit" class="btn btn-primary">Save</button>
      </div>
    </form>
  </div>
</template>

<style scoped>
.profile-image-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.profile-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 4px solid #007bff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.alert-info {
  background-color: #e6f2ff;
  border-color: #b8daff;
  color: #004085;
  text-align: center;
}

.form {
  background-color: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 600px;
  text-align: left;
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

.btn-warning {
  background-color: #ffc107;
  border-color: #ffc107;
  color: #333;
  transition: background-color 0.3s, border-color 0.3s;
}

.btn-warning:hover {
  background-color: #e0a800;
  border-color: #e0a800;
}
</style>