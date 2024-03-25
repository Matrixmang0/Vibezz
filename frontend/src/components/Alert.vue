<template>
	<div v-if="this.$store.state.message">
				<div v-if="this.$store.state.message.includes('success')">
          <div class="alert alert-success mb-3 text-center" role="alert">
                          {{ this.$store.state.message }}
          </div>
        </div>
        <div v-else>
          <div class="alert alert-warning mb-3 text-center" role="alert">
                          {{ this.$store.state.message }}
          </div>
        </div>
	</div>
</template>

<script>
export default {
  name: 'Alert',
}
</script>