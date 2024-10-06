import requests
import os 
import urllib


# STEP #0: Variables & Functions

## VARS
blacklist = 'menu-list.txt'

## METHODS
# Save the response to a file
# TODO python method documention 
def write_response(response, folder_name='raw_html'):
    # Construct the path to the target folder
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(current_file_directory, folder_name)
    
    # Ensure the target folder exists
    os.makedirs(target_folder, exist_ok=True)

    # Create a safe filename from the URL
    filename = urllib.parse.quote(response.url, '')
    
    # Construct the full file path
    filepath = os.path.join(target_folder, filename)

    # filepath = os.path.join(filedir, filename)
    with open(filepath, "wb+") as f: #wb+ for binary files like html
        f.write(response.content)

    # Append the URL to the menu-list.txt file
    with open(blacklist, 'a') as fh:
        fh.write(response.url + '\n')


## TODO parametrize the URL
url = "https://tasty.co/recipe/instant-pot-french-dip-sandwich"

# STEP #1: Scrape the website & save the HTML
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
     print("URL already scraped, aborting ...")
     exit() # TODO exit the script? or just jump to step 2?
else:
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)

        # save the HTML for later analysis
        write_response(response)

    else:
        print("Failed to retrieve the website")



# STEP #2 Analyze the saved HTML
# with open('path/to/saving.html', 'rb') as f:
#     soup = BeautifulSoup(f.read(), 'lxml')
