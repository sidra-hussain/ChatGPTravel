import credentials as credentials
from AIParse import parse_activities, parse_restaurants
from DataStructures import Activity, Hours
from ChatGPT_AI import filter_activities_ai
# import project.credentials
# from project.AIParse import parse_activities, parse_restaurants
# from project.DataStructures import Activity, Hours
import requests
import json
import re
from datetime import datetime
from Amadeus import get_activity_cost
from Geocode import geocode
from geopy.geocoders import Nominatim

def get_lat_long(location):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(location)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

def generate_bounding_boxes(center_lat, center_lon, box_diameter):
    # Define cardinal directions
    directions = ['north', 'south', 'east', 'west']

    # Initialize list to store bounding boxes
    bounding_boxes = []
    box1= ((center_lat, center_lon), (center_lat-(box_diameter / (2 * 111111)), center_lon-(box_diameter / (2 * 111111))))
    bounding_boxes.append(box1)
    box2 = ((center_lat +(box_diameter / (2 * 111111))), center_lon), (center_lat, center_lon-(box_diameter / (2 * 111111)))
    bounding_boxes.append(box2)
    box3 = ((center_lat+(box_diameter / (2 * 111111)), center_lon+(box_diameter / (2 * 111111))) , (center_lat, center_lon))
    bounding_boxes.append(box3)
    box4 = ((center_lat, center_lon+(box_diameter / (2 * 111111))), ((center_lat -(box_diameter / (2 * 111111))), center_lon))
    bounding_boxes.append(box4)

    return bounding_boxes

# need to standardize the phone numbers across foursquare and yelp
# also need to figure out how to return cost

def get_activity_information(latitude, longitude):
    api_key = credentials.foursquare_key0
    final_act = []

    # coordinates = get_lat_long(dest)
    # latitude=coordinates[0]
    # longitude=coordinates[1]

    # api_key = project.credentials.foursquare_key
    url = "https://api.foursquare.com/v3/places/search"

    headers = {
        "Accept": "application/json",
        "Authorization": f"{api_key}"
    }

    bounding_boxes = generate_bounding_boxes(latitude, longitude, 20000)
    for box in bounding_boxes:
        ne = box[0]
        sw = box[1]

        params = {
            "ne": f"{ne[0]},{ne[1]}",
            "sw": f"{sw[0]},{sw[1]}",
            "limit": 50,
            "fields": "fsq_id,name,location,geocodes,tel,price,categories,hours,rating,website",
            "exclude_all_chains": True
        }

        response = requests.request("GET", url, params=params, headers=headers)

        # Handle API Rate Limit 
        if response.status_code == 401:
            success = False
            api_keys = vars(credentials)
            for key, value in api_keys.items():
                if(key.startswith("foursquare_key")):
                    api_key = value
                    headers = {
                        "Accept": "application/json",
                        "Authorization": f"{api_key}"
                    }
                    response = requests.request("GET", url, params=params, headers=headers)
                    if(response.status_code == 200):
                        success = True
                        break
            if not success:
                print("No usable Foursquare API keys")
                return
            
        # gets first result from the request
        data = response.json()
        # business = data['results'][0]
        businesses = data['results']
        # print(businesses)
        for business in businesses:
            # puts the data into json format
            # formatted_json = json.dumps(business, indent=4)
            # print(formatted_json)

            prefix = business["categories"][0]["icon"]["prefix"]
            split = prefix.split("/")[5]
            if (split == "food" or split =="nightlife"):
                continue
            
            try:
                # create a list of dictionaries with time objects to be put into Hours object
                days = []
                day_count = 1
                for i in business["hours"]["regular"]:
                    day_hours = []
                    open_time = datetime.strptime(i["open"], "%H%M").time()
                    close_time = datetime.strptime(i["close"], "%H%M").time()
                    day_hours.append({"open": open_time, "close": close_time})
                    if (day_count == i["day"]):
                        days.append(day_hours)
                        day_count += 1
                    else:
                        days[day_count-1].append({"open": open_time, "close": close_time})

                hours = Hours(
                    Monday = days[0],
                    Tuesday = days[1],
                    Wednesday = days[2],
                    Thursday = days[3],
                    Friday = days[4],
                    Saturday = days[5],
                    Sunday = days[6]
                )

                # populates an activity object with information
                activity = Activity(
                    name=business["name"],
                    address=business["location"]["formatted_address"],
                    latitude=business["geocodes"]["main"]["latitude"],
                    longitude=business["geocodes"]["main"]["longitude"],
                    phonenumber=re.sub("[^0-9]","", business["tel"]) if "tel" in business else "None",
                    cost=foursquare_price(business["price"]) if "price" in business else 0.0,
                    cost_estimate=foursquare_cost_estimate(business["price"]) if "price" in business else '$',
                    category=business["categories"][0]["name"] if isinstance(business["categories"], list) else business["categories"]["name"],
                    hours=hours,
                    isBreakfast=False,
                    isLunch=False,
                    isDinner=False,
                    rating=(business["rating"]/2) if 'rating' in business else 'N/A',
                    website=business["website"] if 'website' in business else 'N/A'
                )
                final_act.append(activity)
            except:
                pass


    # return the full activity
    return final_act


def foursquare_price(price_scale):
    if price_scale == 1:
        return 10.0
    elif price_scale == 2:
        return 20.0
    elif price_scale == 3:
        return 45.0
    else:
        return 75.0

def foursquare_cost_estimate(price_scale):
    if price_scale == 1:
        return "$"
    elif price_scale == 2:
        return "$$"
    elif price_scale == 3:
        return "$$$"
    else:
        return "$$$$"

def list_activity_names(activities):
    activity_string = ""
    i=0
    for activity in activities:
        activity_string += f"{activity.name}\n"
        i+=1
    return activity_string

def filter_activities(lat, long, preferences, num_days):
    activities = get_activity_information(lat, long)
    activity_string = list_activity_names(activities)
    filtered_activities = filter_activities_ai(activity_string, preferences, num_days)
    final_activities = []
    for activity in activities:
        if activity.name in filtered_activities:
            final_activities.append(activity)
    
    return final_activities

# for i in range(100):
#     url = "https://api.foursquare.com/v3/places/search"
#     api_key = credentials.foursquare_key0

#     headers = {
#         "Accept": "application/json",
#         "Authorization": f"{api_key}"
#     }

#     params = {
#         "query" : "Vegas"
#     }

#     response = requests.request("GET", url, params=params, headers=headers)
#     print(response.status_code)


# activities = filter_activities(36.039165, -115.148829, "Museums, Shopping")
# for activity in activities:
#     print(activity.name)
# activities = parse_activities()
# get_activity_information(activities[1], 36.039165, -115.148829)
# verified_act = verify_activities(activities)
# for act in verified_act:
#     print(act)
#     print("*"*40)

# term = "fun"
# latlng = geocode("3799 S Las Vegas Blvd, Las Vegas, NV 89109")
# info = get_activity_information(latlng[0], latlng[1])
# print(len(info))
# for i in info:
#     print(i, '*'*20, '\n')