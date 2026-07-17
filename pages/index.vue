<script lang="ts" setup>
import MiniSearch from 'minisearch'
// import searchContent from
// Create a query looking for anything in content/ directory
const { data } = await useAsyncData("home", () => queryContent().find());
// Search the data
const search = ref('');
const miniSearch = new MiniSearch({
  idField: '_path', // we don't have an id field in the data, so we use the path as the id
  fields: ['title'],
  storeFields: ['title', '_path'],
  searchOptions: {
    fuzzy: 0.2,
    prefix: true,
    boost: {
      title: 2,
    },
  },
});
miniSearch.addAll(data.value ?? []);

const filtered = computed(() => {
  console.log(data.value);
  if (!search.value) return data.value;

  // search for items in miniSearch and return a set of ids
  const ids = new Set(miniSearch.search(search.value).map(item => item._path))
  // return the items in data.value that have the ids
  return (data.value ?? []).filter(item => ids.has(item._path))
  // working with miniSearch data
  // let resultsLocal = miniSearch.search(search.value);
  // console.log(resultsLocal);
  // return resultsLocal;
});
</script>
<template>
  <main>
    <h1>Cafe de Oleson Menu</h1>
    <input v-model="search" placeholder="search" />
    <MenuItemPreview v-if="filtered.length > 0" :items="filtered" />
    <p v-else>No items found</p>
  </main>
</template>
<style lang="scss" scoped>
main {
  margin: 0 auto;
  text-align: center;
  padding: 1rem;
}
</style>
