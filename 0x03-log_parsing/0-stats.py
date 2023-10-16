#!/usr/bin/python3
"""
This is a Python script that calculates the sum of integers from 1 to N.
"""

def calculate_sum(N):
    """
    Calculate the sum of integers from 1 to N.
    :param N: The upper limit (inclusive) for the sum.
    :return: The sum of integers from 1 to N.
    """
    if N < 1:
        return 0
    return N * (N + 1) // 2

if __name__ == "__main__":
    try:
        N = int(input("Enter an integer (N): "))
        result = calculate_sum(N)
        print(f"The sum of integers from 1 to {N} is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
