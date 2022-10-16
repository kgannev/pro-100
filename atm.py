class Atm:
    def_init_(self,cardno, pin):
        self.cardno = cardno
        self.pin = pin
        
    def checkbalance(self):
        print("your balance is 50000")

    def withdrawal(self,amount):
        newbalance =50000-amount 
        print("you have withdraw amount"+amount)
        print("you remaining balance"+new balance)

def main():
    cardnumber = input("insert your card no-")
    pinno =input("pin no-")
    newuser =Atm(cardnumber,pinno)
    
    print("choose your activity")
    print("1.balanceinquery 2.withdrawal")
    activity = int(input("enter activity no"))

    if(activity ==1):
        newuser.checkbalance()
    elif(activity==2):
        amount = int(input("enter the amount"))
        newuser.withdrawal()
    else:
        print("enter valid no")

if _name_=="_main_":
    main()
