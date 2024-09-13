import csv, os
reader = []
with open('customer_transactions.csv', 'r', encoding="utf-8") as f:
    # # Create a CSV reader object
    reader = csv.reader(f)
    # print(type(reader))

    # # Iterate over each row and print it
    # for row in reader:
    #     print(type(row))
    #     print(row[3])
        # print(row)
# filter data inluding transactions with age range of 25 to 40
    min_age = 25
    max_age = 40
    filtered__transactions = []
    for row in reader:
        age = 0 if row[3] == '' else int(row[3]) 
        if min_age <= age <= max_age:
            filtered__transactions.append(row)
for transaction in filtered__transactions:
    print(transaction)
