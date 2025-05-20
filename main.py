import pandas as pd
import yaml

# load configuration params
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)
data_location = config["constants"]["data_location"]
sql_location = config["constants"]["sql_location"]

# get input from user
incident = input("Enter incident number: ")

# read the CSV file
data = pd.read_csv(f"{data_location}/HomeCity.csv")

# sql select statement template
select = "SELECT '{}','{}' from dual"

# initialize sql script
insert = "INSERT INTO table_name (City,Number)\n"

# iterate over the rows and construct the sql script
for index, row in data.iterrows():
    if index != 0:
        insert += " UNION ALL\n"
    insert += select.format(row['City'], row['Number'])

# save sql script to file
with open(f"{sql_location}/{incident}-insert.sql", "w") as file:
    file.write(insert)
