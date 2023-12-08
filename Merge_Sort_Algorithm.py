class MergeSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        if len(self.array) > 1:
            mid = len(self.array) // 2
            left_half = self.array[:mid]
            right_half = self.array[mid:]

            left_sorter = MergeSort(left_half)
            right_sorter = MergeSort(right_half)

            left_sorter.sort()
            right_sorter.sort()

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.array[k] = left_half[i]
                    i += 1
                else:
                    self.array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self.array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self.array[k] = right_half[j]
                j += 1
                k += 1

    def display(self):
        print("Sorted array:", self.array)


# Example usage:
if __name__ == "__main__":
    input_array = [12, 11, 13, 5, 6, 7]
    sorter = MergeSort(input_array)
    sorter.sort()
    sorter.display()
