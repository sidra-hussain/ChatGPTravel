#from project import DataStructures
import random
from datetime import datetime
from ItineraryUtilities import is_open
import DataStructures
from typing import List
from typing import Dict

def dummy_data_cost():
    activities = []

    for i in range(0, 100):
        name = "Activity " + str(i)

        # Randomly determine which meals the Restaurant serves, if any
        isBreakfast=random.choice([True, False])
        isLunch=random.choice([True, False])
        isDinner=random.choice([True, False])
        if(isBreakfast or isLunch or isDinner):
            name = "Restaurant " + str(i)

        # Randomly determine cost
        cost = round(random.uniform(5, 100),2)

        # Use a formula that correlates cost to rating with some randomness
        base_rating = cost / 20 + 1
        randomness = random.uniform(-0.5, 3) 

        # Calculate the final rating with randomness, constrained to be between 0 and 5
        rating = round(min(5.0, max(0.0, base_rating + randomness)), 2)
        activities.append(DataStructures.Activity(
                name=name,
                address="123 Main St",
                latitude=40.7128,
                longitude=-74.0060,
                phonenumber="555-1234",
                cost=cost,
                rating = rating,
                category="Museum",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 9, 0), "close": datetime(2023, 10, 23, 17, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 10, 0), "close": datetime(2023, 10, 24, 18, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 8, 0), "close": datetime(2023, 10, 25, 16, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 10, 0), "close": datetime(2023, 10, 26, 18, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 9, 0), "close": datetime(2023, 10, 27, 17, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 10, 0), "close": datetime(2023, 10, 28, 18, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 11, 0), "close": datetime(2023, 10, 29, 19, 0)},
                },
                isBreakfast=isBreakfast,
                isLunch=isLunch,
                isDinner=isDinner
            ))

    # Sort activities by cost
    sorted_activities = sorted(activities, key=lambda x: x.cost)

    # Separate activities based on properties
    breakfast_activities = [activity for activity in sorted_activities if activity.isBreakfast]
    lunch_activities = [activity for activity in sorted_activities if activity.isLunch]
    dinner_activities = [activity for activity in sorted_activities if activity.isDinner]
    nonmeal_activities = [activity for activity in sorted_activities if not activity.isBreakfast and not activity.isLunch and not activity.isDinner]

    # Print the 3 cheapest activities for each property
    # print("Top 3 Cheapest Breakfast Activities:")
    # for i in range(3):
    #     print(f"{breakfast_activities[i].name}: {breakfast_activities[i].cost}")

    # print("\nTop 3 Cheapest Lunch Activities:")
    # for i in range(3):
    #     print(f"{lunch_activities[i].name}: {lunch_activities[i].cost}")

    # print("\nTop 3 Cheapest Dinner Activities:")
    # for i in range(3):
    #     print(f"{dinner_activities[i].name}: {dinner_activities[i].cost}")

    # print("\nTop 3 Cheapest Non-Meal Activities:")
    # for i in range(3):
    #     print(f"{nonmeal_activities[i].name}: {nonmeal_activities[i].cost}")

    return activities    

#user input for cheapest itinerary 
def cheapest_itinerary(activities, num_days):
    # Add activities
    cheap_activities = [activity for activity in activities]
    
    # Initialize the itinerary with an empty dictionary of days
    days_dict: Dict[int, List[DataStructures.Activity]] = {i: [] for i in range(num_days)}


    # Sort the cheapest activities based on cost
    cheap_activities.sort(key=lambda activity: activity.cost)
    
    size = len(cheap_activities)
    visted = [False]*size
    totalCostList = [0] * num_days
    averageRatingList = [0] * num_days


    for i in range(num_days):
        # totalCost = 0
        # totalRating=0
        #Find breakfast
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                # totalCost += activity.cost
                # totalRating += activity.rating
                break
            
        #Find nonmeal one
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                # totalCost += activity.cost
                # totalRating += activity.rating
                break

        #Find Lunch 
        for index, activity in enumerate(cheap_activities):
            if activity.isLunch == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                # totalCost += activity.cost
                # totalRating += activity.rating
                break

        #Find nonmeal two
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                # totalCost += activity.cost
                # totalRating += activity.rating
                break

        #Find Dinner
        for index, activity in enumerate(cheap_activities):
            if activity.isDinner == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                # totalCost += activity.cost
                # totalRating += activity.rating
                break

        # totalCostList[i] = totalCost
        # averageRatingList[i] = totalRating/5

    return days_dict

#user input for cost-effective itinerary 
def cost_effective_itinerary(activities, num_days):
    # Add activities
    cheap_activities = [activity for activity in activities]
    
    # Initialize the itinerary with an empty dictionary of days
    days_dict: Dict[int, List[DataStructures.Activity]] = {i: [] for i in range(num_days)}


    # Sort the activities based on best rating/cost ratio
    cheap_activities.sort(key=lambda activity: (activity.rating / activity.cost), reverse=True)
    
    size = len(cheap_activities)
    visted = [False]*size
    totalCostList = [0] * num_days
    averageRatingList = [0] * num_days

    for i in range(num_days):
        totalCost = 0
        totalRating = 0
        #Find breakfast
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break
            
        #Find nonmeal one
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find Lunch 
        for index, activity in enumerate(cheap_activities):
            if activity.isLunch == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find nonmeal two
        for index, activity in enumerate(cheap_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find Dinner
        for index, activity in enumerate(cheap_activities):
            if activity.isDinner == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        totalCostList[i] = totalCost
        averageRatingList[i] = totalRating/5

    return days_dict, totalCostList, averageRatingList

def best_rated_itinerary(activities, num_days):
    # Add activities
    high_rated_activities = [activity for activity in activities]
    
    # Initialize the itinerary with an empty dictionary of days
    days_dict: Dict[int, List[DataStructures.Activity]] = {i: [] for i in range(num_days)}


    # Sort the activities based on rating
    high_rated_activities.sort(key=lambda activity: activity.rating, reverse=True)
    
    size = len(high_rated_activities)
    visted = [False]*size
    totalCostList = [0] * num_days
    averageRatingList = [0] * num_days


    for i in range(num_days):
        totalCost = 0
        totalRating=0
        #Find breakfast
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break
            
        #Find nonmeal one
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find Lunch 
        for index, activity in enumerate(high_rated_activities):
            if activity.isLunch == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find nonmeal two
        for index, activity in enumerate(high_rated_activities):
            if activity.isBreakfast == False and activity.isLunch == False and activity.isDinner == False and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        #Find Dinner
        for index, activity in enumerate(high_rated_activities):
            if activity.isDinner == True and visted[index] == False:
                days_dict[i].append(activity)
                visted[index] = True
                totalCost += activity.cost
                totalRating += activity.rating
                break

        totalCostList[i] = totalCost
        averageRatingList[i] = totalRating/5

    return days_dict, totalCostList, averageRatingList

def budgeted_itinerary(activities, capacity):
    cardinality =5
    n = len(activities)
    dp = {}

    for k in range(cardinality + 1):
        for i in range(n + 1):
            for w in range(int(capacity * 100) + 1):  # Multiply by 100 to handle decimals
                if i == 0 or k == 0 or w == 0:
                    dp[i, k, w] = 0
                elif activities[i - 1].cost * 100 > w:
                    dp[i, k, w] = dp[i - 1, k, w]
                else:
                    # Check the type of activity (isBreakfast, isLunch, isDinner, or nonmeal)
                    current_activity = activities[i - 1]
                    if current_activity.isBreakfast and k == 1:
                        include_activity = dp[i - 1, k-1, w - int(current_activity.cost * 100)] + current_activity.rating
                    elif current_activity.isLunch and k == 3:
                        include_activity = dp[i - 1, k-1, w - int(current_activity.cost * 100)] + current_activity.rating
                    elif current_activity.isDinner and k == 5:
                        include_activity = dp[i - 1, k-1, w - int(current_activity.cost * 100)] + current_activity.rating
                    elif (k==2 or k==4) and not any([current_activity.isBreakfast, current_activity.isLunch, current_activity.isDinner]):
                        include_activity = dp[i - 1, k-1, w - int(current_activity.cost * 100)] + current_activity.rating
                    else:
                        include_activity = 0

                    exclude_activity = dp[i - 1, k, w]
                    dp[i, k, w] = max(exclude_activity, include_activity)
                    # if(k == 5 and dp[i, k, w] == exclude_activity and current_activity==bb):
                    #     print("Best Dinner Skipped")
                    #     print(exclude_activity)
                    #     print(include_activity)

    # Iterate through the table to add optimal activities 
    selected_activities = []
    i, k, w = n, cardinality, int(capacity * 100)
    while i > 0 and k > 0 and w > 0:
        if dp[i, k, w] != dp[i - 1, k, w]:
            selected_activities.append(activities[i - 1])
            i -= 1
            k -= 1
            w -= int(activities[i].cost * 100)
        else:
            i -= 1
    
    selected_activities.reverse()

    return selected_activities

def print_itinerary(itinerary, totalCost, averageRating, num_days):
    finalCost =0
    finalRating=0
    for day, activities in itinerary.items():
        print(f"\nDay {day + 1}:")
        for activity in activities:
            print(f"  {activity.name} - Cost: {activity.cost}  - Rating: {activity.rating}")
        print("Total Cost: " + str(round(totalCost[day], 2)))
        print("Average Rating: " + str(round(averageRating[day], 2)))
        finalCost+=round(totalCost[day], 2)
        finalRating+=round(averageRating[day], 2)
    finalRating=finalRating/num_days
    if(num_days>1):
        print("\nItinerary Cost: " + str(round(finalCost, 2)))
        print("Itinerary Rating: " + str(round(finalRating, 2)))
        
# activities = dummy_data_cost()

# num_days = 1

# # Print Best Rated Itinerary
# itinerary, totalCost, averageRating = best_rated_itinerary(activities, num_days)
# print("\nBest Rated Itinerary:")
# print_itinerary(itinerary, totalCost, averageRating, num_days)

# # Print Cheapest Itinerary
# itinerary, totalCost, averageRating = cheapest_itinerary(activities, num_days)
# print("\nCheapest Itinerary:")
# print_itinerary(itinerary, totalCost, averageRating, num_days)

# # Print Cost Effective Itinerary
# itinerary, totalCost, averageRating = cost_effective_itinerary(activities, num_days)
# print("\nCost Effective Itinerary:")
# print_itinerary(itinerary, totalCost, averageRating, num_days)
# prevAverageRating = averageRating
# itinerary = budgeted_itinerary(activities, 100)

# # print("\nBudgeted Itinerary:")
# # totalCost=0
# # averageRating=0
# # for activity in itinerary:
# #     print(f"  {activity.name} - Cost: {activity.cost}  - Rating: {activity.rating} - Meal: {activity.isBreakfast} {activity.isLunch} {activity.isDinner}")
# #     totalCost+=activity.cost
# #     averageRating+=activity.rating
# # averageRating=averageRating/len(itinerary)
# # print("Total Cost: " + str(round(totalCost, 2)))
# # print("Average Rating: " + str(round(averageRating, 2)))

# while(1):
#     activities = dummy_data_cost()

#     # dinner =DataStructures.Activity(
#     #                 name="Mega Dinner",
#     #                 address="123 Main St",
#     #                 latitude=40.7128,
#     #                 longitude=-74.0060,
#     #                 phonenumber="555-1234",
#     #                 cost=40.0,
#     #                 rating = 5.0,
#     #                 category="Museum",
#     #                 hours={
#     #                     "Monday": {"open": datetime(2023, 10, 23, 9, 0), "close": datetime(2023, 10, 23, 17, 0)},
#     #                     "Tuesday": {"open": datetime(2023, 10, 24, 10, 0), "close": datetime(2023, 10, 24, 18, 0)},
#     #                     "Wednesday": {"open": datetime(2023, 10, 25, 8, 0), "close": datetime(2023, 10, 25, 16, 0)},
#     #                     "Thursday": {"open": datetime(2023, 10, 26, 10, 0), "close": datetime(2023, 10, 26, 18, 0)},
#     #                     "Friday": {"open": datetime(2023, 10, 27, 9, 0), "close": datetime(2023, 10, 27, 17, 0)},
#     #                     "Saturday": {"open": datetime(2023, 10, 28, 10, 0), "close": datetime(2023, 10, 28, 18, 0)},
#     #                     "Sunday": {"open": datetime(2023, 10, 29, 11, 0), "close": datetime(2023, 10, 29, 19, 0)},
#     #                 },
#     #                 isBreakfast=False,
#     #                 isLunch=False,
#     #                 isDinner=True
#     #             )

#     # activities.append(dinner)
#     itinerary = budgeted_itinerary(activities, 100)
#     totalCost=0
#     averageRating=0
#     for activity in itinerary:
#         averageRating+=activity.rating
#     averageRating=averageRating/len(itinerary)
#     if (sum(prevAverageRating)) > averageRating:
#         break

# averageRating=0
# for activity in itinerary:
#     print(f"  {activity.name} - Cost: {activity.cost}  - Rating: {activity.rating} - Meal: {activity.isBreakfast} {activity.isLunch} {activity.isDinner}")
#     totalCost+=activity.cost
#     averageRating+=activity.rating
# averageRating=averageRating/len(itinerary)
# print("Total Cost: " + str(round(totalCost, 2)))
# print("Average Rating: " + str(round(averageRating, 2)))

