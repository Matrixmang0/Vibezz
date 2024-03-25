<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#" style="margin-right: 15px;">
        <img src="../assets/logo.png" alt="Vibezz" width="30" height="30" class="d-inline-block align-text-top" />
        Vibezz
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
            <a class="nav-link" href="#"><i class="fa-solid fa-house"></i> Home</a>
          </li>
          
        </ul>

        <!-- {% include 'searchbar.html' with context %}

        {% if request.endpoint == 'show_book' %}
              <div class="text-center text-white">
                  <h1 class="display-5">{{book.title}}</h1>
              </div>
        {% endif %} -->

          <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-if="user_id == 0">
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-chart-simple"></i> User Stats</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-universal-access"></i>  Requests</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-hand-holding-hand"></i> Borrows</a>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-else-if="user_id">
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-chart-simple"></i> My Stats</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-book-open"></i>  My Books</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-cart-shopping"></i> My Cart</a>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-else>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-right-to-bracket"></i> Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#"><i class="fa-solid fa-cash-register"></i> Register</a>
            </li>
          </ul>

      

        <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>

          <div class="dropdown" style="margin: 2px 2px;">
              <a class="btn btn-light" href="#" role="button" id="dropdownMenuLink" data-bs-toggle="dropdown" aria-expanded="false">
                  <!-- {% if "user_id" in session %} -->
                      <!-- <div class="profile-img">
                          <img src="https://api.dicebear.com/7.x/pixel-art/svg?seed=0" width="40" height="40" alt="Profile Image" class="img-fluid rounded-circle" />
                      </div> -->
                  <!-- {% else %} -->
                      <i class="fa-solid fa-user-large fa-2x"></i>
                  <!-- {% endif %} -->
              </a>
              <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuLink">
                  <!-- {% if "user_id" in session %}
                      <li><a class="dropdown-item" href="#">Profile</a></li>
                      {% if session['user_id'] != 10000 %}
                          <li><a class="dropdown-item" href="#">My Orders</a></li>
                          <li><a class="dropdown-item" href="#">My Borrows</a></li>
                          <li><a class="dropdown-item" href="#">Requests</a></li>
                      {% endif %}
                      <li><hr class="dropdown-divider"></li>
                      <li class="logout-item"><a class="dropdown-item" href="#">Logout</a></li>
                  {% else %}
                      <li><a class="dropdown-item" href="#">Login</a></li>
                      <li><a class="dropdown-item" href="#">Register</a></li>
                  {% endif %} -->
              </ul>
          </div>

        <p>&nbsp;</p>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      user_id: localStorage.getItem('user_id'),
    }
  },
  name: 'Navbar',
}
</script>

<style scoped>
  .logout-item {
    background-color: #ff6347; /* Red background color */
  }

  /* If you prefer inline styles */
  .logout-item a {
    background-color: #ff6347; /* Red background color */
  }
</style>