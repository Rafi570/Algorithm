class QuickSort:
    def __init__(self,array):
        self.array=array

    def sort_(self,low,high):
        if low<high:
            partition_i= self.partition(low,high)
            self.sort_(low,partition_i-1)
            self.sort_(partition_i+1,high)
        return self.array
    def partition(self,low,high):
        pivot=self.array[high]

        i=low-1
        for j in range(low,high):
            if self.array[j]<=pivot:
                i+=1
                self.array[i],self.array[j]=self.array[j],self.array[i]
        self.array[i+1],self.array[high]=self.array[high],self.array[i+1]
        return i+1
if __name__ == "__main__":
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ob=QuickSort(input_list)
    print(ob.sort_(0,len(input_list)-1))
