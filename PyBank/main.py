import os
import csv

csvpath = os.path.join('Resources', 'Budget_data.csv')

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Create a list to store all rows
    all_rows = list(csvreader)

# Create a variable to store the total amount, greatest increase, greatest decrease, and average change
total_amount = 0
greatest_increase = {'date': None, 'amount': 0}
greatest_decrease = {'date': None, 'amount': float('inf')}
previous_amount = float(all_rows[0][1])
total_change = 0

# Specify the file to write to
output_path = os.path.join("Analysis", "PyBank.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:
    # Initialize csv.writer
    csvwriter = csv.writer(datafile, delimiter=',')

    # Write the header to the output file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["________________________________________________"])

    # Reset total amount for writing to the output file
    total_amount = 0

    # Write each row of data to the output file
    for i in range(1, len(all_rows)):
        row = all_rows[i]

        # Calculate the total amount for the current row independently
        total_amount = sum(float(row[1]) for row in all_rows[:i+1])

        # Update other calculations as needed
        amount_diff_increase = float(row[1]) - previous_amount
        if amount_diff_increase > greatest_increase['amount']:
            greatest_increase['date'] = row[0]
            greatest_increase['amount'] = amount_diff_increase

        amount_diff_decrease = float(row[1]) - previous_amount
        if amount_diff_decrease < greatest_decrease['amount']:
            greatest_decrease['date'] = row[0]
            greatest_decrease['amount'] = amount_diff_decrease

        total_change += amount_diff_increase

        previous_amount = float(row[1])

    # Count the number of unique dates
    num_unique_dates = len(set(row[0] for row in all_rows))

    # Write the financial results to the output file
    csvwriter.writerow(["Total Months:", num_unique_dates])
    csvwriter.writerow([f'Total: $ {total_amount}'])
    csvwriter.writerow([f'Average Change: $ {total_change / (len(all_rows) - 1)}'])
    csvwriter.writerow([f'Greatest Increase Date: {greatest_increase["date"]}, Profits: $ {greatest_increase["amount"]}'])
    csvwriter.writerow([f'Greatest Decrease Date: {greatest_decrease["date"]}, Profits: $ {greatest_decrease["amount"]}'])
    csvwriter.writerow(["Output saved to", output_path])

    # Print the results on the terminal
    print("\nFinancial Analysis")
    print("________________________________________________")
    print(f'Total Months: {num_unique_dates}')
    print(f'Total:$ {total_amount}')
    print(f'Average Change:$ {total_change / (len(all_rows) - 1)}')
    print(f'Greatest Increase Date: {greatest_increase["date"]}, Profits:$ {greatest_increase["amount"]}')
    print(f'Greatest Decrease Date: {greatest_decrease["date"]}, Profits:$ {greatest_decrease["amount"]}')
    print(f'Output saved to {output_path}')
