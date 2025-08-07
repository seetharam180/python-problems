import random
class Bank:
    T_Holders=[]
    def create_account(self):
        Holder_details={}
        Holder_details['name']=input("Enter name:")
        Holder_details['mobile_no']=input("Enter mabile no:")
        Holder_details['Aadharno']=input("Enter Aadharno:")
        data=random.randint(100000000000,999999999999)
        # while True:
        #     if data not in Bank.T_Holders['Accno']:
        #         Holder_details['Accno']=data
        #         break
        Holder_details['Accno']=data
        Holder_details["Acctype"]=input("Enter Acctype:zero/savings--->")
        while True:
            if Holder_details['Acctype']=='savings':
                balance=input("Deposit 1000 rupess...")
                if int(balance)>=1000:
                    Holder_details['balance']=balance
                    break
            elif Holder_details['Acctype']=='zero':
                balance=input("Deposit 500 rupees....")
                if int(balance)>=500:
                    Holder_details['balance']=balance
                    break
        Bank.T_Holders.append(Holder_details)
        print(Bank.T_Holders)
    def deposit(self):
        Accno=input("Enter Account number:")
        for x in Bank.T_Holders:
            if int(Accno)==x['Accno']:
                deposit_amount=input("Enter amount to deposit:")
                bal=x['balance']
                x['balance']=int(bal)+int(deposit_amount)
                print(f"Your Balance:{x['balance']}")
            else:
                print("You Don't have an account Create first")
    def withdraw(self):
        Accno=input("Enter Account number:")
        for x in Bank.T_Holders:
            if int(Accno)==x['Accno']:
                withdraw_amount=input("Enter amount to withdraw:")
                bal=x['balance']
                if int(withdraw_amount)<=bal:
                    x['balance']=int(bal)-int(withdraw_amount)
                    print(f"Your Balance:{x['balance']}")
                else:
                    print(f"Insufficient balance")
            else:
                print("You Don't have an account Create first")
                
b=Bank()
b.create_account()
b.deposit()
b.withdraw()


