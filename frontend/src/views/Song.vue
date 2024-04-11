<template>
  <div class="song-player">
    <!-- Song Wallpaper -->
    <div class="song-wallpaper">
      <img :src="'http://127.0.0.1:5000/song/cover/' + song.id" alt="Song Wallpaper" class="wallpaper-img" />
    </div>
    <!-- Song Details -->
    <div class="song-details">
      <h2>{{ song.title }}</h2>
      <h3>Artist: {{ song.artist.name }}</h3>
      <p class="lyrics">{{ song.lyrics }}</p>
      <div class="buttons">
        <button type="button" class="btn btn-primary">
          <i class="fa-solid fa-plus"></i> Add
        </button>
        <button type="button" class="btn btn-warning">
          <i class="fa-solid fa-flag"></i> Flag
        </button>
      </div>
    </div>
    <!-- Audio Controls -->
    <div class="audio-controls">
      <audio controls autoplay controlsList="nodownload">
        <source :src="'http://127.0.0.1:5000/song/audio/' + song.id" type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      song: this.$route.meta.song,
    };
  },
  name: 'Song',
};
</script>

<style scoped>
.song-player {
  display: flex;
  height: 100vh;
  background-image: linear-gradient(to right, #141e30, #243b55);
  color: #fff;
  font-family: 'Montserrat', sans-serif;
}

.song-wallpaper {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.wallpaper-img {
  max-width: 100%;
  max-height: 100%;
  filter: brightness(0.7);
  transform: scale(1.2);
}

.song-details {
  flex: 1;
  padding: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.song-details h2 {
  font-size: 32px;
  margin-bottom: 10px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.song-details h3 {
  font-size: 20px;
  color: #bbb;
  margin-bottom: 20px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.song-details .lyrics {
  font-size: 18px;
  line-height: 2;
  margin-bottom: 30px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.buttons {
  display: flex;
  justify-content: center;
  align-items: center;
}

.btn {
  font-size: 16px;
  padding: 10px 20px;
  border-radius: 20px;
  transition: background-color 0.3s;
  color: #fff;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  margin-right: 15px;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-warning {
  background-color: #ffc107;
  border-color: #ffc107;
  margin-left: 15px;
}

.btn-warning:hover {
  background-color: #e0a800;
  border-color: #e0a800;
}

.btn i {
  margin-right: 8px;
}

.audio-controls {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  z-index: 999;
}

audio {
  width: 100%;
  background-color: transparent;
  filter: invert(1);
}

audio::-webkit-media-controls-panel {
  background-color: transparent;
}

audio::-webkit-media-controls-play-button,
audio::-webkit-media-controls-pause-button,
audio::-webkit-media-controls-current-time-display,
audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-timeline,
audio::-webkit-media-controls-volume-slider {
  filter: none;
}
</style>
