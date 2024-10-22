<script lang="ts" setup>
// Create a query looking for anything in content/ directory

const items = await queryContent().find();
</script>

<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>
