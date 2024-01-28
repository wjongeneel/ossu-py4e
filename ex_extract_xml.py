import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Input url and context to get decoded xml 
def get_xml(url, ctx):
    try:
        xml = urllib.request.urlopen(url, context=ctx).read().decode()
        return xml 
    except: 
        print(f'cannot open url: {url}')
        quit()

# Parse counts from comments in xml and return array of count values
def parse_comments_from_xml(xml):
    tree = ET.fromstring(xml)
    count_list = [int(count.text) for count in tree.findall('.//count')]
    return count_list

def main(): 
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    # Get url input 
    url = input('Enter URL: ')

    # Get xml
    xml = get_xml(url, ctx) 

    # Get list of comment counts
    count_list = parse_comments_from_xml(xml)

    # Print out result
    print(sum(count_list))

if __name__ == "__main__":
    main()