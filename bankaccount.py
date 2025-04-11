class BankAccount:
  def __init__(self, username, balance = 0):
    self.username = username
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit {amount} successful! New balance: {self.balance}")
  
  def withdraw(self, amount):
      self.balance -= amount
      print(f"Withdrawal {amount} successful! New balance: {self.balance}")

  def check_balance(self):
    print(f"Account: {self.username}, Current balance: {self.balance}")