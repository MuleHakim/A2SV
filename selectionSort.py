class Solution: 
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min = i
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min = j
                
            if min != i:
                arr[min],arr[i] = arr[i],arr[min]

        return arr


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
main()
