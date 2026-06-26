import requests # for HTTP requests
import os # for file operations
import urllib # for URL encoding
import urllib.request # for downloading images
import sys # for command line arguments 
from bs4 import BeautifulSoup # for HTML parsing
import json # write to JSON file
import re # for regex
import zstandard # for decompressing zstd files
# import xml.etree.ElementTree as ET # for XML parsing
# import asyncio  #todo do we need to make playwright call async?
from playwright.sync_api import sync_playwright # easier to wait for page load before scraping with playwright

## VARS
blacklist = 'menu-list.txt'
current_file_directory = os.path.dirname(os.path.abspath(__file__))
target_folder_name = 'raw_html'

# Save the response to a file
def write_response(response, folder_name=target_folder_name, url=None, content=None):
    print(type(response))
    # Construct the path to the target folder
    target_folder = os.path.join(current_file_directory, folder_name)
    
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Create a safe filename from the URL
    response_url = getattr(response, 'url', 'Generic-Recipe')
    working_url = response_url if url is None else url
    # working_url = (response.url if response.url is not None else "Receipe") if url is None else url
    filename = urllib.parse.quote(working_url, '')

    # Construct the full file path
    filepath = os.path.join(target_folder, filename)

    working_response = response.content if content is None else content
    with open(filepath, "wb+") as f: #wb+ for binary files like html
        f.write(working_response)

    # Append the URL to the menu-list.txt file
    with open(blacklist, 'a') as fh:
        fh.write(working_url + '\n')

# STEP #1: Scrape the website & save the HTML
def scrape_site(url):
    all_links = []
    try:
        with open(blacklist) as fh:
            all_links = fh.read().split('\n')
    except FileNotFoundError:
        print("menu-list.txt file not found.")
        all_links = []

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

        # if response successful, save the HTML
        if response.status_code == 200:
            if response.headers.get('Content-Encoding') == 'zstd':
                    dctx = zstandard.ZstdDecompressor()
                    decoded_content = dctx.decompress(response.content, max_output_size=104857600)

                    ## TODO needed to address 'zstd.ZstdError: could not determine content size in frame header' error when scraping 
                    ## TODO https://ohsweetbasil.com/instant-pot-award-winning-chili-recipe/
#                     ZStandardDcmp = zstd.ZstdDecompressor()

                    # compressedData = base64.b64decode(Base64EncodedData)
                    # stream_reader = ZStandardDcmp.stream_reader(compressedData)
                    # decompressedTXTData = stream_reader.read().decode('utf-8-sig')
                    # stream_reader.close()

                    # Process the decoded content
                    print('decoded content')
                    write_response(decoded_content)
            else:
                print('response text')
                write_response(response)

        else:
            print("Failed to retrieve the website")
            print(f"Error: {response.status_code}")

## TODO implement this as an option passed with initial command? 
## OR as something that can be called from the html analysis step?
def open_browser_with_playwright(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
         # Wait for the page to reach a specific load state
        page.wait_for_load_state("load")  # or "domcontentloaded", "networkidle"
        # title = page.title()
        # print(title)
        data = page.content()
        browser.close()
        # print('playwright data', data)
        return str.encode(data) # encode to bytes for writing to file

def open_filename_by_url(url):
    filename = urllib.parse.quote(url, '')
    path = os.path.join(current_file_directory, target_folder_name, filename)
    with open(path, 'rb') as f:
        return BeautifulSoup(f.read(), 'lxml') # TODO add 'html.parser' for instagram content?

# STEP #2 Analyze the saved HTML
def analyze_html(url): 

    # open filename based on url
    # path = os.path.join(current_file_directory, target_folder_name, filename)
    # with open(path, 'rb') as f:
    #     soup = BeautifulSoup(f.read(), 'lxml')
    soup = open_filename_by_url(url)
    filename = urllib.parse.quote(url, '')

    ## Title ##
    title = soup.select('html head title')
    # print('title', title)

    # if title is list:
    #     print('title is list')
    #     title = title[0].text
    # else:
    #     print(type(title))

    # if titl
    #     print("No title found.")
    #     return

    ## Ingredients ##
    # Find all <li> elements with a class containing "ingredient"
    ingredient_regex = re.compile(".*ingredient.*")
    li_elements = soup.find_all('li', {"class":ingredient_regex})
    # If no ingredients found, try to find any element with a class containing "ingredient"
    if len(li_elements) == 0:
        print("No ingredients found, trying another pattern.")
        li_elements = soup.find_all('div', class_=ingredient_regex)
        print('li_elements', li_elements)
        # class_=re.compile('ingredient')


    if len(li_elements) == 0:
        print("Still no ingredients found, trying Playwright.")
        # try to get the page content with playwright
        html = open_browser_with_playwright(url)
        print('html type', type(html))
        # print('html returned to playwright', html)
        # write response to file and then reassign soup
        write_response({}, url=url, content=html)
        soup = open_filename_by_url(url)
        li_elements = soup.find_all('div', class_=ingredient_regex)
        print('li_elements', li_elements)

        # playwright_soup = BeautifulSoup(html_string, 'html.parser')
        # li_elements = playwright_soup.find_all('div', class_=ingredient_regex)
        # print('li_elements', li_elements)


        # if len(li_elements) == 0:
        #     print("Still no ingredients found, trying another pattern.")
        #     # check for marleyspoon pattern
        #     li_elements = soup.find_all('div', attrs={"class":ingredient_regex})
        #     li_elements_nested = []
        #     for el in li_elements:
        #         print(el.find('p').text)
        #         li_elements_nested.append(el.find('p').text)
        #     li_elements = li_elements_nested
        #     print(li_elements)

    ingredients = []
    for li in li_elements:
        print(li.text)
        #remove ▢ character from start of string if it exists
        if li.text.startswith('▢'):
            ingredients.append(li.text[1:])
        else:
            ingredients.append(li.text)

    ## Instructions ##
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

    ## Image ##
    # look for first string starting with 'https://' and ending with '.jpg', inside a meta tag og:image
    image_regex = re.compile("https://.*\.jpg")
    image_url = soup.find('meta', {'property':'og:image'})['content']
    print("imageurl" + image_url)
    image_filename = filename.replace('%', '').replace('.','') #create a safe filename
    save_as = 'images/' + image_filename + '.jpg'
    save_as_path = os.path.join(current_file_directory, 'public', save_as)
    # if file does not exist, download it
    if not os.path.exists(save_as_path):
        # add browser headers to request image download
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(image_url, save_as_path)
        print("Image downloaded.")
    else:
        print("Image already exists.")

        # Create a dictionary with the above book information
    data = { 'url': url, 'title': title[0].text, 'ingredients': ingredients, 'instructions': instructions, 'image':save_as }
    save_json(data, title[0].text)


# STEP #3: Save the analysis as a JSON object
def save_json(data, title):
    # make title safe for filename
    filename = title.replace(' ', '_') + '.json'
    # filename = urllib.parse.quote(title, '') + '.json'
    with open('content/' + filename, 'w') as f: #encoding='latin-1'
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