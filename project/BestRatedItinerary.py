#from project import DataStructures
from datetime import datetime
from ItineraryUtilities import is_open
import DataStructures
from typing import List
from typing import Dict

#user input for ratings 
def best_rated_itinerary(activities, num_days):
    # Filter activities with a rating of 4 or 5
    high_rated_activities = [activity for activity in activities if 1 <= activity.rating <= 5]
    
    # Initialize the itinerary with an empty dictionary of days
    days_dict: Dict[int, List[DataStructures.Activity]] = {i: [] for i in range(num_days)}


    # Sort the high-rated activities based on ratings in descending order
    high_rated_activities.sort(key=lambda activity: activity.rating, reverse=True)
    
    size = len(high_rated_activities)
    visted = [False]*size

    for i in range(num_days):
        #Find breakfast
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                break
            
        #Find nonmeal one
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                break

        #Find Lunch 
        for index, activity in enumerate(high_rated_activities):
            if activity.isLunch == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                break

        #Find nonmeal two
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                break

        #Find Dinner
        for index, activity in enumerate(high_rated_activities):
            if activity.isDinner == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                break

    return days_dict
