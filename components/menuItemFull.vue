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
    <div class="col-1">
      <h2 v-if="item.title">{{ item.title }}</h2>
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
    <div class="col-2">
      <img class="full-image" :src="item.image" :alt="item.title" />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.menu-item-full {
  display: flex;
  flex-direction: row-reverse;
  .col-1,
  .col-2 {
    flex: 1;
    padding: 1rem;
    height: 94vh;
    overflow: scroll;
    .full-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
  @media screen and (max-width: 768px) {
    flex-direction: column-reverse;
    .col-1,
    .col-2 {
      height: auto;
      .full-image {
        width: 100%;
        height: 40vh;
      }
    }
  }
}
</style>
