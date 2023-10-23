def count_elements_less(arr1, arr2):
    count = []
    n = len(arr1)
    m = len(arr2)
    i = 0   
    j = 0   

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            count.append(i)
            i += 1
        else:
            j += 1
 
    while i < n:
        count.append(i)
        i += 1

    return count

 
n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
 arr1.sort()

 
count_array = count_elements_less(arr1, arr2)

 
for num in count_array:
    print(num, end=' ')
