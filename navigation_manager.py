class NavigationManager:
    def __init__(self):
        pass
    
    def get_current_address(self):
        pass

    def go_to(self, address):
        """
        Time complexity analysis goes here.
        """
        pass
    
    def back_button_pressed(self):
        """
        Time complexity analysis goes here.
        """
        pass
    
    def forward_button_pressed(self):
        """
        Time complexity analysis goes here.
        """
        pass
    
    def report_address_prefix_count(self, address_prefix):
        """
        Time complexity analysis goes here.
        """
        pass


if __name__ == "__main__":
    nav = NavigationManager()
    nav.go_to("google.com")
    nav.go_to("github.com")
    nav.go_to("monash.edu")
    print(nav.get_current_address())  # monash.edu
    nav.back_button_pressed()
    print(nav.get_current_address())  # github.com
    nav.forward_button_pressed()
    print(nav.get_current_address())  # monash.edu

    # Assertions are a great way of testing your code without checking the print outputs.
    assert nav.get_current_address() == "monash.edu"

    # Continue testing your code...