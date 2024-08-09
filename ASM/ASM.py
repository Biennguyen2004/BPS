import pandas as pd

Customer_table_df = pd.read_csv('Customer_table.csv')
Market_Trend_df = pd.read_csv('Market_Trend.csv')
Product_detail_df = pd.read_csv('Product_detail.csv')
Product_group_df = pd.read_csv('Product_group.csv')
Sale_table_df = pd.read_csv('Sale_table_200.csv')
Website_access_category_df = pd.read_csv('Website_access_category.csv')

print(Customer_table_df.head())
print(Market_Trend_df.head())
print(Product_detail_df.head())
print(Product_group_df .head())
print(Sale_table_df .head())
print(Website_access_category_df.head())

print(Customer_table_df.info())
print(Market_Trend_df.info())
print(Product_detail_df.info())
print(Product_group_df.info())
print(Sale_table_df.info())
print(Website_access_category_df.info())

Customer_table_df = Customer_table_df.drop_duplicates()


Customer_table_df = Customer_table_df.fillna('Unknown') 

Market_Trend_df['trend_end_date'] = pd.to_datetime(Market_Trend_df['trend_end_date'], format='%d/%m/%Y')
Market_Trend_df['trend_start_date'] = pd.to_datetime(Market_Trend_df['trend_start_date'], format='%d/%m/%Y')

Market_Trend_df['trend_description'] = Market_Trend_df['trend_description'].str.strip()


Product_detail_df = Product_detail_df.drop_duplicates()
Product_detail_df = Product_detail_df.fillna({'stock_quantity': 0})
Product_detail_df['price'] = Product_detail_df['price'].replace('[\$,]', '', regex=True).astype(float)
Product_detail_df['stock_quantity'] = Product_detail_df['stock_quantity'].astype(int)


Product_group_df = Product_group_df.drop_duplicates()
Product_group_df  = Product_group_df .fillna({'group_description': ''})
Product_group_df ['group_id'] = Product_group_df ['group_id'].astype(int)


Sale_table_df['sale_date'] = pd.to_datetime(Sale_table_df['sale_date'])
Sale_table_df = Sale_table_df.fillna({'quantity': 0, 'total': 0})
sales_data = pd.read_csv('Cleaned_Sale_table.csv')
sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'], errors='coerce')
sales_data_sorted = sales_data.sort_values(by='sale_date', ascending=True)
sales_data_sorted.reset_index(drop=True, inplace=True)
sales_data_sorted.to_csv('Cleanedd_Sale_table.csv', index=False)
print(sales_data_sorted.head())



Website_access_category_df['access_date'] = pd.to_datetime(Website_access_category_df['access_date'])
Website_access_category_df['category_visited'] = Website_access_category_df['category_visited'].astype(str).str.strip() 
Website_access_category_df['duration'] = Website_access_category_df['duration'].astype(int)


merged_df = pd.merge(Sale_table_df, Product_detail_df, on='product_id')
Sale_table_df['Total Revenue'] = Sale_table_df['quantity'] * Sale_table_df['total']


Customer_table_df.to_csv('Cleaned_Customer_Table.csv', index=False)
Market_Trend_df.to_csv('Cleaned_Market_Trend.csv', index=False)
Product_detail_df.to_csv('Cleaned_Product_Detail.csv', index=False)
Product_group_df.to_csv('Cleaned_Product_Group.csv', index=False)
Sale_table_df.to_csv('Cleaned_Sale_table.csv', index=False)
Website_access_category_df.to_csv('Cleaned_Website_access_category.csv', index=False)
