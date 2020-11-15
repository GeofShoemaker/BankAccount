class BankAccount:

  #Imports randint method from random class (for RNG)
  from random import randint

  #Declares and initializes __account_number with a random 8 digit number
  __account_number = randint(0,99999999)

  #_routing_number declaration and initialization
  _routing_number = 891746984

  #___balance declaration and initialization
  __balance = 0

  #Sets up constructor, accepts string "full_name" and assigns Me.__full_name to it
  def __init__(Me, full_name):
    Me.__full_name = full_name

  #Deposit function/method
  def deposit(Me, amt):

    #Adds dep_amt to account balance
    Me.__balance += amt 

    #Me.prints the confirmation message
    print(f"Amount Deposited: ${round(Me.__balance,2)}")

  #Withdraw function/method
  def withdraw(Me, amt):
    #Withdraws and Me.prints amount withdrawn if valid amount
    if amt<=Me.__balance:
      Me.__balance-=amt
      print(f"Amount Withdrawn: ${amt}")
      return
    #Charges overdraft fee and Me.prints notice
    print("Insufficient funds. ")
    amt-=10

  #get_balance function/method, Me.prints and returns account's balance
  def get_balance(Me):
    print(f"Hello, {Me.__full_name}! Your balance is ${Me.__balance}")
    return Me.__balance
  
  #add_interest function/method
  def add_interest(Me):
    Me.__balance*=1.00083
  
  #print_receipt function/method
  def print_receipt(Me):
    print(f"{Me.__full_name}")                                #Name
    print(f"Account No.: ****{str(Me.__account_number)[4:]}") #Account Number
    print(f"Routing No.: {Me._routing_number}")               #Routing Number
    print(f"Balance: ${Me.__balance}")                        #Balance
my_account = BankAccount("Geof Shoemaker")
my_account.deposit(416.32)
my_account.print_receipt()