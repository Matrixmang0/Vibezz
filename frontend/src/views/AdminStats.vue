<template>

      <h1 class="display-3 text-center">User Statistics</h1>


    <div class="flex-container">
      <div class="graph">
        <h2 class="display-5 text-center text-muted">Books in Library</h2>
        <div>
          <canvas id="myChart1"></canvas>
        </div>
      </div>

      <div class="graph">
        <h2 class="display-5 text-center text-muted">Books Purchased</h2>
        <div>
          <canvas id="myChart2"></canvas>
        </div>
      </div>      
    </div>

    <div class="flex-container">
      <div class="graph">
          <h2 class="display-5 text-center text-muted">Books Borrowed</h2>
          <div>
            <canvas id="myChart3"></canvas>
          </div>
      </div>
    </div>

</template>

<script>
export default {
  name: 'AdminStats'
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