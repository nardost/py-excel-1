import pandas as pd

# get incident number from user
incident = input("Enter incident number: ")
# sql script formats
insert = "INSERT INTO table_name (col1,col2)\n"
select = "SELECT '{}','{}'"
# read the CSV file
data = pd.read_csv("./data/HomeCity.csv")
# iterate over the rows and construct the sql script
for index, row in data.iterrows():
    if index != 0:
        insert += " UNION ALL\n"
    insert += select.format(row['City'], row['Number'])

# save sql script to file
with open(f"./sql/{incident}-insert.sql", "w") as file:
    file.write(insert)
