

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
        self.trasactions=[[]]
        self.data={}
        self.data['transactions']=[]
        self._transaction(0)