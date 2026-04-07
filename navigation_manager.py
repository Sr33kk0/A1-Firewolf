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
        Time complexity analysis goes here.
        """
        if self.current_address is not None:
            self.back_address.push(self.current_address)

        self.current_address = address
        self.forward_address.clear()

        self.visits.add(address)
    
    def back_button_pressed(self):
        """
        Time complexity analysis goes here.
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
        Time complexity analysis goes here.
        """
        if self.forward_address.is_empty():
            return

        if self.current_address is not None:
            self.back_address.push(self.current_address)

        self.current_address = self.forward_address.pop()
    
    def report_address_prefix_count(self, address_prefix):
        """
        Time complexity analysis goes here.
        """
        if len(self.visits) == 0:
            return 0

        low = 0
        high = len(self.visits) - 1
        while low < high:
            middle = (low + high) // 2
            if self.visits[middle] < address_prefix:
                low = middle + 1
            else:
                high = middle

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