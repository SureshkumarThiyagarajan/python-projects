
print("Welcome to my Atm")

user_balance = 1000

print("Account Balance: " + str(user_balance)) 

user_pin = "1234"

entered_pin = input("Please Enter your atm pin: ")

while user_pin == entered_pin:
    atm_on = True
    if atm_on == True:
        print("Main menu:")
        selection_list = ["1. Check Balance","2. Deposit Money", "3. Withdraw Money", "4. exit"]
    for items in selection_list:
        print(items)
    else:
        entered_choice = int(input("Enter your Choice: "))
        if entered_choice == 1:
            print("Available Balance: " + str(user_balance))
        elif entered_choice == 2:
            deposited_amount = int(input("please add money: "))
            print("Available Balance: " + str(deposited_amount + user_balance))
        elif entered_choice == 3:
            withdrawal_amount = int(input("please enter your withdrawal amount: "))

            if (user_balance >= withdrawal_amount) & (withdrawal_amount >= 500) :
                print("Withdrawal Successful & Please collect your amount")
                print("Available Balance: " + str(user_balance - withdrawal_amount))
            elif withdrawal_amount < 500:
                print("please enter amount greater than 500")
            elif user_balance< withdrawal_amount:
                print("Balance is insufficient")
        elif entered_choice ==4:

            print("Exiting the Atm Good bye!")
            atm_on = False
            break
        else:
            print("Invalid option!")
                
else:
    atm_on = False
    print("Please enter correct pin")


