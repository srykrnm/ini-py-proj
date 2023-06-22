
### FUNCTIONS ###

class Category:
    def __init__(self, category_name: str):
        self.name = category_name
        self.ledger = []
    def deposit(self, deposit_amount: int, description: str = "None"):
        self.deposit_det = {"amount": deposit_amount, "description": description}
        self.ledger.append(self.deposit_det)
    def withdraw(self, withdraw_amount: int, description: str = "None"):
        if self.check_funds(withdraw_amount):
            self.withdraw_det = {"amount": (0 - withdraw_amount), "description": description}
            self.ledger.append(self.withdraw_det)
            return True
        else:
            return False
    def get_balance(self):
        self.balance = 0
        for i in self.ledger:
            self.balance += i["amount"]
        return self.balance
    def transfer(self, transfer_amount: int, dest_cat):
        if self.check_funds(transfer_amount):
            self.withdraw(transfer_amount, f"Transfer to [{dest_cat.name} Budget Category]")
            dest_cat.deposit(transfer_amount, f"Transfer from [{self.name} Budget Category]")
            return True
        else:
            return False
    def check_funds(self, check_amount):
        if check_amount < self.get_balance():
            return True
        else:
            return False
    def __str__(self):
        title = f"\n{'*' * ((34 - len(self.name)) // 2)}{self.name}{'*' * ((34 - len(self.name)) // 2)}\n\n"
        items = ""
        total = 0
        for item in self.ledger:
            if len(item['description']) > 23:
                description = f"{item['description'][:23]}..."
            else:
                description = item['description']
            amount = item['amount']
            items += f"{description.ljust(27)}{amount:>7.2f}\n"
            total += amount
        output = title + items + f"Total: {total:.2f}\n"
        return output    

def create_spend_chart(catagories: list):
    withdrawal_dict = {}
    chart = ""
    total_withdrawal = 0
    for i in catagories:
        withdrawal = 0 - sum( j["amount"] for j in i.ledger if j["amount"] < 0 )
        total_withdrawal += withdrawal
        withdrawal_dict[i.name] = withdrawal
    percentages = [ int( (i / total_withdrawal) * 100 ) for i in withdrawal_dict.values()] 
    rounded_heights = [10 * (percentage // 10) for percentage in percentages]
    chart += "\nPercentage spent by category\n----------------------------\n\n"
    for percentage in range(100, -10, -10):
        chart += f"{str(percentage).rjust(3)}| "
        for height in rounded_heights:
            if height >= percentage:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"     
    chart += "    " + "-" * (3 * len(catagories) + 1) + "\n"
    max_category_length = max(len(category.name) for category in catagories)
    for i in range(max_category_length):
        chart += "     "
        for category in catagories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    return chart


### MAIN ###

food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")
education = Category("Education")
sports = Category("Sports")

food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restuarent and more food")

clothing.deposit(1000, "Initial deposit")
clothing.withdraw(10.15, "groceries")
clothing.withdraw(15.89, "restuarent and more food")
clothing.transfer(50.15, food)

entertainment.deposit(1500, "Initial deposit")
entertainment.withdraw(15.15, "netfix")
entertainment.withdraw(12.89, "hulu")
entertainment.transfer(100.15, education)

education.deposit(10000, "Initial deposit")
education.withdraw(40.15, "coursera")
education.withdraw(1500.89, "udemy")
education.transfer(507.5, food)

sports.deposit(1000, "Initial deposit")
sports.withdraw(32.15, "dumbells")
sports.withdraw(5.89, "stretchbands")
sports.transfer(500.15, education)

### OUTPUT ###

print(food, clothing, education, entertainment, sports)
print(create_spend_chart([food, clothing, education, entertainment, sports]))

### END ###