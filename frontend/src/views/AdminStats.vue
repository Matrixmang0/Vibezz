<template>

      <h1 class="display-3 text-center">User Statistics</h1>


    <div class="flex-container">
      <div class="graph">
        <h2 class="display-5 text-center text-muted">Album Library</h2>
        <div>
          <canvas id="myChart1"></canvas>
        </div>
      </div>

      <div class="graph">
        <h2 class="display-5 text-center text-muted">User Distribution</h2>
        <div>
          <canvas id="myChart2"></canvas>
        </div>
      </div>      
    </div>

</template>

<script>

export default {
  name: 'AdminStats',
  data() {
    return {
      users: this.$route.meta.users,
      albums: this.$route.meta.albums,
    }
  },
  mounted() {
    // Function to generate random colors
    function getRandomColor(alpha) {
      const random255 = () => Math.floor(Math.random() * 256);
      return `rgba(${random255()}, ${random255()}, ${random255()}, ${alpha})`;
    }

    // First Graph: Number of Songs in Each Album
    const ctx1 = document.getElementById('myChart1');
    new Chart(ctx1, {
      type: 'bar',
      data: {
        labels: this.albums.map(album => album.title), // Extract album titles
        datasets: [{
          label: 'Number of Songs',
          data: this.albums.map(album => album.songs.length), // Number of songs in each album
          backgroundColor: Array.from({ length: this.albums.length }, () => getRandomColor(0.5))
        }],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          }
        }
      }
    });

    // Second Graph: Number of Users for Each Role ID
    const ctx2 = document.getElementById('myChart2');
    const roleCounts = {}; // Object to store role ID counts
    this.users.forEach(user => {
      const roleId = user.role_id;
      roleCounts[roleId] = (roleCounts[roleId] || 0) + 1; // Increment count for each role ID
    });
    new Chart(ctx2, {
      type: 'doughnut',
      data: {
        labels: Object.keys(roleCounts), // Role IDs
        datasets: [{
          data: Object.values(roleCounts), // Number of users for each role ID
          backgroundColor: Array.from({ length: Object.keys(roleCounts).length }, () => getRandomColor(0.5))
        }],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          }
        }
      }
    });
  }
}
</script>


<style scoped>
  .flex-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 50px;
  }

  .graph {
    width: 45%;
    padding: 20px;
    border: 1px solid #000;
    border-radius: 10px;
  }

  canvas {
    width: 100%;
    height: 100%;
  }

  h2 {
    margin-bottom: 20px;
  }

  h1 {
    margin-top: 10px;
  }


</style>