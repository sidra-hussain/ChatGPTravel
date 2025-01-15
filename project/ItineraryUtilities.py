# from project.DataStructures import Day
from ast import List

def simple_itinerary(activities):
    # Initialize the itinerary with an empty list of days
    itinerary = []

    # Sort the activities based on the opening time
    activities.sort(key=lambda activity: activity.hours["Monday"]["open"])

    for activity in activities:
        open_time = activity.hours["Monday"]["open"]
        close_time = activity.hours["Monday"]["close"]
        
        # Find the day corresponding to the open_time
        target_day = open_time.strftime("%A")
        
        # Check if the itinerary already has a day for the target_day
        day_exists = False
        for day in itinerary:
            if day.name == target_day:
                current_day = day
                day_exists = True
                break
        
        # If the day doesn't exist in the itinerary, create a new day
        if not day_exists:
            current_day = Day(None, None, None, [])
            current_day.name = target_day
            itinerary.append(current_day)

        # Add the activity to the current day
        current_day.activities.append(activity)

    return itinerary




    #return 3


#Checks that the passed activity is open at the specified time
def is_open(activity, time):
    day_activities = activity.hours.__getattribute__(time.strftime("%A"))

    for activity_time in day_activities:
        open_time = activity_time.get('open')
        close_time = activity_time.get('close')

        if open_time <= time < close_time:
            return True

    return False