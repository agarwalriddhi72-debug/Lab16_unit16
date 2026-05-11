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

# Processing the info from the file
dates = []
unemployement_rates = []

for row in reader:
    try:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')

        #converts uneployment rate into float
        urates = float(row[1])
    except ValueError:
        print(current_date)

    else:    
        dates.append(current_date)
        unemployement_rates.append(urates)


    
#Graphing the processed data
plt.style.use('dark_background')
figure, graph = plt.subplots()

graph.plot(dates, unemployement_rates, color='blue')

#Titles and labels
graph.set_title('Ohio Unemployment (by Month): 1976 - 2022', fontsize = 24)
graph.set_ylabel("Unemp Rate", fontsize = 16)
graph.set_xlabel("Date", fontsize = 16)

# Formats the dates nicely
figure.autofmt_xdate()

#Saves the figure
plt.savefig("ohio_unemployment.png", bbox_inches = 'tight', pad_inches = 1.0)