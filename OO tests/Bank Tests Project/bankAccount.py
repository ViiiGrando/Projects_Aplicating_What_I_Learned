
class AccountBank:
    
     
    def __init__(self, balance = int, holder ='', active = False):
        self._titular = holder
        self._balance = balance
        self._active = active
        self._accounts =[]
    
   
    def __str__(self):
        return f'Holder: {self._titular}| Balance:R${self._balance} |Accounts: {self.list_accounts}'

    @property
    def active(self):
     return 'Accont open' if self._active else 'Account Closed'


    def activate_account(self):
        self._active = True


    @property
    def list_accounts(self):
      '''@property in Python is used to create methods that can be accessed as if 
     were attributes, allowing the logic of accessing and modifying an attribute to be encapsulated.
     its objective is to encapsulate the logic of accessing and modifying an attribute, making the 
     code easier to read'''
      return self._accounts 

account1 = AccountBank('Victor', 143)
account1.activate_account()
print(account1.active)


'''
******************
      PSs
*******************
@classmethod
Usage: Defines a method that belongs to the class, not a specific instance.
Purpose: Allow the method to operate on the class as a whole, rather than on an instance. 
It is useful for creating factory methods or for manipulating class attributes.

'''







