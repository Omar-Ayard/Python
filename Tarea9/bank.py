import time

class Account:
    transtype=["Deposit","Withdrawal","Query"]

    def __init__(self,first,last,city,state,account,balance):
        self.first=first
        self.last=last
        self.city=city
        self.state=state
        self.account=account
        self.balance=balance
        self.transactionID=0
        self.trasactions=[[]]

    def _transaction(self,type):
        self.transactionID+=1
        self.trasactions.append([self.transactionID,
                                 time.strftime("%d/%m/%y"),
                                 time.strftime("%H:%M:%S"),
                                 type])


    def make_deposit(self,amount):
        if amount > 0:
            try:
                self.balance+=amount
                self._transaction(0)
            except TypeError:
                print("You need to insert a Integer")
            except Exception:
                print("An error has ocurred")
        else:
            print("You can make a deposit less than Cero 0")

    def make_withdrawal(self,amount):
        if amount <= self.balance:
            if amount > 0:
                try:
                    self.balance-=amount
                    self._transaction(1)
                except TypeError:
                    print("You need to insert a Integer")
                except Exception:
                    print("An error has ocurred")
            else:
                print("The amout needs to be greater than Cero")
        else:
            print("Alert: The Amount is greater that Current Balance")

    def make_query(self,id):
        try:
            print("\n\n\t\t\t** CitiBanamex **\t\n")
            print(f'\t\t\t\t{self.city} , {self.state}\n')
            print("Date:\t\tHour:\t\tTransaction ID:")
            print(f'{self.trasactions[id][1]}\t{self.trasactions[id][2]}\t\t\t{self.trasactions[id][0]}\n')
            print("Account Number: "+str(self.account))
            print(f'Owner: {self.first} {self.last}')
            print("Operation: "+str(self.transtype[self.trasactions[id][3]]))
            print("\n\t === BALANCE STATUS ===\n")
            print(f'Current Balance: \t $ {self.balance}')
            self._transaction(2)
        except IndexError:
            print("Error: You has provided an Invalid id ")



cuenta1=Account("Omar","Ayard","ZAPOPAN","JAL","000AAA1",5)
cuenta1.make_deposit(100)
time.sleep(10)
cuenta1.make_withdrawal(3)

cuenta1.make_query(1)
cuenta1.make_query(2)