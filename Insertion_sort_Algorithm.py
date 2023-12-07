class insertion_sort:
    def __init__(self,array):
        self.array=array
    def sort_(self,arr):
        for i in range(len(arr)):
            item=arr[i]
            j=i-1
            while j>=0 and arr[j] > item:
                arr[j+1]=arr[j]
                j=j-1
            arr[j+1]=item
        return arr
if __name__ == "__main__":
    arr=[1,5,6,9,10,2,8,3]
    ob=insertion_sort(arr)
    print(ob.sort_(arr))
