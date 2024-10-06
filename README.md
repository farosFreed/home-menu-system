# Home Menu System

We want to grab relevant data from common recipes sites and save it in a format we can save/use locally.

## Design Musings

Priority #1: Prevent Scrape Spam during testing
We will do this by only visiting and scraping each submitted recipe source once. We then save the raw output to run our HTML parsers against however many times we need. We should then blacklist the exact url to prevent-rescraping. This blacklist can serve as a list of recipes.

### Project TO DOs

- save raw output somewhere we can reuse
- save successfully scrape urls to blacklist / recipe list file
