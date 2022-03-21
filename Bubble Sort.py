def countSwaps(arr):
    global count
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                count = count + 1

        if count == 0:
            break
    print("Array is sorted in %d swaps"%(count))
    print("First element is: %d"%(input_list[0]))
    print("Last element is: %d"%(input_list[-1]))
              
    return arr

n = input()
input_list = list(map(int,input().split()))
countSwaps(input_list)

