import pandas as pd


df=pd.DataFrame({
    "Name": ["A","B","C","D","E","F"],
    "Age": [15,23,45,6,13,14],
    "City": ["Fremomt", "Madurai", "A", "B", "C", "D"]
})



data = pd.read_csv("iris.csv")
print(data.head())  
print(data.head(10))  

print(data.shape)

print(data['species']) 

print(data['sepal_length'].max())  


print(data.info())

print(data.describe())
