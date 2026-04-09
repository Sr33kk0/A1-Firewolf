from data_structures.array_sorted_list import ArraySortedList
from data_structures.array_list import ArrayList

class Account:
    def __init__(self, website, username, max_password):
        self.website = website
        self.username = username
        self.password_history = ArrayList()
        self.password = None

class PasswordManager:
    def __init__(self, max_passwords_per_account):
        self.accounts = ArraySortedList()
        self.max_passwords = max_passwords_per_account
    
    def get_account(self, website, username):
        account = Account(website, username, None)
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
                raise ValueError("Password has already been used before")
            
        account.password = password
        account.password_history.append(password)

    def set_pin(self, website, username, pin):
        pass


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
        pass


if __name__ == "__main__":
    """
    Write tests for your code here...
    """
    pass