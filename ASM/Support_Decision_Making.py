
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the sales data
sales_data_df = pd.read_csv('Cleaned_Sale_table.csv')

# Convert 'sale_date' to datetime format
sales_data_df['sale_date'] = pd.to_datetime(sales_data_df['sale_date'])

# Sort the data by date
sales_data_df = sales_data_df.sort_values('sale_date')

# Extract features and target variable
sales_data_df['Date_ordinal'] = sales_data_df['sale_date'].map(pd.Timestamp.toordinal)
X = sales_data_df[['Date_ordinal']]
y = sales_data_df['Total Revenue']  # Ensure 'Total Revenue' is the correct column for the target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error and R^2 score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Plot the actual vs predicted sales
plt.figure(figsize=(10, 6))
plt.scatter(pd.to_datetime(X_test['Date_ordinal'].apply(pd.Timestamp.fromordinal)), y_test, color='blue', label='Actual Sales')
plt.plot(pd.to_datetime(X_test['Date_ordinal'].apply(pd.Timestamp.fromordinal)), y_pred, color='red', linewidth=2, label='Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Predict sales for the next 30 days
future_dates = pd.date_range(start=sales_data_df['sale_date'].max(), periods=30, freq='D')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal)

# Create a DataFrame for future dates with the correct column name
future_dates_df = pd.DataFrame(future_dates_ordinal, columns=['Date_ordinal'])

# Predict future sales
future_sales = model.predict(future_dates_df)

# Plot future sales predictions
plt.figure(figsize=(10, 6))
plt.plot(future_dates, future_sales, color='green', linewidth=2, label='Predicted Future Sales')
plt.title('Predicted Future Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()