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
    if journal_dates:
        return journal_dates
    else:
        return []

def extract_secret_codes(journal_text):
    """Extracts secret codes!"""

    pattern = r"\w{5}-\d\d/\d\d/\d\d\d\d"
    journal_dates = re.findall(pattern, journal_text)
    if journal_dates:
        return journal_dates
    else:
        return []
