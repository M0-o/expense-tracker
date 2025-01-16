import math 


class Category:

    def __init__(self, name):
        self.ledger = []
        self.name= name 
    
    def __str__(self):
        stars = ((round((30 - len(self.name))/2))+1 )*'*'
        form = f"{stars}{self.name}{stars}\n"

        for expense in self.ledger:

            description = str(expense['description'])[:23]
            amount = f"{expense['amount']:.2f}"

            description_length = len(description)
            amount_length = len(amount)

            number_of_spaces = (30 - description_length - amount_length ) +1
            form+= description + " "*number_of_spaces + amount +'\n' 
            
           
        form += f'Total: {self.get_balance():.2f}'  
        
        return form + "\n"


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True 
        return False 

    def get_balance(self):
        total = 0
        for expense in self.ledger: 
            total += expense['amount']

        return total 

    def transfer(self, amount ,category):

        if self.check_funds(amount):
            self.withdraw(amount , f"Transfer to {category.name}")
            category.deposit(amount , f"Transfer from {self.name}" )
            return True

        return False 


    
    def check_funds(self, amount):
        return self.get_balance() >= amount

    def get_spent(self):
        return -sum([i['amount'] for i in self.ledger if i['amount'] < 0])




def create_spend_chart(categories):

    total = sum([category.get_spent() for category in categories])


    chart= "Percentage spent by category\n"

    for i in range(100,-10,-10):

        chart+=f"{i:3}| "
        for category in categories :
            
            percentage = round(category.get_spent()/total* 100) 

            if i <= percentage:
                chart += f"o{' '*2}"
            else: 
                chart += f"{' '*3}"
        chart+="\n"

    chart+=f'{" "*4}{"-"*len(categories)*3}-\n'

    max_length = max([len(category.name) for category in categories])

    for i in range(max_length):
        chart+=" "*3
        for category in categories:
            chart+=  " "*2 
            if i < len(category.name):
                chart+= category.name[i] 
            else :
                chart+= " "
        
        if i != max_length-1 : 
            chart+="  \n"

    return chart + "  "