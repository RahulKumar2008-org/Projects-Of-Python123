print("Your Bank")
Name=input("Enter your good name:")
Age=int(input("Enter your age:"))
Contactnumber=input("Enter your Contact number:")
DateofBirth=input("Enter your DOB:")



if Age >= 18: # Verification Stage
     print("Welcome Dear ",Name)


     class Account_details:
      def __init__(self,Account_number,Upi_pin,Balance,IFSC_CODE):
          self.Account_number=Account_number
          self.Upi_pin=Upi_pin
          self.Balance=Balance
          self.IFSC_CODE=IFSC_CODE

     class Deposite(Account_details):
      def __init__(self,Account_number,Upi_pin,Balance,IFSC_CODE,deposite_cash):
          super().__init__(Account_number,Upi_pin,Balance,IFSC_CODE)
          self.deposite_cash=deposite_cash

        

   
      def Balancedeposite(self):
         return  self.deposite_cash + self.Balance

      def interest_rate(self):
         return self.Balance + 18.63

     class Withdraw(Deposite):
      def __init__(self,Account_number,Upi_pin,Balance,IFSC_CODE,deposite_cash,withdraw_cash):
          super().__init__(Account_number,Upi_pin,Balance,IFSC_CODE,deposite_cash)   
          self.withdraw_cash=withdraw_cash
        
      def cashwithdraw(self):
          return self.Balance - self.withdraw_cash

      def display_info(self):
          print("Account_number=",self.Account_number)
          print("Upi_pin=",self.Upi_pin)
          print("Balance=",self.Balance)
          print("IFSC_CODE=",self.IFSC_CODE)
          print("Deposite_cash=",self.deposite_cash)
          print("Withdraw_cash=",self.withdraw_cash)
          print("Interest_rate=",self.interest_rate())

     obj3=Withdraw("ats1234mnb","785624",1000000,"Nmst23",300000,100000)
     obj3.display_info()
     print( "Depositecash=",obj3.Balancedeposite())
     print("Withdrawcash=",obj3.cashwithdraw())


     


          
          

      
    



