import DataStructures as DataStructures
from datetime import datetime

def dummy_days(): 
    activities_dict = {
        0: dummy_data_0(),
        1: dummy_data_1(),
        2: dummy_data_2()
    }
    return activities_dict

def dummy_data_0():
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
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=3
        ),
        DataStructures.Activity(
            name="Lincoln Memorial",
            address="2 Lincoln Memorial Cir NW, Washington, DC 20037",
            latitude=38.8895,
            longitude=-77.0502,
            phonenumber="555-6789",
            cost=0.0,
            category="Landmark",
            hours={
                "Monday": {"open": datetime(2023, 10, 23, 8, 0), "close": datetime(2023, 10, 23, 22, 0)},
                "Tuesday": {"open": datetime(2023, 10, 24, 8, 0), "close": datetime(2023, 10, 24, 22, 0)},
                "Wednesday": {"open": datetime(2023, 10, 25, 8, 0), "close": datetime(2023, 10, 25, 22, 0)},
                "Thursday": {"open": datetime(2023, 10, 26, 8, 0), "close": datetime(2023, 10, 26, 22, 0)},
                "Friday": {"open": datetime(2023, 10, 27, 8, 0), "close": datetime(2023, 10, 27, 22, 0)},
                "Saturday": {"open": datetime(2023, 10, 28, 8, 0), "close": datetime(2023, 10, 28, 22, 0)},
                "Sunday": {"open": datetime(2023, 10, 29, 8, 0), "close": datetime(2023, 10, 29, 22, 0)},
            },
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=4
        ),
        # Add more activities as needed
    ]
    return activities

def dummy_data_1():
    activities = [
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
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=3
        ),
        DataStructures.Activity(
            name="National Gallery of Art",
            address="6th & Constitution Ave NW, Washington, DC 20565",
            latitude=38.8913,
            longitude=-77.0194,
            phonenumber="555-9876",
            cost=0.0,
            category="Museum",
            hours={
                "Monday": {"open": datetime(2023, 10, 23, 10, 0), "close": datetime(2023, 10, 23, 17, 0)},
                "Tuesday": {"open": datetime(2023, 10, 24, 10, 0), "close": datetime(2023, 10, 24, 17, 0)},
                "Wednesday": {"open": datetime(2023, 10, 25, 10, 0), "close": datetime(2023, 10, 25, 17, 0)},
                "Thursday": {"open": datetime(2023, 10, 26, 12, 0), "close": datetime(2023, 10, 26, 21, 0)},
                "Friday": {"open": datetime(2023, 10, 27, 12, 0), "close": datetime(2023, 10, 27, 21, 0)},
                "Saturday": {"open": datetime(2023, 10, 28, 12, 0), "close": datetime(2023, 10, 28, 21, 0)},
                "Sunday": {"open": datetime(2023, 10, 29, 12, 0), "close": datetime(2023, 10, 29, 21, 0)},},
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=3),
    ]
    return activities

def dummy_data_2():
    activities = [
        DataStructures.Activity(
            name="Smithsonian National Air and Space Museum",
            address="600 Independence Ave SW, Washington, DC 20560",
            latitude=38.8886,
            longitude=-77.0199,
            phonenumber="555-2468",
            cost=0.0,
            category="Museum",
            hours={
                "Monday": {"open": datetime(2023, 10, 23, 10, 0), "close": datetime(2023, 10, 23, 17, 30)},
                "Tuesday": {"open": datetime(2023, 10, 24, 10, 0), "close": datetime(2023, 10, 24, 17, 30)},
                "Wednesday": {"open": datetime(2023, 10, 25, 10, 0), "close": datetime(2023, 10, 25, 17, 30)},
                "Thursday": {"open": datetime(2023, 10, 26, 10, 0), "close": datetime(2023, 10, 26, 17, 30)},
                "Friday": {"open": datetime(2023, 10, 27, 10, 0), "close": datetime(2023, 10, 27, 17, 30)},
                "Saturday": {"open": datetime(2023, 10, 28, 10, 0), "close": datetime(2023, 10, 28, 17, 30)},
                "Sunday": {"open": datetime(2023, 10, 29, 10, 0), "close": datetime(2023, 10, 29, 17, 30)},
            },
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=4
        ),
        DataStructures.Activity(
            name="Georgetown Waterfront Park",
            address="3303 Water St NW, Washington, DC 20007",
            latitude=38.9021,
            longitude=-77.0627,
            phonenumber="555-5432",
            cost=0.0,
            category="Park",
            hours={
                "Monday": {"open": datetime(2023, 10, 23, 6, 0), "close": datetime(2023, 10, 23, 22, 0)},
                "Tuesday": {"open": datetime(2023, 10, 24, 6, 0), "close": datetime(2023, 10, 24, 22, 0)},
                "Wednesday": {"open": datetime(2023, 10, 25, 6, 0), "close": datetime(2023, 10, 25, 22, 0)},
                "Thursday": {"open": datetime(2023, 10, 26, 6, 0), "close": datetime(2023, 10, 26, 22, 0)},
                "Friday": {"open": datetime(2023, 10, 27, 6, 0), "close": datetime(2023, 10, 27, 22, 0)},
                "Saturday": {"open": datetime(2023, 10, 28, 6, 0), "close": datetime(2023, 10, 28, 22, 0)},
                "Sunday": {"open": datetime(2023, 10, 29, 6, 0), "close": datetime(2023, 10, 29, 22, 0)},
            },
            isBreakfast=False,
            isLunch=False,
            isDinner=False,
            rating=4
        ),
        # Add more activities as needed
    ]
    return activities
