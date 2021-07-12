import math
import sys
 
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x and self.y > other.y:
            return True
        return False
 
    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False
 
def partition(arr, low, high):
    i = low         
    pivot = arr[high]     
 
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
 
    arr[i], arr[high] = arr[high], arr[i]
    return i
 
def quicksort(arr, low, high):
	if len(arr) == 1:
		return arr
	
	if low < high:
		p = partition(arr, low, high)
		
		quicksort(arr, low, p - 1)
		quicksort(arr, p + 1, high)
 
def find_side(p1, p2, p):
    val = (p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x)
 
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0
 
def distance(p1, p2, p):
    return abs ((p.y - p1.y) * (p2.x - p1.x) - 
               (p2.y - p1.y) * (p.x - p1.x))
 
def distance2(p1, p2):
    num = pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2)
    num = math.sqrt(num)
    return num
 
def quickhull_top(points, left, right, edges):
    index = -1
    max_dist = 0
 
    for i in range(left, right):
        temp_dist = distance(points[left], points[right], points[i])
        if find_side(points[left], points[right], points[i]) == 1 and temp_dist > max_dist:
            max_dist = temp_dist
            index = i
 
    if index == -1:
        return
 
    edges.append(points[index])
 
    quickhull_top(points, left, index, edges)
    quickhull_top(points, index, right, edges)
 
def quickhull_bottom(points, left, right, edges):
    index = -1
    max_dist = 0
 
    for i in range(left, right):
        temp_dist = distance(points[left], points[right], points[i])
        if find_side(points[left], points[right], points[i]) == -1 and temp_dist > max_dist:
            max_dist = temp_dist
            index = i
 
    if index == -1:
        return
 
    edges.append(points[index])
 
    quickhull_bottom(points, left, index, edges)
    quickhull_bottom(points, index, right, edges)
 
 
def driver(points, d, size):
	if size <= 1:
		print("0.00")
		print('1')
		return
	
	top_points = [points[0], points[size - 1]]
	bottom_points = [points[0], points[size - 1]]
	
	quickhull_top(points, 0, size - 1, top_points)
	quickhull_bottom(points, 0, size - 1, bottom_points)
	
	quicksort(top_points, 0, len(top_points) - 1)
	
	quicksort(bottom_points, 0, len(bottom_points) - 1)
	
	indexes = []
	for point in bottom_points:
		indexes.append(d[point])
	
	for i in range(1, len(top_points) - 1):
		indexes.append(d[top_points[i]])
	length = 0
	for i in range(0, len(top_points) - 1):
		length += distance2(top_points[i], top_points[i + 1])
	
	for i in range(0, len(bottom_points) - 1):
		length += distance2(bottom_points[i], bottom_points[i + 1])
	
	length = round(length, 2)
	formatted_float = "{:.2f}".format(length)
	print(formatted_float)
	for num in indexes:
		print(num, end=" ")
	print('')

first_flag = 1
blank_flag = 0
size_flag = 0	
coor_flag = 0
size = 0
points = []
d = {}
index = 1
for line in sys.stdin:
	if first_flag == 1:
		first_flag = 0
		blank_flag = 1
	elif blank_flag == 1:
		blank_flag = 0
		size_flag = 1
	elif size_flag == 1:
		size = int(line.strip())
		size_flag = 0
		coor_flag = 1
	elif coor_flag == 1 and size > 0:
		coor = line.strip()
		x = 0
		y = 0
		temp = 0
		flag = 0
		for char in coor:
			if char.isnumeric():
				temp *= 10
				temp += int(char)
			elif char == '-':
				flag = 1
			else:
				if flag == 1:
					temp *= -1
					flag = 0
				x = temp
				temp = 0
			if flag == 1:
				temp *= -1
			y = temp
		p = point(x, y)
		points.append(p)
		d[p] = index
		size -= 1
		index += 1
	elif size == 0:
		driver(points, d, index - 1)
		points.clear()
		d.clear()
		coor_flag = 0
		size_flag = 1
		index = 1
		print('')
driver(points, d, index - 1)