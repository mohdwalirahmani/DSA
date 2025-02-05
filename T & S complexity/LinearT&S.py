# Linear Time and Space Complexity

def linear_eg(arr):
    new_list = []                           # empty list
    for num in arr:                         # loop h isliye O(n) operations honge
        new_list.append(num*2)              # harr no. ko 2 se multiple kr k list m add krenge
    return new_list

print(linear_eg([1,2,3,4]))

