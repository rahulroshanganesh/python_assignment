import csv

# Define file paths
balance_file_path = "data/CustomerAccountBalanceFile_A28.csv"
transaction_file_path = "data/CustomerAccountTrasnactionFile_A28.csv"
warning_file_path = "data/WarningFile_A28.csv"
error_file_path = "data/ErrorFile_A28.csv"
patron_file_path = "data/PatronFile_A28.csv"
updated_balance_file_path = "data/UpdatedCustomerAccountBalanceFile_A28.csv"

# Read customer balances into a dictionary
customer_balances = {}
with open(balance_file_path, mode='r') as balance_file:
    reader = csv.reader(balance_file)
    header = next(reader, None)  # Skip header
    if header:
        for row in reader:
            customer_id, balance = row
            customer_balances[customer_id] = float(balance)
 
# Read transactions and calculate total transaction amount for each customer
customer_transactions = {}
with open(transaction_file_path, mode='r') as transaction_file:
    reader = csv.reader(transaction_file)
    header = next(reader, None)  # Skip header
    if header:
        for row in reader:
            customer_id, transaction_amount = row
            if customer_id not in customer_transactions:
                customer_transactions[customer_id] = 0.0
            customer_transactions[customer_id] += float(transaction_amount)
 
# Update balances and write to files
with open(warning_file_path, mode='w', newline='') as warning_file, \
     open(error_file_path, mode='w', newline='') as error_file, \
     open(patron_file_path, mode='w', newline='') as patron_file, \
     open(updated_balance_file_path, mode='w', newline='') as updated_balance_file:
 
    warning_writer = csv.writer(warning_file)
    error_writer = csv.writer(error_file)
    patron_writer = csv.writer(patron_file)
    updated_balance_writer = csv.writer(updated_balance_file)
 
    # Write headers
    warning_writer.writerow(["CustomerID", "UpdatedBalance"])
    error_writer.writerow(["CustomerID", "UpdatedBalance"])
    patron_writer.writerow(["CustomerID", "UpdatedBalance"])
    updated_balance_writer.writerow(["CustomerID", "UpdatedBalance"])
 
    for customer_id, balance in customer_balances.items():
        total_transaction_amount = customer_transactions.get(customer_id, 0.0)
        updated_balance = balance + total_transaction_amount
 
        # Write to appropriate files based on the updated balance
        if updated_balance < 0.0:
            error_writer.writerow([customer_id, updated_balance])
        elif updated_balance < 100.0:
            warning_writer.writerow([customer_id, updated_balance])
        elif updated_balance > 60000.0:
            patron_writer.writerow([customer_id, updated_balance])
 
        # Write to the updated balance file
        updated_balance_writer.writerow([customer_id, updated_balance])
 
# Sort the final balance file in descending order of updated balance
with open(updated_balance_file_path, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader, None)  # Skip header
    sorted_balances = sorted(reader, key=lambda x: float(x[1]), reverse=True)
 
with open(updated_balance_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write header
    writer.writerows(sorted_balances)  # Write sorted data
 
print("Processing completed successfully.")