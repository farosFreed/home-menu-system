// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",
  app: {
    baseURL: process.env.NODE_ENV === 'production' ? '/home-menu-system/' : '/'
  },
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
  nitro: {
    preset: 'github-pages',
    logLevel: 5, // Force nitro to print full error logs
    prerender: {
      crawlLinks: true
    }
  },
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'Home Menu App',
      short_name: 'Menu App',
      // must match github pages path
      scope: process.env.NODE_ENV === 'production' ? '/home-menu-system/' : '/',
      start_url: process.env.NODE_ENV === 'production' ? '/home-menu-system/' : '/',
      description: 'A Nuxt 3 Progressive Web App',
      theme_color: '#4A90E2',
      icons: [
        {
          src: process.env.NODE_ENV === 'production' ? '/home-menu-system/app-icon-small.png' : '/app-icon-small.png',
          sizes: '192x192',
          type: 'image/png',
        },
        {
          src: process.env.NODE_ENV === 'production' ? '/home-menu-system/app-icon.webp' : '/app-icon.webp',
          sizes: '512x512',
          type: 'image/webp',
        },
      ],
    },
    workbox: {
      // Safely prevents dual forward slashes when parsing assets in subfolders
      modifyURLPrefix: {
        '/_nuxt/': '/_nuxt/',
        '/': '/home-menu-system/'
      },
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
