import codecademylib3
import pandas as pd
import numpy as np

# Loading and Exploring the Data 
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())
print(len(diabetes_data))

#Checking if there's missing data
print(diabetes_data.isnull().sum())
print(diabetes_data.describe())

#Replacing missing values with NaN
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

#Checking the actual data on missing values
print(diabetes_data.isnull().sum())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#Figuring out data types
print(diabetes_data.dtypes)

#Figuring out why the cl. 'Outcome' - object type column
print(diabetes_data['Outcome'].unique())

#Fixing it 
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(str).astype(int)
print(diabetes_data.dtypes)
