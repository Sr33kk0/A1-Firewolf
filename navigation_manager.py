from data_structures.linked_stack import LinkedStack
from data_structures.array_sorted_list import ArraySortedList

class NavigationManager:
    def __init__(self):
        self.back_address = LinkedStack()
        self.forward_address = LinkedStack()
        self.current_address = None
        self.visits = ArraySortedList()
    
    def get_current_address(self):
        return self.current_address

    def go_to(self, address):
        """
        :complexity: Best case is O(log N) where N is the number of past visits.
        Best case happens when the address is added at the end of the ArraySortedList. 
        The binary search takes O(log N) to find the index while no shuffling is needed

        Worst case is O(N) where N is the number of past visits.
        Worst case happens when the address is inserted at the beginning of the ArraySortedList.
        It requires all elements to be shifted to the right, which is O(N)
        """
        if self.current_address is not None:
            self.back_address.push(self.current_address)

        self.current_address = address
        self.forward_address.clear()

        self.visits.add(address)
    
    def back_button_pressed(self):
        """
        :complexity: Best/Worst case is O(1).
        Pushing and popping a LinkedStack takes constant time only. Thus, O(1)
        """
        if self.current_address is None:
            return

        self.forward_address.push(self.current_address)

        if self.back_address.is_empty():
            self.current_address = None
        else:
            self.current_address = self.back_address.pop()
        
    
    def forward_button_pressed(self):
        """
        :complexity: Best/Worst case is O(1).
        Pushing and popping a LinkedStack takes constant time only. Thus, O(1)
        """
        if self.forward_address.is_empty():
            return

        if self.current_address is not None:
            self.back_address.push(self.current_address)

        self.current_address = self.forward_address.pop()
    
    def report_address_prefix_count(self, address_prefix):
        """
        :complexity: Best case is O(1).
        Best case happens when visits ArraySortedList is empty returns 0 immediately., 
        or when address_prefix is greater than every stored visit returns 0 immediately,
        or when the first visit is the only element with address_prefix where the for loop only iterates 1 time.

        Worst case is O(N) where N is the number of entries in self.visits.
        Worst case happens when every visit matches address_prefix, causing the for loop
        to iterate all N times. 
        The binary search runs in O(log N).
        (log N + N) = O(N) overall.
        """
        if len(self.visits) == 0:
            return 0
        elif self.visits[0].startswith(address_prefix):
            low = 0 
        elif address_prefix > self.visits[-1]:
            return 0
        else:
            low = 0
            high = len(self.visits) - 1
            while low < high:
                middle = (low + high) // 2
                if self.visits[middle] >= address_prefix:
                    high = middle
                else:
                    low = middle + 1

        count = 0
        for i in range(low, len(self.visits)):
            if self.visits[i].startswith(address_prefix):
                count += 1
            else:
                break

        return count

if __name__ == "__main__":
    # nav = NavigationManager()
    # print(nav.get_current_address()) 
    # nav.go_to("google.com")
    # nav.go_to("github.com")
    # nav.go_to("monash.edu")
    # print(nav.get_current_address())  # monash.edu
    # nav.back_button_pressed()
    # print(nav.get_current_address())  # github.com
    # nav.back_button_pressed()
    # print(nav.get_current_address())  # monash.edu
    # nav.back_button_pressed()
    # print(nav.get_current_address()) 
    # nav.forward_button_pressed()
    # print(nav.get_current_address()) 
    # nav.forward_button_pressed()
    # print(nav.get_current_address()) 
    # nav.forward_button_pressed()
    # print(nav.get_current_address()) 
    # nav.forward_button_pressed()
    # print(nav.get_current_address()) 

    # Assertions are a great way of testing your code without checking the print outputs.
    # assert nav.get_current_address() == "monash.edu"
    nav = NavigationManager()
    nav.go_to("https://monash.edu")
    nav.go_to("https://google.com")
    nav.go_to("https://github.com")
    nav.go_to("https://google.com/search?q=what+is+python")
    nav.go_to("https://handbook.monash.edu")
    nav.go_to("https://monash.edu/it")
    nav.go_to("https://monash.edu/it/future-students/undergraduate")
    nav.go_to("https://monash.edu/it")

    print(nav.report_address_prefix_count("https://google.com"))
    print(nav.report_address_prefix_count("https://google.com/search"))
    print(nav.report_address_prefix_count("https://www.google.com"))
    print(nav.report_address_prefix_count("https://monash.edu"))

    # Continue testing your code...