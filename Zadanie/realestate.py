#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

import matplotlib.pyplot as plt
import numpy as np
# Importing necessary libraries
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import zscore
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# In[ ]:


# In[2]:


# Load data
dane = pd.read_csv("realestate.csv", sep=";", decimal=",")
print(dane.describe())


# In[3]:


# Summary of the dataset
print(dane.info())


# In[4]:


# Convert 'Location' to categorical and then back to string
dane["Location"] = dane["Location"].astype("category")
dane["Location"] = dane["Location"].astype(str)


# In[5]:


# Outliers handling
data_with_outliers = dane.copy()
data_with_outliers = data_with_outliers.drop(columns=["Location"])
# Replace outliers (values where z-score > 3) with NaN
data_with_outliers = data_with_outliers.apply(lambda x: x.mask(np.abs(zscore(x)) > 3))
# lambda x: to anonimowa funkcja, która przyjmuje jeden argument x.
# apply przetwarza każdą kolumnę osobno.
# zscore(x).abs() > 3 oblicza z-score dla każdej wartości w kolumnie x i sprawdza, czy jego wartość bezwzględna przekracza 3. Z-score mierzy, jak daleko (w jednostkach odchylenia standardowego) dana wartość jest od średniej – wartości z z-score > 3 są często traktowane jako wartości odstające.
# x.mask(...) zastępuje wartości w kolumnie x na NaN tam, gdzie spełniony jest warunek z-score > 3.


# Add 'Location' column back
data_with_outliers["Location"] = dane["Location"]


# In[6]:


# Remove rows with NaN values
data_without_outliers = data_with_outliers.dropna()


# In[7]:


# Calculate correlation and display heatmap
correlation_matrix = data_without_outliers.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


# In[8]:


# Split data into training and testing sets
train, test = train_test_split(data_without_outliers, test_size=0.2, random_state=42)
# Ustawienie random_state zapewnia powtarzalność podziału. Dzięki temu, za każdym razem, gdy uruchomisz ten kod, dane zostaną podzielone w ten sam sposób.


# In[9]:


# Train a linear regression model
features = ["Bedrooms", "Size", "Avg_Price_m3", "Location"]
train_features = pd.get_dummies(train[features], drop_first=True)
test_features = pd.get_dummies(test[features], drop_first=True)


# In[10]:


print(train_features)


# In[11]:


# Model 1: Initial model with all features
X_train = train_features
y_train = train["Price"]
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
train_pred = linear_model.predict(X_train)


# In[12]:


# Add a constant term for the intercept
X_train_optimal = sm.add_constant(X_train)

# Fit the model using statsmodels
linear_model_stats = sm.OLS(y_train, X_train).fit()

# Print the model summary, which includes coefficients, p-values, R-squared, etc.
print(linear_model_stats.summary())


# In[ ]:


# In[15]:


# Optimal model with selected features
# optimal_features = ['Bedrooms', 'Size', 'Avg_Price_m3'] + [col for col in train_features.columns if 'Location' in col]
optimal_features = ["Bedrooms", "Size", "Avg_Price_m3"] + [
    col for col in train_features.columns if "Location" in col
]
X_train_optimal = train_features[optimal_features]
linear_model_optimal = LinearRegression()
linear_model_optimal.fit(X_train_optimal, y_train)


# In[16]:


# Model evaluation on training data
train_pred_optimal = linear_model_optimal.predict(X_train_optimal)
r2_optimal = r2_score(y_train, train_pred_optimal)
rmse_optimal = mean_squared_error(y_train, train_pred_optimal, squared=False)
print(f"Optimal Model - R-squared (Train): {r2_optimal}")
print(f"Optimal Model - RMSE (Train): {rmse_optimal}")


# In[18]:


# Residual analysis
residuals = y_train - train_pred_optimal
plt.figure(figsize=(10, 5))
plt.plot(residuals, marker="o", linestyle="")
plt.axhline(0, color="r", linestyle="--")
plt.title("Residuals")
plt.show()


# In[19]:


# QQ-plot of residuals
import scipy.stats as stats

stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()


# In[20]:


# Histogram of residuals
plt.hist(residuals, bins=20)
plt.title("Histogram of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()


# In[21]:


# Prediction on test set
test_pred = linear_model_optimal.predict(test_features[optimal_features])
rmse_test = np.sqrt(mean_squared_error(test["Price"], test_pred))
print(f"Test RMSE: {rmse_test}")


# In[44]:


# Visualization of actual vs predicted
plt.scatter(test["Price"], test_pred, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(f"Actual vs Predicted Prices\nTest RMSE: {rmse_test}")
plt.plot(
    [test["Price"].min(), test["Price"].max()],
    [test["Price"].min(), test["Price"].max()],
    "k--",
)
plt.show()


# In[23]:


# Get the dummy column names from train_features
dummy_columns = train_features.columns

# Create new data point with the same structure as the training features
# optimal_features = ['Bedrooms', 'Size', 'Avg_Price_m3'] + Location
new_data = pd.DataFrame(
    [[3, 250, 1191] + [0] * (len(dummy_columns) - 3)], columns=dummy_columns
)
new_data["Location_San Miguel"] = 1  # Set Location_San Miguel as the active location

# Predict the price for the new data
new_prediction = linear_model_optimal.predict(new_data).round()
print("Predicted Price for new data:", new_prediction[0])


# In[ ]:
