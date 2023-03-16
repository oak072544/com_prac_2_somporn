# Sample 2D array
original_array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 6, 3]]

# Transpose the array
transposed_array = [[original_array[j][i] for j in range(len(original_array))] for i in range(len(original_array[0]))]

print(transposed_array)
# Output: [[1, 5, 9], [2, 6, 0], [3, 7, 6], [4, 8, 3]]