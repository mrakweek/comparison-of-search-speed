import numpy as np
import time

def binary_search_row(row, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if row[mid] == target:
            return mid
        elif row[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start
    
def linear_search(matrix, target):
	x = 0
	y = len(matrix[0]) - 1
	while x < len(matrix) and y >= 0:
		if matrix[x][y] == target:
			return True
		elif matrix[x][y] > target:
			y -= 1
		else:
			x += 1
	return False


def binary_search(matrix, target):
	for arr in matrix:
		left = 0
		right = len(arr) - 1
		while left <= right:
			tmp = (left + right) // 2
			if arr[tmp] == target:
				return True
			elif arr[tmp] < target:
				left = tmp + 1
			else:
				right = tmp - 1
	return False


def exponential_search(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col < cols:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            start, end = col + 1, min(col * 2, cols - 1)
            col = binary_search_row(matrix[row], target, start, end)
        else:
            row += 1

    return False
	   


def create_sorted_matrix(n, m):
	matrix = np.random.randint(1, 100, size=(n, m))
	sorted_matrix = np.sort(matrix, axis=None)
	sorted_matrix = np.reshape(sorted_matrix, (n, m))
	return sorted_matrix


def create_matrix_1(m, n):
	mat = []
	for i in range(m):
		mat.append([])
		for j in range(n):
			mat[i].append((n // m * i + j) * 2)
	return mat
	
def create_matrix_2(m, n):
	mat = []
	for i in range(m):
		mat.append([])
		for j in range(n):
			mat[i].append((n // m * i * j) * 2)
	return mat


number_elements = [2 ** x for x in range(1, 14)]
time_linear_search = []
time_binary_search = []
time_exponential_search = []
print(number_elements)
print()

for size in number_elements:
	mat = create_matrix_1(size, 2 ** 13)
	target = size * 2 + 1
    
    #linear_search
	start = time.time_ns()
	linear_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_linear_search.append(end - start)
	
	#binary_search
	start = time.time_ns()
	binary_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_binary_search.append(end - start)
	
	#exponential_search
	start = time.time_ns()
	exponential_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_exponential_search.append(end - start)
	
	
print(time_linear_search)
print(time_binary_search)
print(time_exponential_search)

time_linear_search = []
time_binary_search = []
time_exponential_search = []
for size in number_elements:
	mat = create_matrix_2(size, 2 ** 13)
	target = size * 16 + 1
    
    #linear_search
	start = time.time_ns()
	linear_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_linear_search.append(end - start)
	
	#binary_search
	start = time.time_ns()
	binary_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_binary_search.append(end - start)
	
	#exponential_search
	start = time.time_ns()
	exponential_search(mat, target)
	end = time.time_ns()
	print(size, end - start)
	time_exponential_search.append(end - start)

	
	
print(time_linear_search)
print(time_binary_search)
print(time_exponential_search)