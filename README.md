# Home Menu System

We want to grab relevant data from common recipes sites and save it in a format we can save/use locally.

Currently I am just pasting urls into this spreadsheet
https://docs.google.com/spreadsheets/d/1r9qN7Bc8wwT-T5EVMZW8tcuqU7J8bLI8lYeTmff0hj8/edit?gid=0#gid=0

## Design Musings

Priority #1: Prevent Scrape Spam during testing
We will do this by only visiting and scraping each submitted recipe source once. We then save the raw output to run our HTML parsers against however many times we need. We should then blacklist the exact url to prevent-rescraping. This blacklist can serve as a list of recipes.

Priority #2: Smart Parsing
What are some ideas we can use for this? Maybe we can paste HTML from many sites into chat gpt and see if it notices patterns we don't?

### Project Log

- [x] save raw output somewhere we can reuse
- [x] save successfully scrape urls to blacklist / recipe list file
- [x] parameterize URL in scrape.py
- [x] use URL to lookup raw output file, use beautifulSoup to get title
- [x] ingredient list if possible (look for 'ingredient' then `<li>`?)
- [x] output to JSON?
- [ ] use JSON to generate webpage (look at NUXT CONTENT for this https://content.nuxt.com/) https://github.com/nuxt/content
- [ ] use AI to analyze scraped output for recipes details and find patterns?
- [ ] (STRETCH GOAL) notice youtube links and save video instead? or can we scrape reliably from video description?
- [ ] (STRETCH GOAL) scrape instragram posts, they return garbled output or output in a diff format https://scrapfly.io/blog/how-to-scrape-instagram/
