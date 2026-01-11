class Account:
    def __init__(self, balance=0):
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
        
    def withdraw(self, n):
        self._balance -= n 
        
def main():
    account = Account()
    print(f"balance: {account.balance}")
    account.deposit(100)
    account.withdraw(50)
    print(f"balance: {account.balance}")
    
    
    
if __name__ == "__main__":
    main()