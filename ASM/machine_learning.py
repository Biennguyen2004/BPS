import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load historical sales data
sales_data = pd.read_csv('Cleanedd_Sale_table.csv')

# Print columns to verify
print("Historical Sales Data Columns:", sales_data.columns)

# Rename column 'sale_date' to 'Date' if needed
if 'sale_date' in sales_data.columns:
    sales_data.rename(columns={'sale_date': 'Date'}, inplace=True)

# Print updated columns to verify
print("Updated Historical Sales Data Columns:", sales_data.columns)

# Convert 'Date' column to datetime
if 'Date' in sales_data.columns:
    sales_data['Date'] = pd.to_datetime(sales_data['Date'], errors='coerce')
    # Drop rows with invalid dates if any
    sales_data.dropna(subset=['Date'], inplace=True)
    # Set 'Date' as index
    sales_data.set_index('Date', inplace=True)
    # Verify the data after setting index
    print("Data After Setting Index:", sales_data.head())
else:
    print("Column 'Date' not found in historical sales data")

# Feature engineering for Linear Regression model
sales_data['Date_ordinal'] = sales_data.index.map(pd.Timestamp.toordinal)
X = sales_data[['Date_ordinal']]
y = sales_data['Total Revenue']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the mean squared error and R^2 score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Predict sales for the next 30 days
future_dates = pd.date_range(start=sales_data.index.max(), periods=30, freq='D')
future_dates_ordinal = future_dates.map(pd.Timestamp.toordinal)

# Create a DataFrame for future dates with the correct column name
future_dates_df = pd.DataFrame(future_dates_ordinal, columns=['Date_ordinal'])

# Predict future sales
future_sales = model.predict(future_dates_df)

# Create a DataFrame for future sales predictions
predicted_sales = pd.DataFrame({
    'Date': future_dates,
    'Predicted_Sales': future_sales
})
predicted_sales.set_index('Date', inplace=True)

# Plot historical and predicted sales
plt.figure(figsize=(14, 7))
plt.plot(sales_data.index, sales_data['Total Revenue'], label='Historical Sales', color='blue', linewidth=2)
plt.plot(predicted_sales.index, predicted_sales['Predicted_Sales'], label='Predicted Sales', color='red', linestyle='-.', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Historical and Predicted Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
