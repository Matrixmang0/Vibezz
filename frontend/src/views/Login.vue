<script>
	import { apiClient } from "@/apiClient";
</script>

<template>
	<div class="container mt-5">
		<h1 class="display-1 text-center"><b>Login</b></h1>

		<div class="card bg-light shadow-lg p-4 rounded w-50 mx-auto">
			<form method="post">
				<div class="mb-3">
					<label for="username-email" class="form-label">Username</label>
					<input
						type="text"
						v-model="username"
						class="form-control"
						id="InputEmail"
						aria-describedby="emailHelp" />
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
						id="exampleInputPassword1" />
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
