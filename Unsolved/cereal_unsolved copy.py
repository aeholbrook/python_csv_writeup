import os
import csv

cereal_csv = os.path.join("C:/Users/adam/Downloads/CerealCleaner-20210408T210136Z-001/CerealCleaner/Resources/", "cereal.csv")


filter_contents = lambda row : row if float(row[7]) >= 5 else None

with open(cereal_csv, newline="") as csv_file:


    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    csv_reader = csv.reader(csv_file, delimiter=",")

    rows_to_print = filter(None,list(map(filter_contents,list(csv_reader))))

    print('\n'.join(map(str, rows_to_print)))