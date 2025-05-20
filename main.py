import pandas as pd
import yaml

with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)

data_location = config["constants"]["data_location"]
sql_location = config["constants"]["sql_location"]

# get incident number from user
incident = input("Enter incident number: ")

# sql script formats
insert = "INSERT INTO table_name (City,Number)\n"
select = "SELECT '{}','{}' from dual"

# read the CSV file
data = pd.read_csv(f"{data_location}/HomeCity.csv")

# iterate over the rows and construct the sql script
for index, row in data.iterrows():
    if index != 0:
        insert += " UNION ALL\n"
    insert += select.format(row['City'], row['Number'])

# save sql script to file
with open(f"{sql_location}/{incident}-insert.sql", "w") as file:
    file.write(insert)
