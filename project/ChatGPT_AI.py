import openai
import credentials as credentials

OPENAI_API_KEY = credentials.openai_key

openai.api_key = OPENAI_API_KEY

def filter_activities_ai(activities, preferences, num_days):
    # if (isRestaurant): 
    #     num_activities = num_days*3
    #     include_restaurants = ""
    # else: 
    #     num_activities = num_days*2
    #     include_restaurants = "Do not include restaurants or grocery stores."
    
    prompt = f"From the following list, retrieve at least {num_days*4} locations that would be good for a person who enjoys: {preferences}.\n {activities}\n Do not include restaurants or coffee shops. Return only the names of the selected locations, separated by lines."
    # print(prompt)
    response = openai.completions.create(
        # engine="text-davinci-003",
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.8
    )
    return response.choices[0].text.strip()

def filter_restaurants_ai(activities, preferences, num_days):
    # if (isRestaurant): 
    #     num_activities = num_days*3
    #     include_restaurants = ""
    # else: 
    #     num_activities = num_days*2
    #     include_restaurants = "Do not include restaurants or grocery stores."
    
    prompt = f"From the following list of restaurants and their corresponding categories, retrieve at least {num_days*6}  of the locations that would be good for a person who enjoys: {preferences}.\n {activities}\n. Return only the names of the selected locations, separated by lines."
    # print(prompt)
    response = openai.completions.create(
        # engine="text-davinci-003",
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.8
    )
    return response.choices[0].text.strip()
