import os
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/airport.sqlite"
db = SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine, reflect=True)

# # Save references to each table
Airport_Route = Base.classes.Airport_Route
Delay_By_Airline = Base.classes.Delay_By_Airline
Monthly_Average = Base.classes.Monthly_Average
info = Base.classes.info

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tooltip")
def tooltip():
    sel = [
        info.type,
        info.name,
        info.latitude,
        info.longitude,
        info.elevation,
        info.municipality,
        info.iata_code,
        info.home_link]
    results = db.session.query(*sel).all()

    tooltip = []
    for result in results:
        tooltip.append({
            "type": result[0],
            "name": result[1],
            "latitude": result[2],
            "longitude": result[3],
            "elevation": result[4],
            "municiaplity": result[5],
            "iata_code": result[6],
            "home_link": result[7]
        })
    return jsonify(tooltip)


@app.route("/airlines")
def airline():
  
    sel = [
        Delay_By_Airline.Reporting_Airline,
        Delay_By_Airline.Dep_On_Late_Arr,
        Delay_By_Airline.Carrier_Delay,
        Delay_By_Airline.Weather_Delay,
        Delay_By_Airline.NAS_Delay,
        Delay_By_Airline.Security_Delay,
        Delay_By_Airline.Aircraft_Delay,
        Delay_By_Airline.Year
    ]
    results = db.session.query(*sel).all()

    airlines = []
    for result in results:
        airlines.append({
            "Reporting_Airine": result[0],
            "Dep_On_Late_Arr": result[1],
            "Carrier_Delay": result[2],
            "Weather_Delay": result[3],
            "NAS_Delay": result[4],
            "Security_Delay": result[5],
            "Aircraft_Delay": result[6],
            "Year": result[7]
        })
    return jsonify(airlines)

# Return monthly data 2017 and 2018 for a given airport
@app.route("/monthly/<airportName>")
def monthly(airportName):
        sel = [
        Monthly_Average.Month,
        Monthly_Average.Depart_Delay,
        Monthly_Average.Arrival_Delay,
        Monthly_Average.Carrier_Delay,
        Monthly_Average.Weather_Delay,
        Monthly_Average.NAS_Delay,
        Monthly_Average.Security_Delay, 
        Monthly_Average.Aircraft_Delay,
        Monthly_Average.Origin,
        Monthly_Average.Year]

        responses = db.session.query(*sel)\
                            .filter(Monthly_Average.Origin == airportName)
        
        result = []
        for response in responses:
            result.append({
                "Month": response[0],
                "Depart_Delay": response[1],
                "Arrival_Delay": response[2],
                "Carrier_Delay":response[3],
                "Weather_Delay":response[4],
                "NAS_Delay":response[5],
                "Security_Delay":response[6],
                "Aircraft_Delay":response[7],
                "Origin":response[8],
                "Year":response[9]
                })
        
        return jsonify(result)


@app.route("/routes/<airportName>")
def routes(airportName):
    sel = [
        Airport_Route.Origin,
        Airport_Route.Dest,
        Airport_Route.Origin_lat,
        Airport_Route.Origin_long,
        Airport_Route.Dest_lat,
        Airport_Route.Dest_long]

    responses = db.session.query(*sel).filter(Airport_Route.Origin == airportName)
        
    result = []
    for response in responses:
        result.append({
            "Origin": response[0],
            "Dest": response[1],
            "orgin_lat": response[2],
            "orgin_long":response[3],
            "des_lat":response[4],
            "des_long":response[5],
            })
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)














