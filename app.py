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


# if __name__ == "__main__":
#     app.run(debug=True)