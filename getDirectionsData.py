import urllib.request
import json
import credentials

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
#origin = input('Where are you?: ').replace(' ', '+')
#destination = input('Where do you want to go?: ').replace(' ','+')
origin='Mexico'
destination = 'Argentina'
nav_request = 'origin={}&destination={}&key={}'.format(origin, destination, credentials.api_key)

request = endpoint + nav_request

response = urllib.request.urlopen(request).read()
jsonResponse = json.loads(response.decode('utf-8'))

print(jsonResponse)