# edit the "with open" directory locations as this is mine.
# Results will be written in leakcreds.txt (change dirctory)
# Change the regex.json directory to where you cloned the repo and saved it.

import requests
import re
import json

def getText(filename):
    secret_file = input ("Path to JSfiles: ")
    with open(secret_file, 'r') as file:
        urls = file.read().split()
    return urls

def sendRequest(urls):
    with open('/home/hackershiv/leakcreds.txt', 'w') as output_file:  # This is where file will be written
        for url in urls:
            output_file.write(f"Results for URL: {url}\n")
            response = requests.get(url).text
            with open(r'/home/hackershiv/tools/regex.json', 'r') as file:
                json_data = json.load(file)
            for values in json_data:
                result = re.findall(values['pattern'], response)
                if result:
                    output_file.write(f"{values['secret']} has been found!\n")
                    output_file.write(f"Value is {set(result)}\n\n")

# Usage
urls = getText('secret_file')
sendRequest(urls)
