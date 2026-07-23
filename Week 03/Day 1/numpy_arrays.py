

#--------- learn numpy (Numerical python)

#----practise 1
#import numpy as np

#numbers = np.array([10, 20, 30, 40, 50])

#print(numbers) 

# -----------------
# practise 2

#import numpy as np
#list = np.array([1, 2, 2, 3, 1, 2, 4, 5, 7])
#print(list)
 
# --------------- 
# practise 3
#import numpy as np 
#age = np.array([12, 30, 40, 43, 47])
#print(age)

# --------------- 
# practise 4
#import numpy as np

#numbers = np.array([10,20,30,40,50])

#print(numbers)
#print(type(numbers)) # datatype

#---------------------
#import numpy as np 

#arr = np.array([12, 12, 13, 14])
#print(arr)
#print(type(arr))
#-------------------------- 

# Use a tuple to create a NumPy array:
#import numpy as np

#arr = np.array((1, 2, 3, 4, 5, 6))
#print(arr)
#print(type(arr))

#-------------------
# Create a 0-D array with value 65

#import numpy as np 
#arr = np.array(65)
#print(arr)

#-------------------------
# Create a 1-D array containing the values 1,2,3,4,5:

#import numpy as np

#arr = np.array([1, 2, 3, 4, 5])

#print(arr)

#----------------------
# Create a 2-D array containing two arrays with the values

#import numpy as np

#arr =   np.array([[12, 21, 43],[56, 32, 11]])
#print(arr)

#-------------------------
# Create a 3-D array with two 2-D arrays, both containing two arrays with the values

#import numpy as np
#arr = np.array([[[1,2,3],[4,5,6], [1,2,3],[4,5,6]]])
#print(arr)

#----------------- 
# Check how many dimensions the arrays have:

#import numpy as np

#a = np.array(42)
#b = np.array([1, 2, 3, 4, 5])
#c = np.array([[1, 2, 3], [4, 5, 6]])
#d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

#----------------- Array indexing in 1-dimesional
#import numpy as np 
#arr = np.array([10, 20, 30, 40])
#print(arr[1])

# Practise 1
#import numpy as np
#arr = np.array([1, 2, 3, 4, 5, 6])
#print(arr[0])
#print(arr[1])
#print(arr[2])
#print(arr[3])

# practise 2
#import numpy as np
#arr = np.array([1,2,3,4])
#print(arr[3]+arr[2])

#---------------------- 2D array indexing 
#import numpy as np
#arr = np.array([[1,2,3],[4,5,6]])
#print(arr[1,2])

#---------------- 3-D array indexing
#import numpy as np
#arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#print(arr[1,1,0])


#---------------------------------------------------------
# numpy array slicing
#import numpy as np
#arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print (arr[4:])

# negative slicing
#import numpy as np
#arr = np.array([1,2,3,4,5,6,7,8])
#print(arr[-1:-3])