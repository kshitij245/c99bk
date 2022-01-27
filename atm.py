class atm():
    def _init_(self,atmcardNumber,pinNumber):
        def balanceInquiry(self):
            print("your bank balance is 50000")

        def amountWithdrawal(self,amountWithdrawn,TotalAmount):
            amountWithdrawn= input("enter the amount to be withdrawn:")
            TotalAmount= 50000-amountWithdrawn
            print(TotalAmount,amountWithdrawn)

def enquiry():
    a = int(input("enter 1 or 2 for inquiry "))
    if(a==1):
        balanceInquiry()
    elif(a==2):
        amountWithdrawal()
    else:
        print("enter a valid number")