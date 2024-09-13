# import csv, os
# reader = []
# with open('customer_transactions.csv', 'r', encoding="utf-8") as f:
#     # # Create a CSV reader object
#     reader = csv.reader(f)
    
# print(reader[0])

# print(reader[1])

# print(reader[1][3])
import csv
from collections import defaultdict
# Define the file paths
input_file = 'customer_transactions.csv'
output_file = 'filtered_customer_transactions.csv'

# Define the age range
min_age = 25
max_age = 40

# A dictionary to store aggregated data for each customer
# We'll use customer_id as the key, and a dictionary to store the total and count of transactions
customer_data = defaultdict(lambda: {"total_amount": 0, "transaction_count": 0, "city": ""})

# Read the input CSV file
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    # for rows in reader:
    #     print(rows)
    # Iterate over each row in the CSV
    for row in reader:
        # Handle missing age values by skipping such rows
        if row['customer_age'] and row['customer_age'].isdigit():
            age = int(row['customer_age'])
            if min_age <= age <= max_age:
                # Get the transaction amount, customer_id, and city
                customer_id = row['customer_id']
                transaction_amount = float(row['transaction_amount'])
                city = row['city']
                
                # Aggregate the transaction data for each customer
                customer_data[customer_id]['total_amount'] += transaction_amount
                customer_data[customer_id]['transaction_count'] += 1
                customer_data[customer_id]['city'] = city
print(customer_data)
# Write the filtered and aggregated data to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['customer_id', 'total_transaction_amount', 'average_transaction_amount', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write each customer's aggregated data to the new file
    for customer_id, data in customer_data.items():
        total_amount = data['total_amount']
        transaction_count = data['transaction_count']
        average_amount = total_amount / transaction_count  # Calculate average
        city = data['city']
        
        # Write the row to the CSV
        writer.writerow({
            'customer_id': customer_id,
            'total_transaction_amount': total_amount,
            'average_transaction_amount': average_amount,
            'city': city
        })

print(f"Filtered and aggregated data has been written to {output_file}.")