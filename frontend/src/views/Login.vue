<script>
import { apiClient } from "@/apiClient";
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "Login",
  setup() {
    const router = useRouter();
    const username = ref("");
    const password = ref("");
    const message = ref("");

    const login = async (e) => {
			e.preventDefault();
			try {
				const response = await apiClient.post("api/login", {
					username: username.value,
					password: password.value,
				});
				console.log("Login response:", response); // Log the response to the console
				if (response?.data?.token) {
					localStorage.setItem("token", response.data.token);
					router.push("/");
				} else {
					throw new Error("Invalid response from server");
				}
			} catch (error) {
				console.error("Login error:", error); // Log any errors to the console
				message.value = error.response?.data?.message || "An error occurred";
			}
		};

    return { username, password, message, login };
  },
};
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
            v-model="username"
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
            v-model="password"
            class="form-control"
            id="exampleInputPassword1"
          />
        </div>
        <div class="mb-3 text-center">
          <button type="submit" class="btn btn-success btn-lg">Login</button>
        </div>
      </form>

      <p class="text-center">Don't have an account? <a href="#">Register</a></p>
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
