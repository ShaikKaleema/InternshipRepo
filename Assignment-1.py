import numpy as np
from collections import Counter
# input the number of elements in an array
n=int(input("Enter the number of elements:"))
arr = np.zeros(n,dtype=int)
for i in range(len(arr)):
    x=int(input("Enter element:"))
    arr[i]=x
# Finding the biggest number in an array.
maximum=max(arr)
print("The biggest element is:",maximum)
# Finding the smallest number of an array.
minimum=min(arr)
print("The smallest element is:",minimum)
# Finding the repeated elements in an array.
repeat= [ele for ele, count in Counter(arr).items() if count > 1]
print("The repeated elements are:",repeat)
exit()
