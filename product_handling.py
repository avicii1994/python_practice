import json

# Define the input and output file paths
input_file = 'products.json'
output_file = 'cleaned_products.json'

# Function to clean and transform the product data
def clean_product_data(data):
    cleaned_data = []

    for product in data:
        try:
            # Convert price to float if it's a valid number
            product['price'] = float(product['price'])
        except (ValueError, TypeError):
            # If price is not a valid number, skip this product
            continue

        # Check if availability is missing or less than 1
        if product['availability'] is None or product['availability'] < 1:
            continue

        # Append cleaned product to the list
        cleaned_data.append(product)

    return cleaned_data

# Read the JSON data from the input file
with open(input_file, 'r', encoding='utf-8') as f:
    product_data = json.load(f)

# Clean and transform the product data
cleaned_product_data = clean_product_data(product_data)

# Write the cleaned data to the output JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(cleaned_product_data, f, indent=4)

print(f"Cleaned product data has been written to {output_file}.")
