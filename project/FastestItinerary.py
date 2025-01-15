# from project import DataStructures
# from project import GoogleMaps as map

import DataStructures
import GoogleMaps as map

import sys
from typing import Dict
from typing import List
#Generates an itenrary with the least travel time
#currently assumes that there is 1 day
#Perhaps do this with an adjacency vector???

def greedy_fastest_itinerary(activities, hotel, days):

    INT_MAX = 2147483647
    adjMatrix = adjacency_matrix(activities, hotel)

    size = len(adjMatrix)
    visited = [False] * size
    route = []

    days_dict: Dict[int, List[DataStructures.Activity]] = {i: [] for i in range(days)}

    for i in range(days):
        current_city = 0  # Start with the hotel at index 0 for every day
        visited[current_city] = True

        # Function to find the next unvisited city of a specific meal type
        def find_next_city(is_breakfast, is_lunch, is_dinner):
            min_cost = INT_MAX
            next_city = -1

            for j in range(size):
                if not visited[j] and adjMatrix[current_city][j] < min_cost:
                    if (is_breakfast and activities[j].isBreakfast) or \
                    (is_lunch and activities[j].isLunch) or \
                    (is_dinner and activities[j].isDinner):
                        min_cost = adjMatrix[current_city][j]
                        next_city = j

            return next_city
        
        # Function to find the next unvisited city of a non-meal type
        def find_next_nonmeal():
            min_cost = INT_MAX
            next_city = -1
            
            for j in range(size):
                if not visited[j] and not activities[j].isBreakfast and not activities[j].isLunch and not activities[j].isDinner and adjMatrix[current_city][j] < min_cost:
                    min_cost = adjMatrix[current_city][j]
                    next_city = j
            
            return next_city   

        # Visit breakfast first
        breakfast_city = find_next_city(True, False, False)
        if breakfast_city != -1:
            days_dict[i].append(activities[breakfast_city])
            visited[breakfast_city] = True
            current_city = breakfast_city

        # Visit a non-meal activity
        nonmeal_city = find_next_nonmeal()
        if nonmeal_city!= -1:
            days_dict[i].append(activities[nonmeal_city])
            visited[nonmeal_city] = True
            current_city = nonmeal_city

        # Visit lunch
        lunch_city = find_next_city(False, True, False)
        if lunch_city != -1:
            days_dict[i].append(activities[lunch_city])
            visited[lunch_city] = True
            current_city = lunch_city

        # Visit a non-meal activity
        nonmeal_city = find_next_nonmeal()
        if nonmeal_city!= -1:
            days_dict[i].append(activities[nonmeal_city])
            visited[nonmeal_city] = True
            current_city = nonmeal_city

        # Visit dinner
        dinner_city = find_next_city(False, False, True)
        if dinner_city != -1:
            days_dict[i].append(activities[dinner_city])
            visited[dinner_city] = True
            current_city = dinner_city

        activities_route = [activities[city] for city in route]

    return days_dict
    
#Generates an adjacency matrix of the activities and the hotel
#This function is a utiltiy function for the fastest itinerary function's 
#algorithm
def adjacency_matrix (activites, hotel):
    #Set up the adjacency matrix
    adjMatrix = []
    #Ensures the hotel is the start and end location
    activites.insert(0, hotel)
    size = len(activites)
    for i in range(size):
        adjMatrix.append([0 for i in range(size)])
    
    #Fill the adjacency matrix
    for i in range(size):
        for j in range(i, size):
            
            #To prevent the distance of 0 messing with the itinerary 
            if i==j:
                adjMatrix[i][j] = sys.float_info.max
            
            #Not the same activity
            time = map.travel_time(activites[i], activites[j], "driving")
            adjMatrix[i][j] = int(time)
            adjMatrix[j][i] = int(time)
    
    #Result 
    return adjMatrix