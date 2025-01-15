# import project.credentials
# from project.AIParse import parse_activities, parse_restaurants
# from project.DataStructures import Activity, Hours
import credentials as credentials
from AIParse import parse_activities, parse_restaurants
from DataStructures import Activity, Hours
from ChatGPT_AI import filter_activities_ai, filter_restaurants_ai
import requests
import json
import phonenumbers
from datetime import datetime, time
#returns information about the specified business and loads it 
#into the activity data structure

def yelp_price(price_scale):
    if price_scale == "$":
        return 10.0
    elif price_scale == "$$":
        return 20.0
    elif price_scale == "$$$":
        return 45.0
    else:
        return 75.0


def get_business_information(term, location):

    # api_key = project.credentials.yelp_key
    api_key = credentials.yelp_key0
    final_res = []


    # Yelp API endpoint for searching businesses
    url = 'https://api.yelp.com/v3/businesses/search'
    # print(f"{term}, {location}")

    # Define the parameters for your search (limiting results to one business in the specified location)
    params = {
        'location': f'{location}',
        'term': f'{term}',
        'limit': 50,
        'radius': 30000  
    }

    # Set up the headers with your API Key
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    # Make the GET request to the Yelp API
    response = requests.get(url, params=params, headers=headers)

    # Handle API Rate Limit 
    if response.status_code == 429:
            success = False
            api_keys = vars(credentials)
            for key, value in api_keys.items():
                if(key.startswith("yelp_key")):
                    api_key = value
                    # print(api_key)
                    headers = {
                        'Authorization': f'Bearer {api_key}'
                    }
                    response = requests.get(url, params=params, headers=headers)
                    if(response.status_code == 200):
                        success = True
                        break
            if not success:
                print("No usable Yelp API keys")
                return

    # Check if the request was successful
    # print(response)
    data = response.json()
    # business = data['businesses'][0]  # Get the first business in the list
    businesses = data['businesses']
    for business in businesses:

        # Print detailed information about the business
        # formatted_json = json.dumps(data, indent=4)
        # print(formatted_json)

        # call business detail api to get hours
        bus_id = business["id"]
        new_url = f"https://api.yelp.com/v3/businesses/{bus_id}"
        new_response = requests.get(new_url, headers=headers)

        # Handle API Rate Limit
        if new_response.status_code == 429:
            success = False
            api_keys = vars(credentials)
            for key, value in api_keys.items():
                if(key.startswith("yelp_key")):
                    api_key = value
                    headers = {
                        'Authorization': f'Bearer {api_key}'
                    }
                    new_response = requests.get(url, params=params, headers=headers)
                    if(new_response.status_code == 200):
                        success = True
                        break
            if not success:
                print("No usable Yelp API keys")
                return
        
        new_data = new_response.json()

        # formatted_json = json.dumps(new_data, indent=4)
        # print(formatted_json)

        # create a list of dictionaries with time objects to be put into Hours object
        days = []
        day_count = 0
        if "hours" not in new_data:
            continue
        for i in new_data["hours"][0]["open"]:
            # print(day_count)
            if(day_count < i["day"]):
                for j in range(day_count, i["day"]):
                    days.append("Closed")
                day_count = i["day"]

            day_hours = []
            open_time = datetime.strptime(i["start"], "%H%M").time()
            close_time = datetime.strptime(i["end"], "%H%M").time()
            day_hours.append({"open": open_time, "close": close_time})
            if (day_count == i["day"]):
                days.append(day_hours)
                day_count += 1
            # case for if a restaurant closes and reopens on the same day
            else:
                days[day_count-1].append({"open": open_time, "close": close_time})
        if(day_count<=6):
            for i in range(day_count, 7):
                days.append("Closed")

        # print(days)
        # need to determine what to do with sections of hours
        hours = Hours(
            Monday = days[0],
            Tuesday = days[1],
            Wednesday = days[2],
            Thursday = days[3],
            Friday = days[4],
            Saturday = days[5],
            Sunday = days[6]
        )
        # standardized meal start times for restaurants
        b_s_time = time(6, 0)
        l_s_time = time(10, 0)
        d_s_time = time(15, 30)
        no_close = time(0,0)

        # logic for determing if restaurant offers breakfast/lunch/dinner based on hours
        isB = False
        isL = False
        isD = False
        if(type(hours.Wednesday[0]) != str):
            if (hours.Wednesday[0]["open"] >= b_s_time and hours.Wednesday[0]["open"] < l_s_time):
                isB = True
            if ((hours.Wednesday[0]["open"] >= l_s_time and hours.Wednesday[0]["open"] < d_s_time) or (hours.Wednesday[0]["close"] >= l_s_time and hours.Wednesday[0]["close"] <= d_s_time) or (hours.Wednesday[0]["open"] <= l_s_time and hours.Wednesday[0]["close"] >= d_s_time)):
                isL = True
            if ((hours.Wednesday[0]["open"] >= d_s_time) or (hours.Wednesday[0]["close"] >= d_s_time)):
                isD = True
            if ((hours.Wednesday[0]["open"] == no_close and hours.Wednesday[0]["close"] == no_close)):
                isB = True
                isL = True
                isD = True

        # Fill data class
        if "phone" in business and not business["phone"] == '':
            # string = business["phone"]
            # print(business)
            # print(f"{string} a")
            phone = phonenumbers.parse(business["phone"]).national_number
        else: 
            phone = ""
        activity = Activity(
            name=business["name"],
            address=business["location"]["display_address"],
            latitude=business["coordinates"]["latitude"],
            longitude=business["coordinates"]["longitude"],
            phonenumber= phone,
            cost=yelp_price(business["price"]) if "price" in business else 0.0,
            cost_estimate=business["price"] if "price" in business else "$",
            category=business["categories"][0]["title"],
            hours=hours,
            isBreakfast=isB,
            isLunch=isL,
            isDinner=isD,
            rating=business["rating"],
            website=business["url"]
        )
        final_res.append(activity)

            # print(activity)

        # else:
        #     # print(f"Error {new_response.status_code}: {new_response.text}")
            


    # else:
    #     print(f"Error {response.status_code}: {response.text}")

    return final_res

def list_restaurant_names(activities):
    activity_string = ""
    i=0
    for activity in activities:
        activity_string += f"{activity.name}: {activity.category}\n"
        i+=1
    return activity_string

def filter_restaurants(term, location, preferences, num_days):
    activities = get_business_information(term, location)
    activity_string = list_restaurant_names(activities)
    filtered_restaurants = filter_restaurants_ai(activity_string, preferences, num_days)
    final_activities = []
    for activity in activities:
        if activity.name in filtered_restaurants:
            final_activities.append(activity)
    
    return final_activities
# function to be used to verify restaurants
# returns list of activity objects

# activities = filter_restaurants("restaurants", "NYC", "Italian, Japanese, Mediterranean", 1)
# for activity in activities:
#     print(activity.name)

# restaurants = parse_restaurants()
# get_business_information(restaurants[8], "Las Vegas")
# verified_res = verify_restaurants(restaurants)
# for res in verified_res:
#     print(res)
#     print("*"*40)


# term = "restaurants"
# location = "3799 S Las Vegas Blvd, Las Vegas, NV 89109"
# info = get_business_information(term, location)
# for i in info:
#     print(i, '*'*20, '\n')
