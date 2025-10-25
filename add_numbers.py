#!/usr/bin/env python3
"""
Simple program to add two numbers.
Supports both command-line arguments and interactive input.
"""

import sys


def add_numbers(num1, num2):
    """
    Add two numbers and return the result.
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Sum of num1 and num2
    """
    return num1 + num2


def main():
    """Main function to get user input and display the result."""
    print("=" * 40)
    print("Welcome to the Number Addition Program!")
    print("=" * 40)
    
    # Check if command-line arguments are provided
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            result = add_numbers(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        except ValueError:
            print("\nError: Please provide valid numbers as arguments!")
            print("Usage: python3 add_numbers.py <number1> <number2>")
            sys.exit(1)
    
    # Interactive mode
    else:
        if len(sys.argv) > 1:
            print("\nUsage: python3 add_numbers.py <number1> <number2>")
            print("Or run without arguments for interactive mode.\n")
            sys.exit(1)
        
        try:
            # Get input from user
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Calculate sum
            result = add_numbers(num1, num2)
            
            # Display result
            print(f"\n{num1} + {num2} = {result}")
            
        except ValueError:
            print("\nError: Please enter valid numbers!")
        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram terminated.")


if __name__ == "__main__":
    main()

