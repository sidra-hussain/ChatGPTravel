import requests
import json
import re
from datetime import datetime
import credentials

def get_activity_cost(activity):
    #Obtain an access token
    token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    token_data = {
        "grant_type": "client_credentials",
        "client_id": credentials.amadeus_key0,
        "client_secret": credentials.amadeus_secret0
    }
    # print(f"Checking: {activity.name}")
    response = requests.post(token_url, data=token_data)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        # print("Access token: " + access_token)
    else:
        print("Failed to obtain access token")
        exit()

    # Tours and Activities API
    tours_and_activities_url = "https://test.api.amadeus.com/v1/shopping/activities/by-square"

    # Define your search criteria
    search_criteria = {
        "north": activity.latitude + 0.001,
        "west": activity.longitude - 0.001,
        "south": activity.latitude - 0.001, 
        "east": activity.longitude + 0.001,
    }

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(tours_and_activities_url, params=search_criteria, headers=headers)
    
    # Handle API Rate Limit
    if response.status_code != 200:
        success = False
        api_keys = vars(credentials)
        for key, value in api_keys.items():
            for secret, secretValue in api_keys.items():
                last_char = key[-1]
                if(key.startswith("amadeus_key") and secret == ("amadeus_secret"+last_char)):
                    api_key = value
                    api_secret = secretValue
                    #Obtain an access token
                    token_data = {
                        "grant_type": "client_credentials",
                        "client_id": api_key,
                        "client_secret": api_secret
                    }
                    response = requests.post(token_url, data=token_data)

                    if response.status_code == 200:
                        access_token = response.json()["access_token"]
                    else:
                        print("Failed to obtain access token")
                        continue
                    
                    response = requests.get(tours_and_activities_url, params=search_criteria, headers=headers)
                    if(response.status_code == 200):
                        success = True
                        break
                if success:
                    break
            if not success:
                print("No usable Amadeus API keys")
                return
    
    oldCost = activity.cost

    if response.status_code == 200:
        # gets first result from the request
        data = response.json()
        if not data['data']:
            # print("No Cost Found")
            return
        
        # print(data)
        
        result = data['data'][0] if isinstance(data['data'], list) and data['data'] else data['data']
        price = result['price']['amount']
        price_unit = result['price']['currencyCode']
        # print(f"Price: {price}")
        if(float(price) > 0):
            activity.cost = price
            # print("Old Cost: " + str(oldCost) + ", New Cost: " + str(activity.cost))
    else:
        print(f"Error {response.status_code}: {response.text}")

    # return the full activity
    return activity