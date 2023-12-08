class Bubble_sort:
    def sort_(self,array):
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j]>array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
        return array
if __name__ == "__main__":
    array=[1,5,6,0,8,0,100,200]
    ob=Bubble_sort()
    print(ob.sort_(array))
