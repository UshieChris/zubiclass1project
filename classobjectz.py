class Budget():
    def __init__(self, categories, balances):
        self.categories = categories
        self.categories_balance = {}
        
        for i in range(len(categories)):
            self.categories_balance[categories[i]] = balances[i]
            
            
            

    def deposit(self, category):
        send = int(input("how much do you want to sent?>>>"))
        self.categories_balance[category] += send
        print(F'your balance is {self.categories_balance[category]}')

    def withdraw(self, category):
        receive = int(input("How much do you want to withdraw?>>>"))
        if self.categories_balance[category] >= receive:


            self.categories_balance[category] -= receive
                  
            print(F'your balance is {self.categories_balance[category]}')
        else:
            print("your balance is too low, you can't withdraw")
            exit

      
        
    def get_balance(self, category):
        print(self.categories_balance[category])

    def transfer(self, source_category, destination_category):
        amount = int(input("How much do you want to transfer?>>>"))
        if self.categories_balance[source_category] >=amount:
            self.categories_balance[source_category] -= amount
            self.categories_balance[destination_category] += amount
            print("Transfer Successful")
        else:
            print("your balance is too low your can't transfer")
            exit 
categories_list = ['food','clothing','enter']
balance_list = [2,4,0]

prove = Budget(categories_list, balance_list)
prove.withdraw(categories_list[1])
prove.deposit(categories_list[1])

prove.get_balance('food')
prove.get_balance('clothing')
prove.transfer('food','enter')
prove.get_balance('enter')