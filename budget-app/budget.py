class Category:
  # Constructor
  def __init__(self, name):
      self.name = name
      self.ledger = []

  def __str__(self):
      title = f"{self.name:*^30}" + "\n"
      item_list = ""
      total = 0
      for i in self.ledger:
          item_list += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + "\n" 
          total += i['amount']
      output = title + item_list + "Total: " + str(total)
      print(output)
      return output


  # Deposit method
  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})

  # Withdraw method
  def withdraw(self, amount, description=""):
      if (self.check_funds(amount)):
          self.ledger.append({"amount": -amount, "description": description})
          return True # Withdrawal successful
      return False # Insuficient funds

  # get balance method - return current state of budget
  def get_balance(self):
      balance = 0
      for i in self.ledger:
          balance += i["amount"]
      return balance

  # transfer method
  def transfer(self, amount, category):
      if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {category.name}")
          category.deposit(amount, f"Transfer from {self.name}")
          return True
      return False


  # check funds method
  def check_funds(self, amount):
      if amount > self.get_balance():
          return False # Amount is greater than balance
      else:
          return True # Amount is equal or less than balance

  def get_spending(self):
      total = 0
      for item in self.ledger:
          if item["amount"] < 0:
              total += item["amount"]
      return total


def create_spend_chart(categories):
  spending = []
  # spending per category
  for category in categories:
      spending.append(category.get_spending())
  
  # % per category
  total_spending = sum(spending)
  percentages = [(spending / total_spending) * 100 for spending in spending]
  
  # Chart visualization
  header = "Percentage spent by category\n"
  chart = ""
  
  # Counting from 100 to 0 with - 10 steps
  for line in range(100, -1, -10):
      # adds y axis 
      chart += str(line).rjust(3) + '|'
      # adds filler of graph based on percentage
      for percent in percentages:
          if percent >= line:
              chart += " o "
          else:
              chart += "   "
      chart += " \n"
  
  # Adds footer
  footer = '    ' + '-' * ((3 * len(categories)) + 1) + '\n'
  
  # Adds description starts with 5 white spaces , 2 white spaces between cat and end
  # Adds white spaces to align all category length
  desc = [category.name for category in categories]
  maximum_len = max(len(name) for name in desc)
  desc = [name.ljust(maximum_len) for name in desc]
  
  # transpose the list of descriptions 
  for i in zip(*desc):
      footer += "    " + "".join(name.center(3)   for name in i) + ' \n'
  
  return (header + chart + footer).rstrip('\n')
  








