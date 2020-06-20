import json
import logging
import os

import pandas

from dataclasses import dataclass
from .const import DATA_PATH
from .const import TPH_CORONAVIRUS_XLSX_FILENAME

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

    # total_cases = pandas.read_excel(
    #     os.path.join(DATA_PATH, TPH_CORONAVIRUS_XLSX_FILENAME),
    #     sheet_name="Total Cases"
    # )

    cases_by_outcome = pandas.read_excel(
        os.path.join(DATA_PATH, TPH_CORONAVIRUS_XLSX_FILENAME),
        sheet_name="Cases by Outcome"
    )

    cases_by_episode_date = pandas.read_excel(
        os.path.join(DATA_PATH, TPH_CORONAVIRUS_XLSX_FILENAME),
        sheet_name="Cumulative Cases by Episode Dat"
    )
    
    cases = {}

    # cases["all"] = total_cases.at[0, 'Case Count']
    cases["all"] = cases_by_outcome.query("Outcome == 'All Cases'").reset_index().at[0, 'Case Count']
    cases["active"] = cases_by_episode_date.query("`Measure Names` == 'Active Cases'").reset_index().at[0, 'Case Count']
    cases["recovered"] = cases_by_outcome.query("Outcome == 'Recovered Cases'").reset_index().at[0, 'Case Count']
    cases["deaths"] = cases_by_outcome.query("Outcome == 'Deaths'").reset_index().at[0, 'Case Count']
    
    return cases