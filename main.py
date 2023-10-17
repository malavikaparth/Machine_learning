import csv
import pandas as pd

with open('vgsales') as file:
    reader = csv.reader(file)

pd.read_csv('')
for row in reader:
    print(row)
