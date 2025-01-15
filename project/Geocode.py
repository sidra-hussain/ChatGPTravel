import http.client, urllib.parse
import credentials as credentials
import json


def geocode(address):
    conn = http.client.HTTPConnection('api.positionstack.com')

    params = urllib.parse.urlencode({
        'access_key': credentials.geo_api_key,
        'query': address,
        'limit': 1,
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    try:
        res = conn.getresponse()
        data = res.read()
        json_data = json.loads(data.decode("utf-8"))
        lat = json_data['data'][0].get("latitude")
        lng = json_data['data'][0].get("longitude")
        return lat, lng
    except:
        return "Error geocoding address"
