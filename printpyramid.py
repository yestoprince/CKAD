def print_pyramid(height):
    for i in range(1, height + 1):
        # Print leading spaces
        print(" " * (height - i), end="")
        
        # Print stars
        print("*" * (2 * i - 1))

# Example: Print a pyramid with height 5
print_pyramid(20)
