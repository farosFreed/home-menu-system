<script lang="ts" setup>
// Create a query looking for anything in content/ directory
const items = await queryContent().find();
</script>
<template>
  <main>
    <h1>Cafe de Oleson Menu</h1>
    <ul>
      <li v-for="item in items" :key="item.url">
        {{ item.title }}
        {{ item.ingredients }}
        {{ item.instructions }}
      </li>
    </ul>
  </main>
</template>
