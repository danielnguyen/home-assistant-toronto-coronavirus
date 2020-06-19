import json
import logging
import os

import pandas

from dataclasses import dataclass
from .const import DATA_PATH
# from .const import TPH_CORONAVIRUS_FILEID
from .const import TPH_CORONAVIRUS_XLSX_FILENAME
from .helpers import download_file_from_google_drive
from .helpers import extract_spreadsheets_to_json

def get_cases():
    """
    Returns an object with all of the case counts.
    e.g. {
        "all": 5,
        "active": 5,
        "recovered": 5,
        "deaths": 5,
    }
    """
    # Download and save the TPH COVID-19 spreadsheet
    # download_file_from_google_drive(TPH_CORONAVIRUS_FILEID, os.path.join(DATA_PATH, TPH_CORONAVIRUS_XLSX_FILENAME))

    # Convert the XLSX file to JSON.

    data = pandas.read_excel(
        os.path.join(DATA_PATH, TPH_CORONAVIRUS_XLSX_FILENAME),
        sheet_names=["Total Cases", "Cases by Outcome", "Cumulative Cases by Episode Dat"]
    )

    # for sheet in data:
    #     # replacing blank spaces with '_' in column headers
    #     sheet.columns = [column.replace(" ", "_") for column in sheet.columns] 

    cases = {}

    cases["all"] = data["Total Cases"]["Case Count"].values[0]
    cases["active"] = data["Cumulative Cases by Episode Dat"].query("'Measure Names' == 'Active Cases", inplace=False).values[0]
    cases["recovered"] = data["Cases by Outcome"].query("Outcome == 'Recovered Cases", inplace=False).values[0]
    cases["deaths"] = data["Cases by Outcome"].query("Outcome == 'Deaths", inplace=False).values[0]
    
    return cases