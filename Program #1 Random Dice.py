
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.



import random

# Function to roll two dice and return their sum
def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

# Mainline to call randDice 100 times and calculate the average
def main():
    total_sum = 0
    for _ in range(100):
        total_sum += randDice()
    
    # Calculate the average and round it to 2 decimal places
    average = round(total_sum / 100, 2)
    
    # Print the average of 100 rolls
    print(f"Average of 100 dice rolls: {average}")

# Call the main function to execute the program
main()



#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
