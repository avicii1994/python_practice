import pandas as pd

# Define the file paths
input_file = 'customer_transactions.csv'
output_file = 'filtered_customer_transactions.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)
# print(df)
# Step 1: Filter rows where customer_age is between 25 and 40, and remove rows with missing customer_age
df_filtered = df[(df['customer_age'].notna()) & (df['customer_age'].between(25, 40))]

# Step 2: Group by customer_id and calculate the total and average transaction amount
aggregated_data = df_filtered.groupby('customer_id').agg(
    total_transaction_amount=('transaction_amount', 'sum'),
    average_transaction_amount=('transaction_amount', 'mean'),
    city=('city', 'first')  # assuming the city remains the same for each customer
).reset_index()

# Step 3: Write the filtered and aggregated data to a new CSV file
aggregated_data.to_csv(output_file, index=False)

print(f"Filtered and aggregated data has been written to {output_file}.")