import csv
import os.path as path

csv_path = path.join("Resources", "budget_data.csv")

with open(csv_path, "r") as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    
    bank_data = []
    month_data = []
    cash_data = []

    for row in lines:
        bank_data.append(row)
    
    del bank_data[0]

    for row in bank_data:
        month_data.append(row[0])
        cash_data.append(row[1])
    
    month_count = len(month_data)

    total_income = 0
    most_profit = 0
    most_profit_month = ""
    most_loss = 0
    most_loss_month = ""
    average_change = 0

    for i in range(month_count):
        total_income = int(cash_data[i]) + total_income
        
        if(most_profit < int(cash_data[i])):
            most_profit = int(cash_data[i])
            most_profit_month = month_data[i]
        
        if(most_loss > int(cash_data[i])):
            most_loss = int(cash_data[i])
            most_loss_month = month_data[i]
    
    average_change = total_income / month_count

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_income}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {most_profit_month} (${most_profit})")
    print(f"Greatest Decrease in Profits: {most_loss_month} (${most_loss})")
    
    with open("financial_analysis.txt", mode="w") as out_file:
        print("Financial Analysis", file=out_file)
        print("----------------------------", file=out_file)
        print(f"Total Months: {month_count}", file=out_file)
        print(f"Total: ${total_income}", file=out_file)
        print(f"Average Change: ${average_change}", file=out_file)
        print(f"Greatest Increase in Profits: {most_profit_month} (${most_profit})", file=out_file)
        print(f"Greatest Decrease in Profits: {most_loss_month} (${most_loss})", file=out_file)