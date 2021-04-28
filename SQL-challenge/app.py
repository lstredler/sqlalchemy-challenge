#import dependencies
import numpy as np
import datetime as dt
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#generate the engine to the corrext sqlite file 
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
#Uses the automap_base()
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station=Base.classes.station

#create and bind the session between the python app and database 
session=Session(engine)

#################################################
# Flask Setup - list available routes 
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"- Rain total by date and station
        f"/api/v1.0/stations<br/>"
        f"- List of station names 
        f"/api/v1.0/tobs<br/>"
        f"- List of temperature observations
        f"/api/v1.0/start<br/>"
        f"- The max, min and average temperature is given at start date 
        f"/api/v1.0/start/end<br/>"
        f"- The max, min and average temperature is given at start/end date 

    )
##############################################


@app.route("/api/v1.0/precipitation")
def stations():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >last_12_months).\
    order_by(Measurement.date).all()


##############################################

@app.route("/api/v1.0/stations")
def stations():

    """Return a list of stations"""
    # Query measurements 
    station_query = session.query(Stations.name, Station.station)
    stations=pd.read_sql(stations_query.statement, stations_query.session.bind)
    return jsonify(stations.to_dict())

##############################################
@app.route("/api/v1.0/tobs")
def tobs():
