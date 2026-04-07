from data_structures.linked_stack import LinkedStack

class NavigationManager:
    def __init__(self):
        self.back_address = LinkedStack()
        self.forward_address = LinkedStack()
        self.current_address = None
    
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
        pass


if __name__ == "__main__":
    nav = NavigationManager()
    print(nav.get_current_address()) 
    nav.go_to("google.com")
    nav.go_to("github.com")
    nav.go_to("monash.edu")
    print(nav.get_current_address())  # monash.edu
    nav.back_button_pressed()
    print(nav.get_current_address())  # github.com
    nav.back_button_pressed()
    print(nav.get_current_address())  # monash.edu
    nav.back_button_pressed()
    print(nav.get_current_address()) 
    nav.forward_button_pressed()
    print(nav.get_current_address()) 
    nav.forward_button_pressed()
    print(nav.get_current_address()) 
    nav.forward_button_pressed()
    print(nav.get_current_address()) 
    nav.forward_button_pressed()
    print(nav.get_current_address()) 

    # Assertions are a great way of testing your code without checking the print outputs.
    assert nav.get_current_address() == "monash.edu"

    # Continue testing your code...