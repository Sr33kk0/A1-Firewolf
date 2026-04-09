from data_structures.array_sorted_list import ArraySortedList
from data_structures.array_list import ArrayList
from data_structures.bit_vector_set import BitVectorSet

class Account:
    def __init__(self, website, username, max_password):
        self.website = website
        self.username = username
        self.password_history = ArrayList(max_password)
        self.password = None
        self.pin_history = BitVectorSet()
        self.pin = None

    def __eq__(self, other):
        return self.website == other.website and self.username == other.username
    
    def __lt__(self, other):
        if self.website == other.website:
            return self.username < other.username
        
        return self.website < other.website
    
    def __le__(self, other):
        if self.website == other.website:
            return self.username < other.username or self.username == other.username
        
        return self.website < other.website
    
    def __gt__(self, other):
        return other.__lt__(self)
    
    def __ge__(self, other):
        return other.__le__(self)

class PasswordManager:
    def __init__(self, max_passwords_per_account):
        self.accounts = ArraySortedList()
        self.max_passwords = max_passwords_per_account
    
    def get_account(self, website, username):
        account = Account(website, username, self.max_passwords)
        try:
            ind = self.accounts.index(account)
            return self.accounts[ind]
        except ValueError:
            return None

    def set_password(self, website, username, password):
        """
        Time complexity analysis goes here.
        """
        account = self.get_account(website, username)

        if account is None:
            account = Account(website, username, self.max_passwords)
            self.accounts.add(account)

        for i in range(len(account.password_history)):
            if account.password_history[i] == password:
                raise ValueError("Password has already been used for this account")
            
        account.password = password
        account.password_history.append(password)

    def set_pin(self, website, username, pin):
        account = self.get_account(website, username)

        if account is None:
            account = Account(website, username, self.max_passwords)
            self.accounts.add(account)

        if pin in account.pin_history:
                raise ValueError("Pin has already been used for this account")
            
        account.pin = pin
        account.pin_history.add(pin)


    def get_password(self, website, username):
        """
        Time complexity analysis goes here.
        """
        account = self.get_account(website, username)
        
        if account is None:
            raise ValueError("Account does not exist")
        
        if account.password is None:
            raise ValueError("Password is not set")
        
        return account.password
    
    def get_pin(self, website, username):
        account = self.get_account(website, username)
        
        if account is None:
            raise ValueError("Account does not exist")
        
        if account.pin is None:
            raise ValueError("Pin is not set")
        
        return account.pin


if __name__ == "__main__":
    """
    Write tests for your code here...
    """
    pm = PasswordManager(5)
    
    pm.set_password("A", "1", "abcd")
    pm.set_password("A", "2", "1234")
    
    try:
        pm.set_password("A", "1", "abcd")
    except ValueError as e:
        print(e)
        
    pm.set_password("A", "1", "1234")
    assert pm.get_password("A", "1") == "1234"
    assert pm.get_password("A", "2") == "1234"
    print("3.1 ok")

    try:
        pm.get_pin("A", "1")
    except ValueError as e:
        print(e)

    pm.set_pin("A", "1", 123)
    assert pm.get_pin("A", "1") == 123
    print("3.2 ok")
