from typing import List
from typing import Dict
from dataclasses import dataclass
from datetime import datetime, time

# An itenerary is a collection of days 
# Holds the start and end day of a trip
# The project assumes the hotel is the same for the entire trip, therefore stored at itenrary level


#Hours of operation is important for scheduling purposes
@dataclass 
class Hours:
    Monday: List[Dict["open": time, "close": time]]
    Tuesday: List[Dict["open": time, "close": time]]
    Wednesday: List[Dict["open": time, "close": time]]
    Thursday: List[Dict["open": time, "close": time]]
    Friday: List[Dict["open": time, "close": time]]
    Saturday: List[Dict["open": time, "close": time]]
    Sunday: List[Dict["open": time, "close": time]]



@dataclass
class Itinerary:
    days : Dict[int, List["Activity"]]
    startDate : datetime
    endDate : datetime
    hotel : str

#Each activity has this minimum amount of information associated with it
@dataclass
class Activity:
    name : str
    address : str 
    latitude : float
    longitude : float 
    phonenumber : str
    cost : float 
    cost_estimate : str
    category : "Category"
    hours : Hours
    isBreakfast : bool
    isLunch : bool 
    isDinner : bool
    rating : float
    website : str

#The yelp API returns the category of the activity queried, there are many different types of activities 
#The assumption will be that there are infinte activities, if the activity triggers a special child class
#It will be set accordingly, so there needs to be logic added to this function to do that correctly
class Category:
    def __init__(self, categories):
        self.categories = categories

#Hours of operation is important for scheduling purposes