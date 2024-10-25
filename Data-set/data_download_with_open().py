import csv
from itertools import count
from pprint import pprint
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

#What I want to do
# download data and read data
# write function to find out how many ids in a list with no duplicates
#convert list of dictionaries to a pandas DataFrame
# plot it in a chart


# Download latest version
file_path = '/Users/shantirai/PycharmProjects/cgf-python/FitBit-data-analysis/Data-set/archive/dailyActivity_merged.csv'

# Function to read CSV data
def read_data():
    data = []
    with open(file_path, 'r') as file:
        spreadsheet = csv.DictReader(file)
        for row in spreadsheet:
            data.append(row)
    return data

#save data to spreadsheet_data variable
data = read_data()
one_participant = data[0]
pprint(one_participant)

# Convert the list of dictionaries to a pandas DataFrame
data_df = pd.DataFrame(data)

# Ensure the 'Id' column is in numeric format
data_df['Id'] = pd.to_numeric(data_df['Id'])

def count_ids(data_df):
    return data_df['Id'].value_counts()

id_counts = count_ids(data_df)

# Print unique Ids and their counts
pprint(id_counts)
print(f"Number of unique IDs: {len(id_counts)}")


#Create a bar plot using seaborn
plt.figure(figsize=(10,6))
sns.barplot(x=id_counts.index, y=id_counts.values)

# Add labels and title
plt.title('Count of Data Inputs per Unique Id')
plt.xlabel('Unique Id')  # Make it clear you're referring to unique identifiers
plt.ylabel('Total Count of Data Inputs')

# Rotate x-axis labels for better readability if necessary
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# return Id with lowest amount if inputs- Id: 4057192912

def get_data_for_lowest_id(data_df):
    # Count occurrences of each Id
    id_counts = data_df['Id'].value_counts()

    # Find the Id with the lowest count
    lowest_id = id_counts.idxmin()

    # Step 2: Filter the dataframe to get all rows with that Id
    data_for_lowest_id = data_df[data_df['Id'] == lowest_id]

    return lowest_id, data_for_lowest_id

# Example usage:
lowest_id, data_for_lowest_id = get_data_for_lowest_id(data_df)
print(f"Id with the lowest count: {lowest_id}")
pprint(data_for_lowest_id)
