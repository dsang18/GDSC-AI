import pandas as pd
titanic = pd.read_csv("titanic.csv")

# select columns from titanic with data type number
titanic.select_dtypes("number").columns
titanic.head(10)

# drop all rows from titanic having age or fare as null values
z = titanic.dropna(axis=0,subset=["Age","Fare"])
print(z.head(10))

# fill all null values of age with value as its mean
titanic['Age'].fillna(value=titanic['Age'].mean(), inplace=True)
print(titanic.head(10))

# fill all null values of Fare with value as its mean
titanic['Fare'].fillna(value=titanic['Fare'].mean(), inplace=True)
print(titanic.head(50))
