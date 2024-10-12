# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program


# Function to calculate taxes
def calculateTaxes(total_sales):
    state_tax_rate = 0.05  # 5% state tax
    county_tax_rate = 0.025  # 2.5% county tax
    
    state_tax = total_sales * state_tax_rate
    county_tax = total_sales * county_tax_rate
    total_sales_tax = state_tax + county_tax
    
    return state_tax, county_tax, total_sales_tax

# Main program
def main():
    # Input: Ask for the total sales amount
    total_sales = float(input("Enter the total sales for the month: $"))
    
    # Call the function to calculate taxes
    state_tax, county_tax, total_sales_tax = calculateTaxes(total_sales)
    
    # Output: Display the calculated taxes
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"Total Sales Tax: ${total_sales_tax:.2f}")

# Run the main program
main()
