#This command, while not covered above, is what measures the current time.
time1 = time.time()
#Define the path which will lead to the cereal.csv file.
cereal_csv = os.path.join("Resources", "cereal.csv")
# Open and read csv
with open(cereal_csv, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  # Read the header row first (skip this part if there is no header)
  csv_header = next(csvfile)
  print(f"Header: {csv_header}")
  # Read through each row of data after the header
  for row in csvreader:
    # Convert row to float and compare to grams of fiber
    if float(row[7]) >= 5:
      print(row)
time1 = time.time() - time1

print(f"\nTime: {time1}")