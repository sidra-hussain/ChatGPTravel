from DataStructures import Activity, Category, Hours, Itinerary
from datetime import date, datetime, timedelta
from ItineraryUtilities import simple_itinerary
from ChatGPT_AI import ai_activities, ai_restaurants
from Yelp import verify_restaurants, num_restaurants
from Foursquare import verify_activities, num_activities
from AIParse import parse_restaurants, parse_activities
from Amadeus import get_activity_cost
import FastestItinerary as ft
import math
import BestRatedItinerary as br
import CheapestItinerary as cheapest
import GoogleMaps as gm

def get_date(start_end):
    while True:
        user_input = input(f"On what date does your trip {start_end}? Please enter in mm/dd/yyyy format: ")

        # error check that date is valid
        try:
            # convert string to date type
            user_datetime = datetime.strptime(user_input, "%m/%d/%Y")
            user_date = user_datetime.date()
            break
        except:
            print("Error: Please ensure you input a valid date in mm/dd/yyyy format.")

    return user_date

def get_input():
    # input destination
    # assumes user inputs valid city
    dest = input("Enter the city that you are traveling to: ")

    hotel = input("Enter the address of the hotel at which you are staying: ")

    today = date.today()

    # call function to get start date
    start_date = get_date("begin")
    while True:
        # check that date is in the future
        if (start_date < today):
            print("Error: Please input a valid date in the future.")
            start_date = get_date("begin")
        else:
            break
    # while True:
    #     # check that this is the correct date for the user
    #     start_correct = input(f"Is this correct date? {start_date} (Y/N): ")
    #     if (start_correct == "N"):
    #         start_date = get_date("begin")
    #     elif (start_correct == "Y"):
    #         break
    #     else:
    #         print("Please enter Y or N.")


    # call function to get end date
    end_date = get_date("end")
    while True:
        # check that date is after the start date
        if (end_date <= start_date):
            print("Error: Please enter an end date after your start date.")
            end_date = get_date("end")
        else:
            break
    # while True:
    #     # check that this is the correct date for the user
    #     end_correct = input(f"Is this correct date? {end_date} (Y/N): ")
    #     if (end_correct == "N"):
    #         end_date = get_date("end")
    #     elif (end_correct == "Y"):
    #         break
    #     else:
    #         print("Please enter Y or N.")

    
    while True:
        # prompt for optimization choice
        opt = input("Choose an optimization metric: Transit Time, Cost, Ratings: ")
        if (opt.lower() != "transit time" and opt.lower() != "cost" and opt.lower() != "ratings"):
            print("Error: Please choose from one of the listed optimization metrics. ")
        else:
            break


    # print("Destination:", dest)
    # print("Hotel:", hotel)
    # print("Start date:", start_date)
    # print("End date:", end_date)
    # print("Optimizer:", opt.title())

    input_items = {
        "destination": dest,
        "hotel": hotel,
        "start_date": start_date,
        "end_date": end_date,
        "optimizer": opt.lower()
    }

    return input_items


def main():

    # get input from user
    input = get_input()
    num_days = (input["end_date"] - input["start_date"]).days
    dest = input["destination"]
    hotel = input["hotel"]

    num_res = int(math.ceil(num_days * 1.5))
    num_act = num_days * 3

    print("Generating restaurants and activities.")

    # initial call to ai to return restaurants and activities
    res_prompt = f"Give me a list of {num_res} breakfast restaurants, {num_res} lunch restaurants, and {num_res} dinner restaurants to eat at in {dest} with a name, category, latitude, longitude, and address."
    ai_restaurants(res_prompt)
    act_prompt = f"Give me a list of {num_act} activities to do in {dest} with a name, category, latitude, longitude, and address."
    ai_activities(act_prompt)

    # verify with yelp/foursquare, check for ai errors in json
    while True:
        try:
            restaurants = parse_restaurants()
            break
        except:
            ai_restaurants(res_prompt)
    verified_res = verify_restaurants(restaurants, dest)
    while True:
        try:
            activities = parse_activities()
            break
        except:
            ai_activities(act_prompt)
    verified_act = verify_activities(activities)

    # get final list of restaurants and activities with appropriate amount of each meal
    final_res = num_restaurants(num_res, verified_res, dest)
    final_act = num_activities(num_act, verified_act, dest)
    for res in final_res:
        get_activity_cost(res)
    for act in final_act:
        get_activity_cost(act)

    # concatenated list of activities and restaurants to be passed into optimization algorithms
    final_res_act = final_res + final_act

    # for act in final_res_act:
    #     print(act)
    #     print("*"*40)

    print("Building your itinerary.")

    # call specific optimization algorithms based on user preference
    opt = input["optimizer"]
    if (opt == "transit time"):
        # send to sidra
        print("Optimizing on Transit Time.")
        planned_days = ft.greedy_fastest_itinerary(final_res_act, hotel, num_days)
        
        plan = Itinerary (
         days = planned_days,
         startDate = datetime.now(),
         endDate = datetime.now(),
         hotel = hotel
        )
    
        days = plan.days

        for day, day_activities in days.items():
            count = 0
            print(f"Day {day+1}:")
            print(f"  Hotel: {plan.hotel}")
            print(f"    Time to next location: {gm.travel_time(plan.hotel, day_activities[count].address, 'driving')} minutes")
            for activity in day_activities:
                print(f"  {activity.name}")
                if (count + 1 < len(day_activities)):
                    print(f"    Time to next location: {gm.travel_time(day_activities[count].address, day_activities[count+1].address, 'driving')} minutes")
                else:
                    print(f"    Time to next location: {gm.travel_time(day_activities[count].address, plan.hotel, 'driving')} minutes")
                count += 1
            print(f"  Hotel: {plan.hotel}")
    
    elif (opt == "cost"):
        # send to evan
        print("Optimizing on cost.")
        planned_days = cheapest.cheapest_itinerary(final_res_act, num_days)
        
        plan = Itinerary (
         days = planned_days,
         startDate = datetime.now(),
         endDate = datetime.now(),
         hotel = hotel
        )
    
        days = plan.days

        for day, day_activities in days.items():
            print(f"Day {day+1}:")
            print(f"  Hotel: {plan.hotel}")
            for activity in day_activities:
                print(f"  {activity.name}: {activity.cost}")
            print(f"  Hotel: {plan.hotel}")
        # print("2")
    elif (opt == "ratings"):
        # send to sarah
        print("Optimizing on ratings.")
        planned_days = br.best_rated_itinerary(final_res_act, num_days)
        
        plan = Itinerary (
         days = planned_days,
         startDate = datetime.now(),
         endDate = datetime.now(),
         hotel = hotel
        )
    
        days = plan.days

        for day, day_activities in days.items():
            print(f"Day {day+1}:")
            print(f"  Hotel: {plan.hotel}")
            for activity in day_activities:
                print(f"  {activity.name}: {activity.rating}")
            print(f"  Hotel: {plan.hotel}")
        # print("3")



if __name__ == "__main__":
    main()

