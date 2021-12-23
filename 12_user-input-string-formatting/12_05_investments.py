# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

invest_amount = input("Enter the intial investment amount: ")
int_rate = input("Enter the interest rate: ")
num_years = input("Enter the number of years to invest: ")

amount = int(invest_amount)
rate = int(int_rate)/100
years = int(num_years)
pv = amount*(1 + rate)**years
print(pv)
