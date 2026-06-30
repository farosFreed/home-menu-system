// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  devtools: { enabled: true },
  modules: [
    '@nuxt/content',
    '@vite-pwa/nuxt'
  ],
  content: {
    experimental: {
      search: { indexed: true },
    },
  },
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'Home Menu App',
      short_name: 'Menu App',
      description: 'A Nuxt 3 Progressive Web App',
      theme_color: '#4A90E2',
      icons: [
        {
          src: '/app-icon-small.png',
          sizes: '192x192',
          type: 'image/png',
        },
        {
          src: '/app-icon.webp',
          sizes: '512x512',
          type: 'image/webp',
        },
      ],
    },
    workbox: {
      navigateFallback: '/',
      globPatterns: ['**/*.{js,css,html,png,svg,ico}'],
      runtimeCaching: [
        {
          urlPattern: '/^\/_content\/.*$/',
          handler: 'StaleWhileRevalidate',
          options: {
            cacheName: 'nuxt-content-cache',
            expiration: {
              maxEntries: 50,
              maxAgeSeconds: 60 * 60 * 24 * 30, // 30 days
            },
          },
        },
      ],
    },
    devOptions: {
      enabled: true,
      type: "module"
    }
  },
});
