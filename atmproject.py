user_information={"name":"sai nikhil",
                  "mobile number":"",
                  "ATM pin":"6600",
                  "balance":47238,
                  "Transaction History":[]
                  } #user data
print("please insert ATM card:")
remaining_attempts=3
while remaining_attempts > 0:
    pin=input("enter 4 digits ATM PIN")
    if len(pin)==4:
        if pin in user_information['ATM pin']:
            print("select")
            print("1.withdraw")
            print("2.deposit")
            print("3.balance enquiry")
            serv=int(input())
            if serv==1:
                withdraw_amount=int(input())
                if withdraw_amount>=user_information['balance']:
                    balance-=withdraw_amount
            elif serv==2:
                deposit_amount=int(input("enter deposit amount"))
                user_information['balance']+=deposit_amount
                print("balance amount: after deposit",user_information['balance'])
            elif serv==3:
                print("balance:",user_info['balance'])        
        else:
            print("Invalid pin")
            remaining_attempts-=1
            if remaining_attempts>0:
                print(f"Invalid pin entered and you have{remaining_attempts} attempts")
            else:
                print("you've run out of attempts,your ATM card is blocked")
                break
    else:
        print("please enter 4 digit password")
            
            

    


