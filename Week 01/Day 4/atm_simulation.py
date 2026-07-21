#//program for atm simulation
print("== WELCOME TO ATM Services==")
correct_pin = 1234
balance = 10000
entered_pin = int(input("Enter your 4-digit PIN: "))
if entered_pin == correct_pin:
    print("Login Successful!")
else:
    print("Incorrect PIN!")

print("\n1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice = int(input("Choose an option: "))

if choice == 1:
    print("Your Balance is:", balance)
    
elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit Successful!")
    print("New Balance:", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful!")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance!")

elif choice == 4:
    print("Thank you for using our ATM.")
else:
    print("Invalid Option!")