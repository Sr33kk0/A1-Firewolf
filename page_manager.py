from data_structures import ArrayR
from data_structures.linked_queue import LinkedQueue
from data_structures.array_list import ArrayList

class PageManager:
    def __init__(self, original_page: ArrayR):
        """
        Don't change this method.
        Only implement the other functions.
        """
        self.single_page: ArrayR = self.generate_single_page(original_page)
    
    def generate_single_page(self, page):
        """
        Analyse the time complexity.
        """
        queue = LinkedQueue()
        result = ArrayList()

        queue.append(page)

        while not queue.is_empty():
            current_array = queue.serve()

            for item in current_array:
                if type(item) == str:
                    result.append(item)
                else:
                    queue.append(item)

        return ArrayR.from_list(result) #O(n)

    def semi_sorted_word_iterator(self, page):
        pass
    
    def is_page_ai(self, pattern: str):
        """
        Analyse the time complexity.
        """
        pass


if __name__ == "__main__":
    """
    Write tests for your code here...
    """
    page = ["Page", "level", "one", "link", 
    [
        "Page", "level", "two", "link", ["Page", "level", "three"],
        "more", "of", "level", "two", "another", "link", ["Last", "page!"],
        "and", "end", "of", "page", "two"
    ],
    "end"]
    pm = PageManager(page)
    print(pm.single_page)

    
