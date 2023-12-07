class SelectionSort:
    def __init__(self,arr):
        self.arr=arr
    def sort_(self,array):
        for i in range(len(array)-1):
            mini=i
            for j in range(i+1,len(array)):
                if array[j] < array[mini]:
                    mini = j
            if mini !=i:
                array[i],array[mini]=array[mini],array[i]
        return array

if __name__ == "__main__":
    arr=[1,50,3,2,0,800,300]
    ob=SelectionSort(arr)
    print(ob.sort_(arr))
