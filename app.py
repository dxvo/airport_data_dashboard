import os
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
#

# Don't push SQLite to git
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/airport_db.sqlite"
# app.config to route outside of repo to avoid large file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../airport_sql/airport_db.sqlite"


db = SQLAlchemy(app)



# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
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

    selCon = [
        Airport_Route.Origin
    ]

    resultsCon = db.session.query(*selCon)
    results = db.session.query(*sel).filter(info.type == "large_airport").all()


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

@app.route("/conn")
def conn():

    selCon = [
        Airport_Route.Origin,
        info.municipality,
        info.iata_code
    ]

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

    first = db.session.query(*selCon).distinct()
    second = db.session.query(*sel)
    # third = first.join(second)



    uniqueAirports = []
    for airport in first:
        uniqueAirports.append({
            "Airport": airport[0]
    #         "type": airport[1],
    #         "name": airport[2],
    #         "latitude": airport[3],
    #         "longitude": airport[4],
    #         "elevation": airport[5],
    #         "municiaplity": airport[6],
    #         "iata_code": airport[7],
    #         "home_link": airport[8]
        })

    return jsonify(uniqueAirports)

# @app.route("/airports")
# def airports():
  
#     sel = [
#         Monthly_Average.
#     ]

#     results = db.session.query(*sel).filter(info.type == "large_airport").all()

#     tooltip = []
#     for result in results:
#         tooltip.append({
#             "type": result[0],
#             "name": result[1],
#             "latitude": result[2],
#             "longitude": result[3],
#             "elevation": result[4],
#             "municiaplity": result[5],
#             "iata_code": result[6],
#             "home_link": result[7]
#         })
#     return jsonify(tooltip)


if __name__ == "__main__":
    app.run(debug=True)