def solve():
    
    n = int(input())
    list1 = list(map(int, input().split(" ")))
    i = 0
    byValue = []
    temp = []
    summ = 0

    
    while i < len(list1):
       
        if i == len(list1) - 1:
            temp.append(list1[i])
            byValue.append(temp)
            break

       
        if list1[i] > 0:
            temp.append(list1[i])
             
            if list1[i+1] < 0:
                byValue.append(temp)
                temp = []
        
        elif list1[i] < 0:
            temp.append(list1[i])
            # Check if the next element is positive
            if list1[i + 1] > 0:
                byValue.append(temp)
                temp = []

        i += 1

    
    for sublist in byValue:
        summ += max(sublist)

     
    print(summ)
t = int(input())

for _ in range(t):
    solve()
