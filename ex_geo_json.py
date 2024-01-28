import json
import ssl
import urllib.request, urllib.parse, urllib.error

def get_json(url, ctx):
    try: 
        print(f'Retrieving {url}')
        data = urllib.request.urlopen(url, context=ctx)
        data = data.read().decode()
        print(f'Retrieved {len(data)} characters')
        try: 
            json_dict = json.loads(data)
        except: 
            json_dict = None
    except: 
        print(f'cannot open url: {url}')
        quit()
    return json_dict

def main(): 
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Service url 
    service_url = 'http://py4e-data.dr-chuck.net/json?'

    # Get url input
    address = input('Enter location: ')

    # Set request parameters and encode url 
    params = dict()
    params['key'] = 42
    params['address'] = address
    url = service_url + urllib.parse.urlencode(params)
    
    # Get response using the formatted url and ctx and parse place_id
    data = get_json(url, ctx)
    place_id = data['results'][0]['place_id']
    print(f'Place id {place_id}')

if __name__ == "__main__":
    main()