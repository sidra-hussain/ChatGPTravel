import GoogleMaps
import DataStructures
from datetime import datetime
import FastestItinerary as ft

def dummy_data():

    # Create some dummy data for testing
        activities = [
               
               DataStructures.Activity(
                name="White House",
                address="1600 Pennsylvania Avenue NW, Washington, DC 20500",
                latitude=38.898819,
                longitude=-77.036690,
                phonenumber="555-1234",
                cost=10.0,
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
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),
                DataStructures.Activity(
                name="Bus Boys and Poets",
                address="450 K St NW, Washington, DC 20001",
                latitude=38.902088,
                longitude=-77.018028,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                }, 
                isBreakfast = False,
                isLunch = False,
                isDinner = True,
                rating = 3
            ),
                DataStructures.Activity(
                name="All Day by Kramers",
                address="1517 Connecticut Ave NW, Washington, DC 20036",
                latitude=38.910831,
                longitude=-77.043770,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = True,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="Washington National Cathedral",
                address="3101 Wisconsin Ave NW, Washington, DC 20016",
                latitude=38.929760,
                longitude=-77.069450,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="1789 Restaurant & Bar",
                address="1226 36th St NW, Washington, DC 20007",
                latitude=38.905991,
                longitude=-77.070518,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = True,
                isLunch = True,
                isDinner = False,
                rating = 3
            )
        ]

        return activities

def multi_day_data(): 
    activities = [
               
               DataStructures.Activity(
                name="White House",
                address="1600 Pennsylvania Avenue NW, Washington, DC 20500",
                latitude=38.898819,
                longitude=-77.036690,
                phonenumber="555-1234",
                cost=10.0,
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
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),
                DataStructures.Activity(
                name="Bus Boys and Poets",
                address="450 K St NW, Washington, DC 20001",
                latitude=38.902088,
                longitude=-77.018028,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                }, 
                isBreakfast = False,
                isLunch = False,
                isDinner = True,
                rating = 3
            ),
                DataStructures.Activity(
                name="All Day by Kramers",
                address="1517 Connecticut Ave NW, Washington, DC 20036",
                latitude=38.910831,
                longitude=-77.043770,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = True,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="Washington National Cathedral",
                address="3101 Wisconsin Ave NW, Washington, DC 20016",
                latitude=38.929760,
                longitude=-77.069450,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="1789 Restaurant & Bar",
                address="1226 36th St NW, Washington, DC 20007",
                latitude=38.905991,
                longitude=-77.070518,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = True,
                isLunch = True,
                isDinner = False,
                rating = 3
            ),
            DataStructures.Activity(
                name="White House",
                address="1600 Pennsylvania Avenue NW, Washington, DC 20500",
                latitude=38.898819,
                longitude=-77.036690,
                phonenumber="555-1234",
                cost=10.0,
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
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),
                DataStructures.Activity(
                name="Bus Boys and Poets",
                address="450 K St NW, Washington, DC 20001",
                latitude=38.902088,
                longitude=-77.018028,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                }, 
                isBreakfast = False,
                isLunch = False,
                isDinner = True,
                rating = 3
            ),
                DataStructures.Activity(
                name="All Day by Kramers",
                address="1517 Connecticut Ave NW, Washington, DC 20036",
                latitude=38.910831,
                longitude=-77.043770,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = True,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="Washington National Cathedral",
                address="3101 Wisconsin Ave NW, Washington, DC 20016",
                latitude=38.929760,
                longitude=-77.069450,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = False,
                isLunch = False,
                isDinner = False,
                rating = 3
            ),

            DataStructures.Activity(
                name="1789 Restaurant & Bar",
                address="1226 36th St NW, Washington, DC 20007",
                latitude=38.905991,
                longitude=-77.070518,
                phonenumber="555-5678",
                cost=20.0,
                category="Restaurant",
                hours={
                    "Monday": {"open": datetime(2023, 10, 23, 12, 0), "close": datetime(2023, 10, 23, 21, 0)},
                    "Tuesday": {"open": datetime(2023, 10, 24, 11, 0), "close": datetime(2023, 10, 24, 22, 0)},
                    "Wednesday": {"open": datetime(2023, 10, 25, 11, 0), "close": datetime(2023, 10, 25, 22, 0)},
                    "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                    "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                    "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                    "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},
                },
                isBreakfast = True,
                isLunch = True,
                isDinner = False,
                rating = 3
            ),

        ]
    return activities


def main():
    activities = dummy_data()
    planned_days = ft.greedy_fastest_itinerary(activities, "2020 F st NW Washington, DC 20006", 1)
    plan = DataStructures.Itinerary (
         days = planned_days,
         startDate = datetime.now(),
         endDate = datetime.now(),
         hotel = "2020 F st NW Washington, DC 20006"
        )
    
    days = plan.days

    print ("One Day Itinerary")
    for day, day_activities in days.items():
        print(f"Day {day}:")
        print(f"  {plan.hotel}")
        for activity in day_activities:
            print(f"  {activity.name}")
        print(f"  {plan.hotel}")

    activities = multi_day_data()
    planned_days = ft.greedy_fastest_itinerary(activities, "2020 F st NW Washington, DC 20006", 2)
    
    plan = DataStructures.Itinerary (
         days = planned_days,
         startDate = datetime.now(),
         endDate = datetime.now(),
         hotel = "2020 F st NW Washington, DC 20006"
        )
    
    days = plan.days
    print ("Multi Day Itinerary")
    for day, day_activities in days.items():
        print(f"Day {day}:")
        print(f"  {plan.hotel}")
        for activity in day_activities:
            print(f"  {activity.name}")
        print(f"  {plan.hotel}")


if __name__ == "__main__":
    main()