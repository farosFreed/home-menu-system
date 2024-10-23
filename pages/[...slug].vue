<script></script>
<template>
  <main>
    <!-- Nuxt Content provides ContentDoc component to render content -->
    <ContentDoc v-slot="{ doc }">
      <MenuItemFull v-if="doc" :item="doc" />
    </ContentDoc>
  </main>
</template>
