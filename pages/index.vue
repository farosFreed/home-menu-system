<script lang="ts" setup>
// import searchContent from
// Create a query looking for anything in content/ directory
const { data } = await useAsyncData("home", () => queryContent().find());
// Search the data
const miniSearchOptions = defineMiniSearchOptions({
  fields: ["title"],
});
const search = ref("");
const results = ref([]);
</script>
<template>
  <main>
    <h1>Cafe de Oleson Menu</h1>
    <input v-model="search" placeholder="search" />
    <ContentList :query="{ where: { title: { $regex: `/${search}/ig` } } }">
      <template #default="{ list }">
        <MenuItemPreview :items="list" />
      </template>
      <template #not-found>
        <p v-if="search.length > 0">
          Nothing found for '{{ search }}'. Browse recipes below:
        </p>
        <MenuItemPreview v-if="data" :items="data" />
      </template>
    </ContentList>
  </main>
</template>
<style lang="scss" scoped>
main {
  margin: 0 auto;
  text-align: center;
  padding: 1rem;
}
</style>
