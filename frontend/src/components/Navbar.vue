<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/" style="margin-right: 15px;">
        <img src="../assets/logo.png" alt="Vibezz" width="30" height="30" class="d-inline-block align-text-top" />
        <span class="brand-name">Vibezz</span>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo02"
        aria-controls="navbarTogglerDemo02"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="/"><i class="fa-solid fa-house"></i> Home</a>
          </li>
        </ul>

        <div v-if="this.$route.name === 'Home'" class="search-box">
          <form>
            <div class="input-group mb-3">
              <select v-model="selectedParameter" class="form-select">
                <option value="" disabled selected>Select Parameter</option>
                <option value=0>Album</option>
                <option value=1>Song</option>
              </select>
              <input v-model="searchQuery" class="form-control" type="text" placeholder="Search" aria-label="Text input with dropdown button">
              <button class="btn btn-outline-primary" type="submit"><i class="fa-solid fa-x"></i></button>
            </div>
          </form>
        </div>

        <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-if="user_id == 0">
          <li class="nav-item">
            <a class="nav-link" href="/user-stats"><i class="fa-solid fa-chart-simple"></i> User Stats</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"><i class="fa-solid fa-universal-access"></i> Flag Requests</a>
          </li>
        </ul>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-else-if="user_id">
          <li class="nav-item">
            <a class="nav-link" href="/playlists"><i class="fa-solid fa-bookmark"></i> My Playlist</a>
          </li>
        </ul>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-else>
          <li class="nav-item">
            <a class="nav-link" href="/login"><i class="fa-solid fa-right-to-bracket"></i> Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/register"><i class="fa-solid fa-cash-register"></i> Register</a>
          </li>
        </ul>

        <div class="dropdown" style="margin: 2px 2px;">
          <a class="btn btn-primary" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
            <div v-if="user_id">
              <div class="profile-img">
                <img :src="'https://api.dicebear.com/7.x/pixel-art/svg?seed='+user_id" width="40" height="40" alt="Profile Image" class="img-fluid rounded-circle" />
              </div>
            </div>
            <div v-else>
              <i class="fa-solid fa-user-large fa-2x"></i>
            </div>
          </a>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuLink">
            <div v-if="user_id">
              <li><a class="dropdown-item" href="/profile" :class="{ 'active': $route.name === 'Profile' }">Profile</a></li>
              <div v-if="user_id != 0">
                <li><a class="dropdown-item" href="/studio" :class="{ 'active': $route.name === 'MyStudio' }">My Studio</a></li>
                <li><a class="dropdown-item" href="/playlists">My Playlist</a></li>
              </div>
              <li><hr class="dropdown-divider"></li>
              <li class="logout-item"><a class="dropdown-item" @click="logout" href="">Logout</a></li>
            </div>
            <div v-else>
              <li><a class="dropdown-item" :class="{ 'active': $route.name === 'Login' }" href="/login">Login</a></li>
              <li><a class="dropdown-item" :class="{ 'active': $route.name === 'Registration' }" href="/register">Register</a></li>
            </div>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  data() {
    return {
      user_id: localStorage.getItem('user_id'),
      selectedParameter: '',
      searchQuery: ''
    }
  },

  watch: {
    selectedParameter() {
      this.updateParameter();
    },
    searchQuery() {
      this.updateQuery();
    }
  },

  methods: {
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('user_id');
      this.$router.go('/login');
    },

    updateParameter() {
      this.$store.dispatch('updateSelectedParameter', this.selectedParameter);
    },
    updateQuery() {
      this.$store.dispatch('updateSearchQuery', this.searchQuery);
    }
  },

  name: 'Navbar'
}
</script>

<style scoped>
.logout-item {
  background-color: #ff6347; /* Red background color */
}

.search-box {
  justify-content: center;
  margin-top: 15px;
}

.brand-name {
  font-size: 1.2rem;
  font-weight: bold;
  margin-left: 0.5rem;
}

.navbar {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-image: linear-gradient(to right, #141e30, #243b55);
}

.navbar-brand,
.nav-link {
  color: #fff;
  transition: color 0.3s;
}

.navbar-brand:hover,
.nav-link:hover {
  color: #e6e6e6;
}

.dropdown-menu {
  border: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.dropdown-item {
  transition: background-color 0.3s;
}

.dropdown-item:hover {
  background-color: #f5f5f5;
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
</style>