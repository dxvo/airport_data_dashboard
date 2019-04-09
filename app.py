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


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/airport_db.sqlite"
# 
app.config["DATABASE_URL"] = "postgres://tmbsjdrhvxvrwz:ddf6e4b3e9e2066b6d2cc86d1869c5c0d18c7575909b07a598c221ae2ea3f81f@ec2-184-72-238-22.compute-1.amazonaws.com:5432/d2fbmddig8nvpu"
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
        info.home_link
    ]

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




if __name__ == "__main__":
    app.run(debug=True)