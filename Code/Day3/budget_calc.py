class Category:
  def __init__(self, name):
    self.Ledger = []
    self.Balance = 0
    self.Name = name

  def __str__(self):
    for i in range(15):
      print("*", end="")

  def deposit(self, amount, description=""):
    self.Balance = self.Balance + amount
    self.Ledger.append({"amount": amount, "description": description})

  def check_funds(self, amount): 
    if self.Balance < amount:
      return False
    else:
      return True

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.Balance = self.Balance - amount
      self.Ledger.append({"amount": -amount, "description": description})
      return True
    else: 
      return False
  
  def transfer(self, amount, other_category): 
    withdrawBool = self.withdraw(amount, "Transfer to " + str(other_category.Name))
    if withdrawBool: 
      other_category.deposit(amount, "Transfer from " + str(self.Name))
      return True
    else: 
      return False
      
  
  def get_balance(self):
    return self.Balance
  
