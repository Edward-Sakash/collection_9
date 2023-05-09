"""Task - Matrix mean
You are given a two dimensional list of numbers. Calculate the mean of those numbers by implementing a mean method that takes a list as an argument.

Input:
numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
Output:
> mean(numbers)

[19, 65, 23, 90]"""

# Solution 1

def mean(numbers):
    # Step 1: Calculate the mean of each row
    row_means = [sum(row)/len(row) for row in numbers]

    # Step 2: Return the list of row means
    return row_means

# Example usage
numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
mean_numbers = mean(numbers)
print(mean_numbers)

print("____________________________________________")

# Solution 2
def mean(numbers):
    # Initialize an empty list to store the row means
    row_means = []

    # Iterate over each row in the list
    for row in numbers:
        # Initialize a variable to store the sum of the row
        row_sum = 0
        
        # Iterate over each number in the row and add it to the row_sum
        for num in row:
            row_sum += num
        
        # Calculate the mean of the row by dividing the row_sum by the length of the row
        row_mean = row_sum / len(row)
        
        # Append the row_mean to the row_means list
        row_means.append(row_mean)

    # Return the row_means list
    return row_means

# Example usage
numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
mean_numbers = mean(numbers)
print(mean_numbers)
