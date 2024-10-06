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

-[X] save raw output somewhere we can reuse -[X] save successfully scrape urls to blacklist / recipe list file -[ ] parameterize URL in scrape.py -[ ] document method better including param definitions and return output -[ ] analyze 4-5 scraped outputs and look for
