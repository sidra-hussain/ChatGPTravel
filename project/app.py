from email.mime import base
from typing import Dict, List
import json
import random
import sys
import ast
from DataStructures import Activity, Category, Hours, Itinerary
from datetime import datetime, timedelta, time
import dummydata as data
import re
import MapsTest as test
from Yelp import filter_restaurants
from Foursquare import filter_activities
from AIParse import parse_restaurants, parse_activities
import FastestItinerary as ft
import math
import BestRatedItinerary as br
import GoogleMaps as gm
import CheapestItinerary as cheap
from Geocode import geocode
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session, redirect, render_template, request, flash, url_for
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import logging



app = Flask(__name__)
app.secret_key = 'SaIufXYzLoDNeovs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://error:404Error2024$@database-13.ct044uiusk8o.us-east-2.rds.amazonaws.com:3306/user_schema'  # Change this to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()


class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    itineraries = db.relationship('Itineraries', backref='user', lazy=True)


class Itineraries(db.Model):
    __tablename__ = 'itineraries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Add the ID field
    # itinerary_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Make itinerary_id the primary key
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    hotel = db.Column(db.String)
    user_email = db.Column(db.String(255), db.ForeignKey('user.email'), nullable=False)
    activities = db.relationship('ItineraryActivity', back_populates='itinerary')

class ItineraryActivity(db.Model):
    __tablename__ = 'itinerary_activity'
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'), nullable=False)  # Update foreign key reference
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    phonenumber = db.Column(db.String(20))
    cost = db.Column(db.Float)
    cost_estimate = db.Column(db.String(255))
    category = db.Column(db.String(255))
    hours = db.Column(db.String(255))
    isBreakfast = db.Column(db.Boolean)
    isLunch = db.Column(db.Boolean)
    isDinner = db.Column(db.Boolean)
    rating = db.Column(db.Float)
    website = db.Column(db.String(255))
    itinerary = db.relationship('Itineraries', back_populates='activities', overlaps='itinerary_rel')


itinerary = None
hotel_lat = None
hotel_long = None
opt = None

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/loading", methods=['GET', 'POST'])
def loading():
    if request.method == "POST":
        # gets input from html form
        # need to error check
        dest = request.form.get("inputDest")
        hotel = request.form.get("inputHotel")
        startDate = request.form.get("inputStartDate")
        endDate = request.form.get("inputEndDate")
        activityPrefs = request.form.getlist("inputActivityPrefs")
        foodPrefs = request.form.getlist("inputFoodPrefs")
        opt = request.form.get("optCheck")

        # Store data in session variables
        session['dest'] = dest
        session['hotel'] = hotel
        session['startDate'] = startDate
        session['endDate'] = endDate
        session['activityPrefs'] = activityPrefs
        session['foodPrefs'] = foodPrefs
        session['opt'] = opt
        return render_template("loading.html")
        


@app.route("/itinerary", methods=['GET', 'POST'])
def gen_itin(num=None):
    # gets input from html form
    # need to error check
    
    global itinerary  # Add this line to use the global itinerary variable
    global hotel_lat
    global hotel_long
    global opt

    dest = session.get('dest')
    hotel = session.get('hotel')
    startDate = session.get('startDate')
    start = datetime.strptime(startDate, '%Y-%m-%d')
    endDate = session.get('endDate')
    end = datetime.strptime(endDate, '%Y-%m-%d')
    opt = session.get('opt')
    activityPrefs = session.get('activityPrefs')
    foodPrefs = session.get('foodPrefs')

    itinerary = parse_and_generate(dest, hotel, start, end, opt, foodPrefs, activityPrefs)

    hotel_lat, hotel_long = geocode(hotel)

# Inside your Flask route function
    email = session.get('user_email')

    if email:
        #Create a new itinerary associated with the user's email
        new_itinerary = Itineraries(
            user_email=email,
            start_date=start,
            end_date=end,
            hotel=hotel
        )
        db.session.add(new_itinerary)
        db.session.commit()
        
        itinerary_id = new_itinerary.id
        print(f"Itinerary ID: {itinerary_id}")
        # Save activities to the database
        for day_activities in itinerary.days.values():
            for activity in day_activities:
                activity.address = ''.join(activity.address)
                new_activity = ItineraryActivity(
                    itinerary_id=itinerary_id,
                    name=activity.name,
                    address=activity.address,
                    latitude=activity.latitude,
                    longitude=activity.longitude,
                    phonenumber=activity.phonenumber,
                    cost=activity.cost,
                    cost_estimate=activity.cost_estimate,
                    hours=str(activity.hours),
                    category=activity.category,
                    isBreakfast=activity.isBreakfast,
                    isLunch=activity.isLunch,
                    isDinner=activity.isDinner,
                    rating=activity.rating,
                    website=activity.website
                )
                db.session.add(new_activity)
        db.session.commit()

    if num == None:
        num = 0
    transit_dict = dict.fromkeys(range(len(itinerary.days)), None)
    if opt == 'transit':
        for index in range(len(itinerary.days)):
                transit_dict[index] = gm.total_itinerary_travel_time(itinerary.days[index], itinerary.hotel, "driving")
    
    timestamp_str = datetime.now().strftime('%Y%m%d%H%M%S')
    
    return render_template("itinerary.html", id=0, plan=itinerary.days, startdate=itinerary.startDate, enddate = itinerary.endDate, hotel = itinerary.hotel, timestamp=timestamp_str, num=num, hotel_lat=hotel_lat, hotel_long=hotel_long, opt=opt, transit_dict=transit_dict, travel_time = gm.travel_time)

# @app.route("/error/<num>", methods = ['GET', 'POST'])
# def error(num=0):
#     if num==0:
#         return render_template("error.html", error_message="This is not a valid itinerary.")
#     elif num==1:
#         return render_template("error.html", error_message="You are not authorized to view this itinerary.")
    
@app.route("/itinerary/<id>/<day>", methods=['GET', 'POST'])
def itinerary_display(id=0, day=None):
    global itinerary  # Add this line to use the global itinerary variable
    global hotel_lat
    global hotel_long
    global opt
    
    # print(id)
    if int(id) == 0:
        print("No Itineraries Found")
        saved_itinerary = itinerary
        saved_hotel_lat = hotel_lat
        saved_hotel_long = hotel_long
        saved_opt = opt
    else:
        # print("Found!")
        saved_itinerary=load_itinerary(id)
        if(isinstance(saved_itinerary, str)):
            return saved_itinerary
        saved_hotel_lat, saved_hotel_long = geocode(saved_itinerary.hotel)
        saved_opt = "cost"
    
    if(day==None):
        day=0
    
    day=int(day)

    transit_dict = dict.fromkeys(range(len(saved_itinerary.days)), None)
    if saved_opt == 'transit':
        for index in range(len(saved_itinerary.days)):
                transit_dict[index] = gm.total_itinerary_travel_time(saved_itinerary.days[index], saved_itinerary.hotel, "driving")

    # print(saved_itinerary)
    timestamp_str = datetime.now().strftime('%Y%m%d%H%M%S')
    return render_template("itinerary.html", id=id, plan=saved_itinerary.days, startdate=saved_itinerary.startDate, enddate = saved_itinerary.endDate, hotel = saved_itinerary.hotel, num=day, timestamp=timestamp_str, hotel_lat=saved_hotel_lat, hotel_long=saved_hotel_long, opt=saved_opt, transit_dict=transit_dict, travel_time = gm.travel_time)

def load_itinerary(id):
    user_email = session.get('user_email')
    itinerary = Itineraries.query.filter_by(id=id).first()
    print(itinerary)
    if(itinerary == None):
        # print("No itinerary found") 
        # return redirect("/error/0")
        return render_template("error.html", error_message="This is not a valid itinerary.")
    if(itinerary.user_email != user_email):
        # print("Not Authorized")
        # return redirect("/error/1")
        return render_template("error.html", error_message="You are not authorized to view this itinerary.")
    difference = itinerary.end_date - itinerary.start_date
    num_days = difference.days
    days_dict: Dict[int, List[Activity]] = {i: [] for i in range(num_days)}
    activities = ItineraryActivity.query.filter_by(itinerary_id=itinerary.id).all()
    day=0
    activity_num=0
    for activity in activities:
        # Define a regular expression pattern to match datetime.time() calls
        pattern = r"datetime\.time\((\d+), (\d+)\)|C\wo|s\wd"

        # Find all matches in the string and convert them to time objects
        matches = re.findall(pattern, activity.hours)
        # print(matches)
        time_objects = [datetime.strptime(f"{hour}:{minute}", "%H:%M") if hour and minute else "Closed" for hour, minute in matches]
        # print(activity.hours)

        # Organize time objects into dictionaries according to the desired format
        hours_data = Hours(
            Monday=[{'open': time_objects[0], 'close': time_objects[1]}],
            Tuesday=[{'open': time_objects[2], 'close': time_objects[3]}],
            Wednesday=[{'open': time_objects[4], 'close': time_objects[5]}],
            Thursday=[{'open': time_objects[6], 'close': time_objects[7]}],
            Friday=[{'open': time_objects[8], 'close': time_objects[9]}],
            Saturday=[{'open': time_objects[10], 'close': time_objects[11]}],
            Sunday=[{'open': time_objects[12], 'close': time_objects[13]}]
        )
        activity_struct = Activity(
                name=activity.name,
                address=activity.address,
                latitude=activity.latitude,
                longitude=activity.longitude,
                phonenumber=activity.phonenumber,
                cost=activity.cost,
                cost_estimate=activity.cost_estimate,
                category=activity.category,
                hours=hours_data,
                isBreakfast=activity.isBreakfast,
                isLunch=activity.isLunch,
                isDinner=activity.isDinner,
                rating=activity.rating,
                website=activity.website
            )
        activity_num+=1
        days_dict[day].append(activity_struct)
        if(activity_num%5==0):
            day+=1
    itinerary_struct = Itinerary (
        days = days_dict,
        startDate = itinerary.start_date,
        endDate = itinerary.end_date,
        hotel = itinerary.hotel
    )
    # print(itinerary_struct)
    return itinerary_struct

def parse_and_generate(dest, hotel, start, end, opt, foodPrefs, activityPrefs):
    # calculates the number of days for the trip and the number of required restaurants/activities
    num_days = (end - start).days
    num_res = int(math.ceil(num_days * 1.5))
    num_act = num_days * 3

    lat, long = geocode(hotel)

    print("Generating restaurants and activities.")
    # get final list of restaurants and activities with appropriate amount of each meal
    final_res = filter_restaurants("food", dest, foodPrefs, num_days)
    final_act = filter_activities(lat, long, activityPrefs, num_days)

    # concatenated list of activities and restaurants to be passed into optimization algorithms
    final_res_act = final_res + final_act
    # print(final_res_act)

    print("Building your itinerary.")

    plan = Itinerary (
            days = None,
            startDate = start,
            endDate = end,
            hotel = hotel
        )

    # call specific optimization algorithms based on user preference
    if (opt == "transit"):
        # send to sidra
        print("Optimizing on Transit Time.")
        planned_days = ft.greedy_fastest_itinerary(final_res_act, hotel, num_days)
        
        plan = Itinerary (
            days = planned_days,
            startDate = start,
            endDate = end,
            hotel = hotel
        )
    elif (opt == "ratings"):
        # send to sarah
        print("Optimizing on ratings.")
        planned_days = br.best_rated_itinerary(final_res_act, num_days)
        
        plan = Itinerary (
            days = planned_days,
            startDate = start,
            endDate = end,
            hotel = hotel
        )
    elif (opt == "cost"):
        # send to sarah
        print("Optimizing on cost.")
        planned_days = cheap.cheapest_itinerary(final_res_act, num_days)
        
        plan = Itinerary (
            days = planned_days,
            startDate = start,
            endDate = end,
            hotel = hotel
        )
    
    return plan

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/saved_itineraries/", methods=['GET', 'POST'])
def itineraries():
    user_email = session.get('user_email')
    itineraries_list = []
    itineraries = Itineraries.query.filter_by(user_email=user_email).all()
    # print(itineraries)
    for itinerary in itineraries:
        itinerary_times = str(itinerary.start_date) + " - " + str(itinerary.end_date)
        itineraries_list.append((itinerary.id, itinerary_times))
    # print(f"List: {itineraries_list}")
    return render_template("saved_itineraries.html", user_email=user_email, itineraries=itineraries_list)

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Email and password are required.', 'error')
        elif not is_valid_email(email):
            flash('Invalid email address.', 'error')
        elif len(password) < 8:  
            flash('Password must be at least 8 characters long.', 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            session['user_email'] = email
            return render_template("welcome.html")
        

    return render_template("signup.html")


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


# @app.route("/itinerary/")
# @app.route("/itinerary/<num>")
# def itinerarydisplay(num = None):
#     if num == None:
#         num = 0
#     int(num)
#     timestamp_str = datetime.now().strftime('%Y%m%d%H%M%S')
#     return render_template("itinerary.html", plan=itinerary.days, startdate=itinerary.startDate, enddate = itinerary.endDate, hotel = itinerary.hotel, num=num, timestamp=timestamp_str)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_email'] = user.email
            return render_template("welcome.html")
        else:
            error = "Invalid email or password"
    return render_template("login.html", error=error)

@app.route('/welcome')
def welcome():
    user_email = session.get('user_email')
    return render_template('welcome.html', user_email=user_email)


@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return render_template("landing.html")

@app.route('/plan_trip')
def plan_trip():
    return render_template("landing.html")


# app name and inbuilt function which takes error as parameter 
@app.errorhandler(404) 
def not_found(e): 
# defining function 
  return render_template("404.html") 

# app name and inbuilt function which takes error as parameter 
@app.route('/504')
def handle_504_error():
# defining function 
  return render_template("504.html") 


