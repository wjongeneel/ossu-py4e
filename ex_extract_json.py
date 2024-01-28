import json
import ssl
import urllib.request, urllib.parse, urllib.error

def get_json(url, ctx):
    try: 
        data = urllib.request.urlopen(url, context=ctx)
    except: 
        print(f'cannot open url: {url}')
        quit()
    data = data.read().decode()
    return json.loads(data) 

def main(): 
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Get url input
    url = input('Enter URL: ')
    
    comments = get_json(url, ctx)['comments']
    comment_sum = int()
    for comment in comments: 
        comment_sum += comment['count']

    print(comment_sum)

if __name__ == "__main__":
    main()