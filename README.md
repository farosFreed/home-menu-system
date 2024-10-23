# Home Menu System

We want to grab relevant data from common recipes sites and save it in a format we can save/use locally.

Currently I am just pasting urls into this spreadsheet
https://docs.google.com/spreadsheets/d/1r9qN7Bc8wwT-T5EVMZW8tcuqU7J8bLI8lYeTmff0hj8/edit?gid=0#gid=0

## Design Musings

(Done) Priority #1: Prevent Scrape Spam during testing
We will do this by only visiting and scraping each submitted recipe source once. We then save the raw output to run our HTML parsers against however many times we need. We should then blacklist the exact url to prevent-rescraping. This blacklist can serve as a list of recipes.

Priority #2: Smart Parsing
What are some ideas we can use for this? Maybe we can paste HTML from many sites into chat gpt and see if it notices patterns we don't? Currently parsing is basic.

Priority #3: Nice, searchable UI
Can we use this project to learn more elastic search?

### Project Log

- [x] save raw output somewhere we can reuse
- [x] save successfully scrape urls to blacklist / recipe list file
- [x] parameterize URL in scrape.py
- [x] use URL to lookup raw output file, use beautifulSoup to get title
- [x] ingredient list if possible (look for 'ingredient' then `<li>`?)
- [x] output to JSON?
- [x] use JSON to generate webpage (look at NUXT CONTENT for this https://content.nuxt.com/) https://github.com/nuxt/content
- [x] generate individual recipe pages with nuxt content
- [x] use components to display data nicely
- [ ] explore solutions to download images
- [ ] implement a search, use elastic search?
- [ ] (STRETCH GOAL) standardize data (strip out '[]' characters etc) and add nicer styles, always nicer styles
- [ ] (STRETCH GOAL) use AI to analyze scraped output for recipes details and find patterns?
- [ ] (STRETCH GOAL) notice youtube links and save video instead? or can we scrape reliably from video description?

## Nuxt Stuff

### Setup

Make sure to install the dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

### Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm run dev

# yarn
yarn dev

# bun
bun run dev
```

### Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm run build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm run preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
