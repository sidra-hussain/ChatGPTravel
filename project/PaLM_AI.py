import project.credentials as credentials
import google.generativeai as palm
import re

API_KEY = credentials.palm_key
palm.configure(api_key=API_KEY)
model_id = 'models/text-bison-001'

#We might want to break down get activities 
#to be more specific, but I think this depends on the
#quality of the results we are getting back to be honest

# We can also send the outputs to JSON files if we decide
# that's what we want. It's an easy add-on
def get_activities (activities_query):
  completion = palm.generate_text(
      model = model_id,
      prompt = activities_query,
      temperature = 0.9,
      candidate_count=1
  )
  output = completion.result
  output = re.sub("```json", "", output)
  output = re.sub("```", "", output)
  return output

def get_restaurants (restaurants_query):
  completion = palm.generate_text(
      model = model_id,
      prompt = restaurants_query,
      temperature = 0.9,
      candidate_count=1
  )
  output = completion.result
  output = re.sub("```json", "", output)
  output = re.sub("```", "", output)
  return output

# prompts can be easily changed to ask for different information, be in a different format, etc.
act_query = '''
Give me a list of activities to do in Las Vegas with a name, category, address, and phone number. 
do not include hotels or restaurants.
give the phone number in the form ###-###-####.
create a valid json object in the format 
{
  "Activities":[
    {
      "name":"name",
      "category":"category",
      "address":"address",
      "phonenumber":"phonenumber"
    }
  ]
}.
do not return any non JSON text or numbering
'''
res_query = '''
Give me a list of 10 restaurants to do in Las Vegas with a name, category, address, and phone number. 
give the category based on whether it offers breakfast, lunch, or dinner.
give the phone number in the form ###-###-####.
create a valid json object in the format 
{
  "Restaurants":[
    {
      "name":"name",
      "category":"category",
      "address":"address",
      "phonenumber":"phonenumber"
    }
  ]
}.
do not return any non JSON text or numbering
'''



# Sends outputs to JSON files to be read by parse file
def activities_to_json():
  output1 = get_activities(act_query)
  f = open("Activities.json", "w")
  f.write(output1)
  f.close()

def restaurants_to_json():
  output2 = get_restaurants(res_query)
  f = open("Restaurants.json", "w")
  f.write(output2)
  f.close()

activities_to_json()
restaurants_to_json()