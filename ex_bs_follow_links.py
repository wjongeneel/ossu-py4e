# Imports
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Gets the new url at given position from the inserted url 
def get_url(url, position, context):
    url = url
    try:
        html = urllib.request.urlopen(url, context=context).read()
    except: 
        print(f'cannot open url: {url}')
        quit()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return str(tags[position - 1].get('href',None))

def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Get url input
    url = input('Enter URL: ')

    # Get repetitions input
    try:
        repetitions = int(input('Enter count: '))
    except TypeError: 
        print('please enter an int for repetitions')
        quit()

    # Get position input
    try:
        position = int(input('Enter position: '))
    except TypeError:
        print('please enter an int for position')
        quit()
    
    # Run program for the given url, repetitions and position
    while repetitions + 1 > 0:
        print(f'Retrieving: {url}')
        url = get_url(url, position, ctx)
        repetitions -= 1

if __name__ == "__main__":
    main()

