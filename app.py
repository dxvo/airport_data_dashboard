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


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/airport_db.sqlite"
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

<<<<<<< HEAD
    selCon = [
        Airport_Route.Origin,
        Airport_Route.Origin_lat,
        Airport_Route.Origin_long
    ]

    resultsCon = db.session.query(*selCon).distinct(Airport_Route.Origin)
    results = db.session.query(*sel).filter(info.type == "large_airport").all()

=======
    results = db.session.query(*sel).all()
>>>>>>> 0ed56869a5ef10140da6d0b085dc250445611fa0

    tooltip = []
    # for result in results:
    #     tooltip.append({
    #         "type": result[0],
    #         "name": result[1],
    #         "latitude": result[2],
    #         "longitude": result[3],
    #         "elevation": result[4],
    #         "municiaplity": result[5],
    #         "iata_code": result[6],
    #         "home_link": result[7]
    #     })
    for result in resultsCon:
        tooltip.append({
            "airport": result[0],
            "lat": result[1],
            "lon": result[2]
        })
<<<<<<< HEAD

=======
>>>>>>> 0ed56869a5ef10140da6d0b085dc250445611fa0
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
<<<<<<< HEAD
    first = db.session.query(*selCon).distinct()
    second = db.session.query(*sel)
    # third = first.join(second)

=======

    results = db.session.query(*sel).all()
>>>>>>> 0ed56869a5ef10140da6d0b085dc250445611fa0

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