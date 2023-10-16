# Import necessary libraries
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database tables into classes
Base = automap_base()
Base.prepare(autoload_with=engine)

# Define the classes that map to the database tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session to interact with the database
session = Session(engine)



#################################################
# Flask Setup
#################################################
# Create a Flask app
app = Flask(__name__)


#################################################
# Flask Routes
##################################################

# Define the default route, which provides information about available routes
@app.route("/")
def welcome():
    return (
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start
        /api/v1.0/temp/start/end
        ''')

# Define a route to retrieve precipitation data for the last year
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query for date and precipitation data within the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    # Create a dictionary to hold the results
    precip = {date: prcp for date, prcp in precipitation}
    
    return jsonify(precip)

# Define a route to retrieve a list of stations
@app.route("/api/v1.0/stations")
def stations():
    
    # Query for a list of station codes
    results = session.query(Station.station).all()
    
    # Flatten the results and return as JSON
    stations = list(np.ravel(results))
    
    return jsonify(stations=stations)

# Define a route to retrieve temperature data for the most active station in the last year
@app.route("/api/v1.0/tobs")
def temp_monthly():
    
    # Calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Query for temperature data from the most active station within the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # Convert the query results to a list
    temps = list(np.ravel(results))
    
    return jsonify(temps=temps)

# Define a route to retrieve temperature statistics for a given date range
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start='2017-06-01', end='2017-06-30'):
    
    # Define the temperature statistics to calculate (min, avg, max)
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if end:
        # Query for temperature statistics within the specified date range
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        
    else:
        # Query for temperature statistics from the start date to the end of the data
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
    # Convert the query results to a list
    temps = list(np.ravel(results))
    
    return jsonify(temps)

if __name__ == '__main__':
    app.run()







