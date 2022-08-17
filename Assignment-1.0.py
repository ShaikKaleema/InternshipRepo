#Function to count the repeated elements
def repeat(arr,n):
#traverse throughout the elements if they are repeated mark as repeated.
    repeated=[False for i in range(n)]
    for i in range(n):
        if (repeated[i]==True):
            continue
        count=1
        for j in range(i+1,n,1):
            if arr[i]==arr[j]:
                repeated[j]=True
                count+=1
        if count!=1:
            print(arr[i])


# Driver code
length = int(input("Enter number of elements:")) 
arr = [] 
for i in range(length): 
    x=int(input("Enter element:"))
    arr.append(x)
n = len(arr)
#Finding biggest element
maximum=max(arr)
print("Biggest element:",maximum)
#Finding smallest element
minimum=min(arr)
print("Smallest element:",minimum)
print("The repeated elements are:")
# function call
repeat(arr, n)
exit()