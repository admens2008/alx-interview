
#!/usr/bin/python3
import sys

def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to meet a given total.
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount to be made using the fewest number of coins.
    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any combination of coins, returns -1.
    '''
    if total <= 0:
        return 0

    # Initialize the table with a large number (sys.maxsize)
    table = [sys.maxsize] * (total + 1)
    table[0] = 0

    # Loop through all amounts from 1 to total
    for i in range(1, total + 1):
        # Check for each coin
        for coin in coins:
            if coin <= i:
                subres = table[i - coin]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    # If the total cannot be met by any combination of coins, return -1
    return -1 if table[total] == sys.maxsize else table[total]

# Testing the function with the provided examples
print(makeChange([1, 2, 25], 37))   # Output should be 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output should be -1
