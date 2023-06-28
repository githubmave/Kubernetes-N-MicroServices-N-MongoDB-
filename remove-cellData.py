import panda as pd

df=pd.read_csv('data.csv');
# return a new data frame with NO EMPTY cell

new_df=df.dropna();

# Remove all rows with NULL values

dr.dropna(inplace= True)

# replace NULL values with the number 30
df.fillna(30, inplace= True)

#Replce NULL value in the "Calories" columns with the number 30

df["Calories"].fillna(130, inplace=True)

# find mean of column of Caleries
x=df["Calories"].mean()

# Convert into a correct format







