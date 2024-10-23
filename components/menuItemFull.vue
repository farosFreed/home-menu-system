<script lang="ts" setup>
const { item } = defineProps({
  item: {
    type: Object as PropType<any>,
    required: true,
  },
});
</script>
<template>
  <div class="menu-item-full">
    <h2 v-if="item.title">{{ item.title }}</h2>
    [ IMAGE HERE ]
    <div v-if="item.ingredients">
      <h3>Ingredients</h3>
      <ul>
        <li v-for="ingredient in item.ingredients" :key="ingredient">
          {{ ingredient }}
        </li>
      </ul>
    </div>
    <div v-if="item.instructions">
      <h3>Instructions</h3>
      <ol>
        <li v-for="instruction in item.instructions" :key="instruction">
          {{ instruction }}
        </li>
      </ol>
    </div>
  </div>
</template>
<style lang="scss" scoped></style>
