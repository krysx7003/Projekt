# 1,2,3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 4
data = pd.read_csv("./realestate.csv", sep=";", decimal=",")
print(data.describe())

# 5
print(data.info())

# 6

data_with_outliers = data.copy()
data_with_outliers = data_with_outliers.drop(columns=["Location"])

data_with_outliers = data_with_outliers.apply(lambda x: x.mask(np.abs(zscore(x)) > 3))


data_with_outliers = data_with_outliers.dropna()
# 7

corr_matrix = data_with_outliers.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Macierz korelacji")
plt.show()

data_with_outliers["Location"] = data["Location"]

train: pd.DataFrame
test: pd.DataFrame
train, test = train_test_split(data_with_outliers, test_size=0.2, random_state=22)


features: list[str] = ["Bedrooms", "Size", "Avg_Price_m3", "Location"]
train_features = pd.get_dummies(train[features], drop_first=True).astype(int)
test_features = pd.get_dummies(test[features], drop_first=True).astype(int)
train_features.to_csv("data_with_outliers.csv", index=False)

# 9
X_train = train_features
y_train = train["Price"]


lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
pred = lin_model.predict(X_train)

X_train_optimal = sm.add_constant(X_train)
linear_model_stats = sm.OLS(y_train, X_train).fit()
print(linear_model_stats.summary())

optimal_features = ["Bedrooms", "Size", "Avg_Price_m3"] + [
    col for col in train_features.columns if "Location" in col
]
X_train_optimal = train_features[optimal_features]
linear_model_optimal = LinearRegression()
linear_model_optimal.fit(X_train_optimal, y_train)

train_pred_optimal = linear_model_optimal.predict(X_train_optimal)
r2_optimal = r2_score(y_train, train_pred_optimal)
rmse_optimal = mean_squared_error(y_train, train_pred_optimal)
print(f"Optimal Model - R-squared (Train): {r2_optimal}")
print(f"Optimal Model - RMSE (Train): {rmse_optimal}")

residuals = y_train - train_pred_optimal
plt.figure(figsize=(10, 5))
plt.plot(residuals, marker="o", linestyle="")
plt.axhline(0, color="r", linestyle="--")
plt.title("Residuals")
plt.show()

stats.probplot(residuals, dist="norm", plot=plt)
plt.title("QQ Plot of Residuals")
plt.show()

plt.hist(residuals, bins=20)
plt.title("Histogram of Residuals")
plt.xlabel("Residuals")
plt.ylabel("Frequency")
plt.show()

rmse_test = np.sqrt(mean_squared_error(test["Price"], pred))
print(f"Test RMSE: {rmse_test}")

plt.scatter(test["Price"], pred, alpha=0.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(f"Actual vs Predicted Prices\nTest RMSE: {rmse_test}")
plt.plot(
    [test["Price"].min(), test["Price"].max()],
    [test["Price"].min(), test["Price"].max()],
    "k--",
)
plt.show()

dummy_columns = train_features.columns

new_data = pd.DataFrame(
    [[3, 250, 1191] + [0] * (len(dummy_columns) - 3)], columns=dummy_columns
)
new_data["Location_San Miguel"] = 1

new_prediction = linear_model_optimal.predict(new_data).round()
print("Predicted Price for new data:", new_prediction[0])
