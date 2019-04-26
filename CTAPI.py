import requests


def geoInfo(APIKey, address):

    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), APIKey))
    try:
        geodata = dict()
        response = requests.get(url)
        resp_json = response.json()
        lat = resp_json['results'][0]['geometry']['location']['lat']
        lng = resp_json['results'][0]['geometry']['location']['lng']
        # format for output
        result = resp_json['results'][0]
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']

    except:

        print('ERROR: {}'.format(address))
        lat = 0
        lng = 0
    print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
    return lat, lng

APIKEY = 'AIzaSyCUNUiey3wyJEZ0BUHWuu1_9Yl6KPgdNSI'
add = 'abo tarek'

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

x, y = geoInfo(APIKEY, add)
print(x)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(y)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
