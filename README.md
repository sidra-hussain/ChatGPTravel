GW Bachelor of Science in Computer Science Senior Design 2023-2024

Team 404ERROR
# Introduction to chatGPTravel
chatGPTravel bridges the gap between knowing where you want to travel to, but not knowing what to do at your destination once you arrive. Our service creates a travel itinerary for a user-specified location based on a selected optimization metric, such as cost, rating, or time and activity suggestions genrated using chatGPT 
# Overview
The repository consists of general functionality to run the application as well as its supporting functions, data, and api parsing. The implmentation can be found in the project directory. 

## Viewing and Using the Application

Our project is publicly available at: http://3.140.37.87/

It is running on an EC2 Server running ubuntu. If you would like to use the application we reccomend viewing this [guide](https://docs.google.com/document/d/1nw6ikTy9yNSUYZMvGe15j-BICmRgYBejXz2JEV_QxkI/edit)

## Installation Guide
Our application utilizes multiple python libraries from Python 3.11.8. Therefore, please make sure you are running the correct version of python.

To install libraries associated with our application run: 
```
pip3 install -r requirements.txt
```

# API Keys 

Our application heavily relies on APIs to operate. Many of the keys we use have usage limits or are paid keys. Therefore, users running the application locally need to create their own keys to run the application locally and store them in a credentials.py file that contains the types of keys listed below with the specific naming convention: 

```python
yelp_key0 = "{Your yelp fusion API key}"
.
.
.
yelp_key6 = "{Your yelp fusion API backup key}"
foursquare_key0 = "{Your foursquare api key}"
amadeus_key0 = "{Your amedeaus api key}"
amadeus_secret0 = "{Your amedeaus api key's associated secret key}"
maps_key0="{Your google maps api key}"
geo_api_key="{Your geocoder api key}"
openai_key = "{Your open ai api key}"
```

## Running the Application

Run the project locally by navigating into the project folder and entering the below command into your terminal:

```
python3 -m flask run
```

# Branches
- main
  - Central branch with integrated code used for running the project
- fullstack-dev
   - Stable development enviornment used for Spring 2024, majority of the code was merged and confirmed to work on this branch before being merged into the main branch
- project-website
  - To be used for set-up/maintenance of the website for our project
 
  
