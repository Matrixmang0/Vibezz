<template>
  <div class="container my-5">
    <h1 v-if="this.$route.meta.flags"  class="mb-4">Flag Requests</h1>
    <table v-if="this.$route.meta.flags"  class="table table-striped table-hover">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">User</th>
          <th scope="col">Song</th>
          <th scope="col">Artist</th>
          <th scope="col">Album</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="flag in flags" :key="flag.id">
          <th scope="row">{{ flag.id }}</th>
          <td>{{ flag.user.name }}</td>
          <td>{{ flag.song.title }}</td>
          <td>{{ flag.song.artist.name }}</td>
          <td>{{ flag.song.album.title }}</td>
          <td>
            <button class="btn btn-success mr-2" @click="approveFlag(flag.id, flag.song.id)">
              <i class="fas fa-check"></i> Approve
            </button>
            <button class="btn btn-danger" @click="rejectFlag(flag.id)">
              <i class="fas fa-times"></i> Reject
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-else class="no-flags-container">
      <h2 class="no-flags-title">No Flags to Review</h2>
      <p class="no-flags-message">Come back later.</p>
    </div>
  </div>
      
</template>

<script>
export default {
  name: 'FlagRequests',
  data() {
    return {
      flags: this.$route.meta.flags
    }
  },
  methods: {
    async approveFlag(flagId, songId) {
      try {
            const token = localStorage.getItem('token');
            const response1 = await fetch(`http://127.0.0.1:5000/api/flags/${flagId}`, {
              method: 'delete',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
              },
            });

            if (!response1.ok) {
              // Handle non-successful response (status code other than 2xx)
              const errorData = await response1.json();
              throw new Error(errorData.message || 'Failed to delete flag');
            }

            const data = await response1.json();
            this.$store.dispatch('showMessage', data.message);
            this.$router.go();
          } catch (error) {
            console.error('Error deleting flag:', error);
            // Optionally, show an error message to the user
            this.$store.dispatch('showMessage', 'Failed to delete flag');
          }
      try {
            const token = localStorage.getItem('token');
            const response2 = await fetch(`http://127.0.0.1:5000/api/${localStorage.getItem('user_id')}/songs/${songId}/delete`, {
              method: 'delete',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
              },
            });

            if (!response2.ok) {
              // Handle non-successful response (status code other than 2xx)
              const errorData = await response2.json();
              throw new Error(errorData.message || 'Failed to delete song');
            }

            const data = await response2.json();
            this.$store.dispatch('showMessage', data.message);
            this.$router.go();
          } catch (error) {
            console.error('Error deleting song:', error);
            // Optionally, show an error message to the user
            this.$store.dispatch('showMessage', 'Failed to delete song');
          }
    },
    async rejectFlag(flagId) {
      // Implement reject flag logic here
      try {
            const token = localStorage.getItem('token');
            const response1 = await fetch(`http://127.0.0.1:5000/api/flags/${flagId}`, {
              method: 'delete',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
              },
            });

            if (!response1.ok) {
              // Handle non-successful response (status code other than 2xx)
              const errorData = await response1.json();
              throw new Error(errorData.message || 'Failed to delete flag');
            }

            const data = await response1.json();
            this.$store.dispatch('showMessage', data.message);
            this.$router.go();
          } catch (error) {
            console.error('Error deleting flag:', error);
            // Optionally, show an error message to the user
            this.$store.dispatch('showMessage', 'Failed to delete flag');
          }
    }
  }
}
</script>

<style scoped>
.container {
  background-color: #f5f5f5;
  border-radius: 0.5rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  padding: 2rem;
}

.table {
  background-color: #fff;
  border-radius: 0.5rem;
  overflow: hidden;
}

.table th {
  background-color: #f5f5f5;
  font-weight: bold;
  color: #333;
}

.table td {
  border-bottom: 1px solid #eee;
}

.btn {
  margin-right: 0.5rem;
}

.no-flags-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 300px;
}

.no-flags-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.no-flags-message {
  font-size: 1.5rem;
  color: #666;
}
</style>
