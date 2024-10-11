import requests # for HTTP requests
import os # for file operations
import urllib # for URL encoding
import sys # for command line arguments 
from bs4 import BeautifulSoup # for HTML parsing
import json # write to JSON file
import re # for regex

## VARS
blacklist = 'menu-list.txt'
current_file_directory = os.path.dirname(os.path.abspath(__file__))
target_folder_name = 'raw_html'

# Save the response to a file
def write_response(response, folder_name=target_folder_name):
    # Construct the path to the target folder
    target_folder = os.path.join(current_file_directory, folder_name)
    
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Create a safe filename from the URL
    filename = urllib.parse.quote(response.url, '')

    # Construct the full file path
    filepath = os.path.join(target_folder, filename)

    with open(filepath, "wb+") as f: #wb+ for binary files like html
        f.write(response.content)

    # Append the URL to the menu-list.txt file
    with open(blacklist, 'a') as fh:
        fh.write(response.url + '\n')

# STEP #1: Scrape the website & save the HTML
def scrape_site(url):
    all_links = []
    try:
        with open(blacklist) as fh:
            all_links = fh.read().split('\n')
    except FileNotFoundError:
        print("menu-list.txt file not found.")
        all_links = []

    print(all_links)

    # check all_links for url to prevent re-scraping
    if url in all_links:
        print("URL already scraped, getting html file...")
    else:
        # Headers to mimic browser
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(response.text)

            # save the HTML for later analysis
            write_response(response)

        else:
            print("Failed to retrieve the website")
            print(f"Error: {response.status_code}")


# STEP #2 Analyze the saved HTML
def analyze_html(url): 
    filename = urllib.parse.quote(url, '')
    path = os.path.join(current_file_directory, target_folder_name, filename)
    with open(path, 'rb') as f:
        soup = BeautifulSoup(f.read(), 'lxml') # TODO add 'html.parser' for instagram content?

        # Title
        title = soup.select('html head title')
        # Ingredients
        # Find all <li> elements with a class containing "ingredient"
        ingredient_regex = re.compile(".*ingredient.*")
        li_elements = soup.find_all('li', {"class":ingredient_regex})
        ingredients = []
        for li in li_elements:
            print(li.text)
            ingredients.append(li.text)
        # Instructions
        instruction_regex = re.compile(".*instruction.*")
        li_elements_2 = soup.find_all('li', {"class":instruction_regex})
        instructions = []
        # add get ol with prep steps
        for li in li_elements_2:
            print(li.text)
            instructions.append(li.text)
        
        if len(instructions) == 0:
            # try to find using 'prep' instead, as Tasty uses
            prep_regex = re.compile(".*prep.*")
            prep_elements = soup.find_all(['ol', 'ul'], {"class":prep_regex})
            for el in prep_elements:
                print(el.text)
                for li in el.find_all('li'):
                    print(li.text)
                    instructions.append(li.text)

         # Create a dictionary with the above book information
        data = { 'url': url, 'title': title[0].text, 'ingredients': ingredients, 'instructions': instructions }
        save_json(data, title[0].text)


# STEP #3: Save the analysis as a JSON object
def save_json(data, title):
    # make title safe for filename
    filename = title.replace(' ', '_') + '.json'
    # filename = urllib.parse.quote(title, '') + '.json'
    with open('json/' + filename, 'w') as f: #encoding='latin-1'
        json.dump(data, f, indent=8, ensure_ascii=False)
    print("Created Json File")


# START MAIN FUNCTION
if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        scrape_site(url)
        # then analyze the html, do we need to put this in a callback?
        analyze_html(url)
    else:
        print("Please provide a url.")