<template>
  <div v-if="active" class="loader-wrapper">
    <div class="loader">
      <div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div>
    </div>
    <p>{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: 'LoadingSpinner',
  props: {
    active: Boolean,
    text: String
  }
}
</script>

<style scoped>
p {
  font-size: 0.8em;
  font-weight: 300;
  margin-top: 5px;
  letter-spacing: 1px;
  color: white;
}

.loader-wrapper {
  text-align: center;
}

.loader {
  width: 48px;
  height: 48px;
  border: 5px solid;
  border-color: #8DD0FF transparent;
  border-radius: 50%;
  display: inline-block;
  box-sizing: border-box;
  animation: rotation 0.5s linear infinite;
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
