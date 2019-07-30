import time
import json

class Account:
    transtype=["Append","Deposit","Withdrawal","Query"]

    def __init__(self,first,last,city,state,account,balance):
        self.first=first
        self.last=last
        self.city=city
        self.state=state
        self.account=account
        self.balance=balance
        self.transactionID=0
        self.data={}
        self.data['transactions']=[]
        self._transaction(0)


    def _transaction(self,type):
        self.transactionID+=1
        self.data['transactions'].append({
            'Trans': self.transactionID,
            'Date': time.strftime("%d/%m/%y"),
            'Hour': time.strftime("%H:%M:%S"),
            'Operation': type})
        self._writeFile();

    def _writeFile(self):
        with open(str(self.account)+".json", 'w') as file:
            json.dump(self.data, file, indent=4)


    def _openFile(self):
        with open(str(self.account)+".json") as file:
             return json.load(file)


    def make_deposit(self,amount):
        if amount > 0:
            try:
                self.balance+=amount
                self._transaction(1)
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
                    self._transaction(2)
                except TypeError:
                    print("You need to insert a Integer")
                except Exception:
                    print("An error has ocurred")
            else:
                print("The amout needs to be greater than Cero")
        else:
            print("Alert: The Amount is greater that Current Balance")

    def make_query(self):
        try:
            info=self._openFile()
            values=info['transactions'][0]
            print(values['Date'])
            print("\n\n\t\t\t** CitiBanamex **\t\n")
            print(f'\t\t\t\t{self.city} , {self.state}\n')
            print("Date:\t\tHour:\t\tTransaction ID:")
            print(f'{values["Date"]}\t{values["Hour"]}\t\t\t{values["Trans"]}\n')
            print("Account Number: "+str(self.account))
            print(f'Owner: {self.first} {self.last}')
            print("Operation: "+str(self.transtype[values["Operation"]]))
            print("\n\t === BALANCE STATUS ===\n")
            print(f'Current Balance: \t $ {self.balance}')
            self._transaction(3)
        except IndexError:
            print("Error: You has provided an Invalid id ")



cuenta1=Account("Omar","Ayard","ZAPOPAN","JAL","000AAA1",100)
cuenta1.make_deposit(50)
cuenta1.make_withdrawal(10)
cuenta1.make_query()
print(40*'*')
cuenta2=Account("Othoniel","Rivera","JIQUILPAN","MICH","000BBB2",200)
cuenta2.make_deposit(100)
cuenta2.make_withdrawal(1000)
cuenta2.make_query()