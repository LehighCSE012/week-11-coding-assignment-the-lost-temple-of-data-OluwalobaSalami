"""This is week 11 of the adventure."""

import pandas as pd
import re

def load_artifact_data(excel_filepath):
    """reads data from an excel file"""

    artifact_data = pd.read_excel(excel_filepath, sheet_name="Main Chamber", skiprows=3)
    return artifact_data

def load_location_notes(tsv_filepath):
    """Reads the file into a dataframe"""

    location_data = pd.read_csv(tsv_filepath, sep='\t')
    return location_data

def extract_journal_dates(journal_text):
    """Examines Dr. Reed's journal content"""

    pattern = r"\d\d/\d\d/\d\d\d\d"
    journal_dates = re.findall(pattern, journal_text)
    valid_dates = []
    for date in journal_dates:
        month, day, year = date.split("/")
        # Basic validation of month and day ranges
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and year != "9999":
            valid_dates.append(date)

    return valid_dates

def extract_secret_codes(journal_text):
    """Extracts secret codes!"""

    pattern = r"\w{5}-\d{3}"
    journal_dates = re.findall(pattern, journal_text)
    if journal_dates:
        return journal_dates
    else:
        return []
