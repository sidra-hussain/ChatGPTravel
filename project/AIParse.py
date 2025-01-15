import json

# Activities
def parse_activities():
    with open('Activities.json', 'r') as parse_file:
        data = json.load(parse_file)

    cats1 = data['Activities']
    acts = []
    for cat in cats1:
        act_items = []
        act_items.append(cat.get('name'))
        act_items.append(cat.get('latitude'))
        act_items.append(cat.get('longitude'))
        acts.append(act_items)

    return acts
#------------------------------------------------------------------------------------#

# Restaurants
def parse_restaurants():
    with open('Restaurants.json', 'r') as parse_file:
        data = json.load(parse_file)

    cats2 = data['Restaurants']
    rests = []
    for cat in cats2:
        rests.append(cat.get('name'))

    return rests

# parse_activities()
# parse_restaurants()
