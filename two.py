def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return i,j
    return -1
n = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter element value:"))
    arr.append(num)
target = int(input("Enter target value:"))    
result = two_sum(arr,target)  
if result != -1:
    print("Incides are",result)
else:
    print("No pair found")    
