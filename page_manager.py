from data_structures import ArrayR
from data_structures.linked_queue import LinkedQueue
from data_structures.array_list import ArrayList
from data_structures.linked_list import LinkedList

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
        result = LinkedList()
        if page is None:
            single_page = self.single_page
        else:
            single_page = self.generate_single_page(page)

        w1 = single_page[0]
        w2 = single_page[1]

        if len(w1) > len(w2):
            result.append(w2)
            result.append(w1)
        else:
            result.append(w1)
            result.append(w2)

        for i in range(2, len(single_page)):
            w = single_page[i]
            dif_front = abs(len(w) - len(result[0]))
            dif_last = abs(len(w) - len(result[len(result) - 1]))

            if dif_front < dif_last:
                result.insert(0, w)
            else:
                result.append(w)

        return iter(result)
        
    
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

    test = ["short", "words", "and", "long", "words", "it", "doesn't", "fully", "sort"]

    for word in pm.semi_sorted_word_iterator(pm.generate_single_page(test)):
        print(word)

    
