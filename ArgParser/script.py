import argparse
import os


parser = argparse.ArgumentParser(
    prog="script.py",
    description="Calculate statistics from a transaction file.",
    epilog="Example usage: python script.py input.csv",
)

parser.add_argument("input", help="Input file containing transactions.")
args = parser.parse_args()
input_file = args.input

base, ext = os.path.splitext(input_file)
output_file = f"{base}_output.txt"

total_records = 0
total_expenses = 0.0
total_income = 0.0
monthly_data = []

try:
    print(f"Processing file: {input_file}")
    with open(input_file, "r", encoding="utf-8") as input_f:
        for line in input_f:
            line = line.strip()
            if not line:
                continue
            try:
                parts = line.split(",")
                if len(parts) < 2:
                    continue

                month = parts[0].strip()
                income = float(parts[1].strip())
                monthly_expenses = 0.0
                for value in parts[2:]:
                    monthly_expenses += float(value.strip())

                balance = income - monthly_expenses
                monthly_data.append((month, income, monthly_expenses, balance))
                total_expenses += monthly_expenses
                total_records += 1
                total_income += income
            except ValueError:
                print(f"Warning: Skipping invalid line: {line}")

    if total_records > 0:
        expenses_mean = total_expenses / total_records
        income_mean = total_income / total_records
        balance_mean = income_mean - expenses_mean

        with open(output_file, "w", encoding="utf-8") as output_f:
            output_f.write(f"===ANNUAL TRANSACTIONS FOR {base}===\n")
            output_f.write(f"Total Records: {total_records} months\n")
            output_f.write(f"Total Income: {total_income:.2f}€\n")
            output_f.write(f"Total Expenses: {total_expenses:.2f}€\n")
            output_f.write(f"Annual Balance: {total_income - total_expenses:.2f}€\n")
            output_f.write("\n")
            output_f.write("===ANNUAL AVERAGES===\n")
            output_f.write(f"Average Monthly Income: {income_mean:.2f}€\n")
            output_f.write(f"Average Monthly Expenses: {expenses_mean:.2f}€\n")
            output_f.write(f"Average Monthly Balance: {balance_mean:.2f}€\n")
            output_f.write("\n")
            output_f.write("===MONTHLY TRANSACTIONS===\n")
            output_f.write("Monthly Expenses:\n")
            for month, income, monthly_expenses, balance in monthly_data:
                output_f.write(
                    f" {month}: {monthly_expenses:.2f}€, Income: {income:.2f}€, Balance: {balance:.2f}€\n"
                )
        print(f"Statistics have been written to '{output_file}'.")
    else:
        print("No valid transactions found in the file.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
