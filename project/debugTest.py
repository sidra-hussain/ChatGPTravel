def main():
    from datetime import time
    from DataStructures import Hours, Activity, Category
    from BestRatedItinerary import best_rated_itinerary

    # Sample activities
    activity1 = Activity(
        name="Restaurant A",
        address="123 Main St",
        latitude=40.7128,
        longitude=-74.0060,
        phonenumber="555-1234",
        cost=50.0,
        category=Category(categories=["Food"]),
        hours=Hours(
            Monday=[{"open": time(8, 0), "close": time(10, 0)}],
            Tuesday=[{"open": time(12, 0), "close": time(14, 0)}],
            Wednesday=[{"open": time(18, 0), "close": time(20, 0)}],
            Thursday=[{"open": time(8, 0), "close": time(12, 0)}],
            Friday=[{"open": time(12, 0), "close": time(15, 0)}],
            Saturday=[{"open": time(10, 0), "close": time(14, 0)}],
            Sunday=[{"open": time(18, 0), "close": time(22, 0)}]
        ),
        isBreakfast=True,
        isLunch=False,
        isDinner=False,
        rating=4.8
    )

    activity2 = Activity(
        name="Resturant B",
        address="456 Oak St",
        latitude=40.7308,
        longitude=-74.0360,
        phonenumber="555-5678",
        cost=30.0,
        category=Category(categories=["Cafe"]),
        hours=Hours(
            Monday=[{"open": time(8, 0), "close": time(14, 0)}],
            Tuesday=[{"open": time(10, 0), "close": time(16, 0)}],
            Wednesday=[{"open": time(14, 0), "close": time(18, 0)}],
            Thursday=[{"open": time(9, 0), "close": time(13, 0)}],
            Friday=[{"open": time(11, 0), "close": time(15, 0)}],
            Saturday=[{"open": time(9, 0), "close": time(12, 0)}],
            Sunday=[{"open": time(12, 0), "close": time(16, 0)}]
        ),
        isBreakfast=False,
        isLunch=True,
        isDinner=False,
        rating=4.7
    )

    activity3 = Activity(
        name="Activity A",
        address="123 Main St",
        latitude=40.7128,
        longitude=-74.0060,
        phonenumber="555-1234",
        cost=50.0,
        category=Category(categories=["Food"]),
        hours=Hours(
            Monday=[{"open": time(8, 0), "close": time(10, 0)}],
            Tuesday=[{"open": time(12, 0), "close": time(14, 0)}],
            Wednesday=[{"open": time(18, 0), "close": time(20, 0)}],
            Thursday=[{"open": time(8, 0), "close": time(12, 0)}],
            Friday=[{"open": time(12, 0), "close": time(15, 0)}],
            Saturday=[{"open": time(10, 0), "close": time(14, 0)}],
            Sunday=[{"open": time(18, 0), "close": time(22, 0)}]
        ),
        isBreakfast=False,
        isLunch=False,
        isDinner=False,
        rating=4.5
    )

    # List of activities
    activities_list = [activity1, activity2, activity3]

    num_days = 7

    # Test the function with 7 days
    result = best_rated_itinerary(activities_list,num_days)

    # Display the result
    for day, activities in result.items():
        print(f"\nDay {day} Itinerary:")
        for activity in activities:
            print(f"{activity.name} - Rating: {activity.rating}")


if __name__ == "__main__":
    main()

