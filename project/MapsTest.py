import GoogleMaps
import DataStructures as DataStructures
from datetime import datetime

def dummy_data():

    # Create some dummy data for testing
        activities = [
               
               DataStructures.Activity(
                name="White House",
                address="1600 Pennsylvania Avenue NW, Washington, DC 20500",
                latitude=40.7128,
                longitude=-74.0060,
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
                latitude=40.7129,
                longitude=-74.0061,
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
                name="GWU",
                address="2121 I St NW, Washington, DC 20052",
                latitude=40.7129,
                longitude=-74.0061,
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
            )
        ]

        return activities


def main():
    activities = dummy_data()
    # time = GoogleMaps.travel_time("2020 F st NW Washington DC, 20006", "53 Wensley Drive Great Neck NY, 11020", "driving")
    # total_time = GoogleMaps.total_itinerary_travel_time(activities, "2020 F st NW Washington, DC 20006", "driving")
    # print ("The travel time is: " + str(time))
    # print ("Itinerary Travel time: " + str(total_time))

if __name__ == "__main__":
    main()