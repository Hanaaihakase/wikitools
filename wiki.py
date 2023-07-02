import requests
import re
from file import *

def create_name(title, site, lang):
    # Output the complete name
    name = f"{title}_{lang}_{site}"
    name = name.replace("/", "_")
    return name

def create_dir(site, lang, type):
    # Output the complete directory
    dir = fr".\{site}\{lang}\{type}"
    return dir

def get_wiki(title, site, lang, type):
    # Output the complete name snd dir
    name = create_name(title, site, lang)
    dir = create_dir(site, lang, type)

    # Use the Wiki API to get the page content
    url = f"https://{lang}.{site}.org/w/api.php?action=query&prop=extracts&format=json&titles={title}"
    print(f"The url link is {url}")
    response = requests.get(url)
    data = response.json()

    # Get the content
    page = data["query"]["pages"]
    content = page[next(iter(page))]["extract"]

    # Write it
    file_write(dir, name, type, content)

def delink(title, site, lang, type):
    # Output the complete name snd dir
    name = create_name(title, site, lang)
    dir = create_dir(site, lang, type)

    # Read the file from the file path
    content = file_read(dir, name, type)
    path = fr"{dir}\{name}.{type}"

    # Delete all the <link>
    content = re.sub(r'<link\s.*?>', '', content, flags=re.DOTALL)

    # Write the file to the file path
    file_write(dir, name, type, content)

    print(fr"All <link> marks in {path} has been deleted!")

