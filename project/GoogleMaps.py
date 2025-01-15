# from project import DataStructures
import DataStructures
# from project import credentials as credentials
import credentials as credentials
import requests
import re
#time it takes to get from a start
#point to an end point
#mode can be driving, walking or transit
def travel_time(origin, destination, mode):
    base_url = "https://maps.googleapis.com/maps/api/directions/json"
    
    params = {
        "key": credentials.maps_key0,
        "origin": origin,
        "destination": destination,
        "mode": mode,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if data["status"] != "OK":
            success = False
            api_keys = vars(credentials)
            for key, value in api_keys.items():
                if(key.startswith("maps_key")):
                    api_key = value
                    # print(api_key)
                    params = {
                        "key": value,
                        "origin": origin,
                        "destination": destination,
                        "mode": mode,
                    }
                    response = requests.get(base_url, params=params)
                    data = response.json()
                    if(data["status"]=="OK"):
                        success = True
                        break
            if not success:
                print("No usable Google Maps API keys")
                return

    if data["status"] == "OK":
        total_duration_seconds = data['routes'][0]['legs'][0]['duration']['value']
        
        #Turn the duration into an integer and minutes
        return int(round(total_duration_seconds / 60, 2))
    else:
        return "Error: Unable to calculate travel time."

#the amount of time it takes to travel from each activity to the next activity
#activities will be the itinerary in order and the hotel will be the hotel specified in the itenrary
def total_itinerary_travel_time(activities, hotel, mode):

    #Time taken to get from the hotel to the activity
    sum = travel_time(hotel, activities[0], mode) 
    
    #Time it takes to get from the start activity to all other activities in the itinerary
    for index in range(len(activities)-1):
       sum+=travel_time(activities[index], activities[index+1], mode) 
    
    #Time it takes to get from the last activity to home
    sum+=travel_time(activities[len(activities)-1], hotel, mode)

    return round(sum,2)


