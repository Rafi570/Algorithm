class SelectionSort:
    def __init__(self,arr):
        self.arr=arr
    def sort_(self):
        for i in range(len(arr)-1):
            mini=i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
            if mini !=i:
                arr[i],arr[mini]=arr[mini],arr[i]
        return arr

if __name__ == "__main__":
    arr=[1,50,3,2,0,800,300]
    ob=SelectionSort(arr)
    print(ob.sort_())
