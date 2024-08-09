import matplotlib.pyplot as plt
import pandas as pd
Customer_Table_df = pd.read_csv('Cleaned_Customer_Table.csv')
Market_Trend_df = pd.read_csv('Cleaned_Market_Trend.csv')
Product_Detail_df = pd.read_csv('Cleaned_Product_Detail.csv')
Product_Group_df = pd.read_csv('Cleaned_Product_Group.csv')
Sale_table_df = pd.read_csv('Cleaned_Sale_table.csv')
Website_access_category_df = pd.read_csv('Cleaned_Website_access_category.csv')


# Website_access_category_df['access_date'] = pd.to_datetime(Website_access_category_df['access_date'])

# # Trích xuất năm và tháng
# Website_access_category_df['year'] = Website_access_category_df['access_date'].dt.year
# Website_access_category_df['month'] = Website_access_category_df['access_date'].dt.month

# # Nhóm dữ liệu theo năm và tháng, đếm số lượt truy cập
# monthly_visits = Website_access_category_df.groupby(['year', 'month']).size().reset_index(name='visit_count')

# # Vẽ biểu đồ
# plt.figure(figsize=(12, 8))
# for year in monthly_visits['year'].unique():
#     data = monthly_visits[monthly_visits['year'] == year]
#     plt.plot(data['month'], data['visit_count'], marker='o', label=str(year))

# plt.xlabel('Month')
# plt.ylabel('Number of Visits')
# plt.title('Monthly Website Visits by Year')
# plt.legend(title='Year')
# plt.grid(True)
# plt.tight_layout()
# plt.show()





import seaborn as sns

# Chuyển đổi 'trend_start_date' và 'trend_end_date' sang định dạng datetime
Market_Trend_df['trend_start_date'] = pd.to_datetime(Market_Trend_df['trend_start_date'])
Market_Trend_df['trend_end_date'] = pd.to_datetime(Market_Trend_df['trend_end_date'])

# Tính toán khoảng thời gian của xu hướng
Market_Trend_df['trend_duration'] = (Market_Trend_df['trend_end_date'] - Market_Trend_df['trend_start_date']).dt.days

# Thiết lập palette màu cho các nhóm sản phẩm
palette = sns.color_palette("husl", len(Market_Trend_df['product_group_id'].unique()))

# Tạo biểu đồ Scatter Plot với seaborn
plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=Market_Trend_df, 
    x='product_group_id', 
    y='trend_duration', 
    hue='product_group_id', 
    palette=palette, 
    legend='full'
)

# Thêm nhãn và tiêu đề
plt.xlabel('Product Group ID')
plt.ylabel('Trend Duration (days)')
plt.title('Detailed Scatter Plot of Trend Duration by Product Group ID')
plt.grid(True)
plt.tight_layout()
plt.legend(title='Product Group ID', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()



# Sale_table_df['sale_date'] = pd.to_datetime(Sale_table_df['sale_date'])
# Sale_table_df['year'] = Sale_table_df['sale_date'].dt.year
# Sale_table_df['month'] = Sale_table_df['sale_date'].dt.month
# monthly_revenue = Sale_table_df.groupby(['year', 'month'])['Total Revenue'].sum().reset_index()
# plt.figure(figsize=(12, 8))
# for year in monthly_revenue['year'].unique():
#     data = monthly_revenue[monthly_revenue['year'] == year]
#     plt.plot(data['month'], data['Total Revenue'], marker='o', label=str(year))

# plt.xlabel('Month')
# plt.ylabel('Total Revenue')
# plt.title('Revenue in one year')
# plt.legend(title='Year')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# print(Product_Group_df.head())
# revenue_by_product_type = Product_Group_df.groupby('group_name')['Revenue by Product Type'].sum().reset_index()
# revenue_by_product_type = revenue_by_product_type.sort_values(by='Revenue by Product Type', ascending=False)
# plt.figure(figsize=(10, 6))
# plt.bar(revenue_by_product_type['group_name'], revenue_by_product_type['Revenue by Product Type'], color='skyblue')
# plt.xlabel('Product Type')
# plt.ylabel('Total Revenue')
# plt.title('Total Revenue by Product Type')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()



# paths = Website_access_category_df['Popular Paths'].unique()
# plt.figure(figsize=(12, 8))
# for path in paths:
#     path_data = Website_access_category_df[Website_access_category_df['Popular Paths'] == path]
#     plt.plot(path_data['Access Date'], path_data['Number of Visits'], marker='o', label=path)
# plt.title('Comparison of Popular Paths')
# plt.xlabel('Date')
# plt.ylabel('Number of Visits')
# plt.legend(title='Paths')
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
