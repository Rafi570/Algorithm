class LinearSearch:
    def __init__(self, array):
        self.array = array

    def search(self, target):
        for index, element in enumerate(self.array):
            if element == target:
                return index  # Element found, return its index
        return -1  # Element not found
if __name__ == "__main__":
    # Creating an instance of LinearSearch
    array_to_search = [1, 3, 5, 7, 9, 11, 13]
    linear_search_instance = LinearSearch(array_to_search)

    # Searching for an element
    target_element = 7
    result = linear_search_instance.search(target_element)

    if result != -1:
        print(f"Element {target_element} found at index {result}.")
    else:
        print(f"Element {target_element} not found.")
