<script lang="ts" setup>
// TODO implement types
type MenuItem = {
  title: string;
  ingredients: string;
  instructions: string;
  url: string;
};
const props = defineProps({
  items: {
    type: Array as PropType<any[]>,
    required: true,
  },
});

// When clicking the list item, navigate to the item's path
const handleClick = async (item_path: string) => {
  await navigateTo(item_path);
};
</script>
<template>
  <ul class="menu-item">
    <li v-for="item in items" :key="item.url" @click="handleClick(item._path)">
      <img class="preview-image" :src="item.image" :alt="item.title" />
      <h3>
        <NuxtLink :to="item._path">{{ item.title }}</NuxtLink>
      </h3>
      <p class="preview">{{ item.ingredients }}</p>
    </li>
  </ul>
</template>
<style lang="scss" scoped>
$radius: 1rem;
$spacer: 1rem;
$lightblue: #d4e7f9;
ul.menu-item {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: $spacer;
  li {
    list-style-type: none;
    border: 1px solid #ccc;
    border-radius: $radius;
    margin-top: $spacer;
    padding: $spacer;
    cursor: pointer;
    &:hover {
      background-color: $lightblue;
    }
    .preview-image {
      width: 100%;
      height: 20vh;
      object-fit: cover;
      border-radius: $radius;
    }
    .preview {
      display: -webkit-box;
      line-clamp: 2;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
  }
  @media screen and (max-width: 768px) {
    grid-template-columns: 1fr 1fr;
  }
  @media screen and (max-width: 540px) {
    grid-template-columns: 1fr;
  }
}
</style>
