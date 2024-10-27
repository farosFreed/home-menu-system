<script lang="ts" setup>
// Create a query looking for anything in content/ directory
const { data } = await useAsyncData("home", () => queryContent().find());
</script>
<template>
  <main>
    <h1>Cafe de Oleson Menu</h1>
    <MenuItemPreview v-if="data" :items="data" />
  </main>
</template>
<style lang="scss" scoped>
main {
  margin: 0 auto;
  text-align: center;
  padding: 1rem;
}
</style>
