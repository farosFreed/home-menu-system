<script lang="ts" setup>
// import { defineProps } from "vue";
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  ingredients: {
    type: Array as PropType<string[]>,
    required: true,
  },
  instructions: {
    type: Array as PropType<string[]>,
    required: true,
  },
});
</script>
<template>
  <li>
    <h2>{{ title }}</h2>
    <!-- <ul>
        <li v-for="ingredient in ingredients" :key="ingredient">
            {{ ingredient }}
        </li>
        </ul>
        <ul>
        <li v-for="instruction in instructions" :key="instruction">
            {{ instruction }}
        </li>
        </ul> -->
  </li>
</template>
<style scoped></style>
