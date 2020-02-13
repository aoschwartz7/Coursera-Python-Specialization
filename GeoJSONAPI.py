# Using the GeoJSON API
# This program will use a GeoLocation lookup API modelled after
# the Google API to look up some universities and parse the returned data.
# The program will prompt for a location, contact a web service and retrieve JSON
# for the web service and parse that data, and retrieve the first place_id from
# the JSON. A place ID is a textual identifier that uniquely identifies
# a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    # create dictionary for storing parameters
    parms = dict()
    # insert address search into parms
    parms['address'] = address
    # insert API key into parms
    if api_key is not False: parms['key'] = api_key
    # encode address search + api key into service url
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    # use urlopen to treat url like file to read data
    uh = urllib.request.urlopen(url, context=ctx)
    # decode binary and read data
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    # check if JSON data can be loaded
    try:
        js = json.loads(data)
    except:
        js = None
    # if JSON data cannot be loaded, escape
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # if JSON data can be loaded, parse JSON for these parameters
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    # print(location)
    print(js["results"][0]["place_id"])
