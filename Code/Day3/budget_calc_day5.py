import math

class Category:
  def __init__(self, name):
    self.ledger = []
    self.balance = 0
    self.name = name
    self.spent = 0 

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for i in range(len(self.ledger)):
      items += f"{self.ledger[i]['description'][0:23]:23}" + \
      f"{self.ledger[i]['amount']:>7.2f}" + "\n"
      total += self.ledger[i]['amount']
    output = title + items + "Total: " + str(total)
    return output

  def deposit(self, amount, description=""):
    self.balance = self.balance + amount
    self.ledger.append({"amount": amount, "description": description})

  def check_funds(self, amount): 
    if self.balance < amount:
      return False
    else:
      return True

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.balance = self.balance - amount
      self.ledger.append({"amount": -amount, "description": description})
      self.spent += amount
      return True
    else: 
      return False
  
  def transfer(self, amount, other_category): 
    withdrawBool = self.withdraw(amount, "Transfer to " + str(other_category.name))
    if withdrawBool: 
      other_category.deposit(amount, "Transfer from " + str(self.name))
      return True
    else: 
      return False
      
  
  def get_balance(self):
    return self.balance
  

def create_spend_chart(categories):
  total_spend = 0
  percentages = []
  for i in range(len(categories)):
    total_spend += categories[i].spent
  for i in range(len(categories)):
    percent = math.floor((categories[i].spent / total_spend) * 10) * 10
    percentages.append(percent)
  txt = []
  txt.append("Percentage spent by category")
  for i in range(0,11,1):
    leftNum = (10 - i) * 10
    temp = ""
    if i == 0:
      temp += str(leftNum) + "| "
    elif i == 10:
      temp += "  " + str(leftNum) + "| "
    else:
      temp += " " + str(leftNum) + "| "
    for i in range(len(categories)):
      if percentages[i] >= leftNum:
        temp += "o  "
      else:
        temp += "   "
    txt.append(temp)
  txt.append("    " + "-" * (len(categories)*3 + 1))
  names = [c.name for c in categories]
  n = max(map(len,names))
  for i in range(n):
    s = " " * 4
    for name in names:
      s += " "
      s += name[i] if len(name) > i else " "
      s += " "
    txt.append(s + " ")
  return "\n".join(txt)
