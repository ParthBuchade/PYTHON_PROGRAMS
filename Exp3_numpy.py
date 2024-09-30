import numpy
import numpy as np

arr = np.array([4.4,5.5,3.0,6.7,np.nan])
print(len(arr)) # it will print 5...it considers nan value also

print(arr.max()) # print nan

# for maximum value excepting nan

print(np.nanmax(arr))
 # summation of each element in array
print(numpy.nansum(arr))

# finding avg of array elements

avg = (numpy.nansum(arr))/(len(arr))

print(avg)