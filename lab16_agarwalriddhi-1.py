"""
The program's name: Plot Ohio Unemployment Data
Name: Riddhi Agarwal
Purpose of Program: This program reads Ohio unemployment data from a CSV file and creates a graph showing unemployment rates over time.
Starter Code: None
Date: May 10, 2026
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

#Read the header row
header_row = next(reader)

# Use enumerate() to analyze the header row
for index, col_title in enumerate(header_row):
    print(f'{index}: {col_title}')

