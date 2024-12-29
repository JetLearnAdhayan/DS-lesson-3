import pandas as pd

# Create a Frame from scratch to relate a dataframe with a dictionary
df=pd.DataFrame({
    "Name": ["A","B","C","D","E","F"],
    "Age": [15,23,45,6,13,14],
    "City": ["Fremomt", "Madurai", "A", "B", "C", "D"]
})

print(df.head())#by default print first 5 rows of data
print(df.head(7))

print(df.shape)# prints the number of rows and coloums

print(df["Name"])
print(df["Age"].max()) # prints the biggest number in that list


print(df.info()) #gives the typical summary of the data

print(df.describe()) #gives the important calculations on the numerical coloums

#Loading the data from a file
data = pd.read_csv("titanic.csv")

print(data.head())
print(data.info())
print(data[["Name", "Age"]])

#Filtering Out rows
above35 = data[data["Age"]>35]
print(above35.head())
print(above35.shape)
class2and3 = data[data["Pclass"].isin([2,3])]
print(class2and3.head())
print(class2and3[["Name", "Pclass"]])

class2and3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class2and3.head(10))