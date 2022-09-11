print("WELCOME TO THE BANK OF CFG")


def password_validation(number):
    if not password == 1989:
        raise ValueError("PIN NUMBER INCORRECT")
    return password


isSuccessful = False

try:
    password = int(input("\nPLEASE ENTER YOUR PIN NUMBER: "))
    password_validation(password)

except ValueError as ve:
    print(ve)
    try:
        password = int(input("\nPLEASE ENTER YOUR PIN NUMBER: "))
        password_validation(password)

    except ValueError as ve:
        print(ve)
        try:
            password = int(input("\nPLEASE ENTER YOUR PIN NUMBER: "))
            password_validation(password)

        except ValueError as ve:
            print(ve)

        else:
            isSuccessful = True
            print("PIN NUMBER CORRECT")

    else:
        isSuccessful = True
        print("PIN NUMBER CORRECT")

else:
    isSuccessful = True
    print("PIN NUMBER CORRECT")

finally:
    if isSuccessful:

        def withdrawal_validation(amount):
            if not withdrawal <= account_balance:
                raise ValueError("WITHDRAWAL NOT GRANTED \nNOT ENOUGH FUNDS")
            return account_balance


        isMoney = False

        try:
            withdrawal = int(input("PLEASE ENTER WITHDRAWAL AMOUNT: £"))
            account_balance = 100
            balance = account_balance - withdrawal
            withdrawal_validation(balance)

        except ValueError as ve:
            print(ve)

        else:
            isMoney = True
            print('WITHDRAWAL GRANTED \nYOUR REMAINING BALANCE IS = £{}'.format(balance))

    else:
        print("ACCESS DENIED")


# Writen alternative with if statements in attempt to make "easier" for testing - this failed - run this for tests.


# print("WELCOME TO THE BANK OF CFG")
# password = int(input("\nPLEASE ENTER YOUR PIN NUMBER: "))
#
#
# def password_validation(password):
#     if password == 1989:
#         print("PIN NUMBER CORRECT")
#         count = 4
#     elif password != 1989:
#         count = 1
#         while count < 3:
#             if password == 1989:
#                 print("PIN NUMBER CORRECT")
#                 count = 4
#             else:
#                 print("PIN NUMBER INCORRECT. TRY AGAIN")
#                 password = int(input("\nPLEASE ENTER YOUR PIN NUMBER: "))
#                 count += 1
#         else:
#             if password != 1989:
#                 print("PIN NUMBER INCORRECT ON THIRD ATTEMPT \nACCESS DENIED")
#             else:
#                 print("ACCESS GRANTED")
#     else:
#         print("ACCESS GRANTED")
#     return True
#
#
# password_validation(password)
#
# if password:
#     def withdrawal_validation(amount):
#         if not withdrawal <= account_balance:
#             raise ValueError("WITHDRAWAL NOT GRANTED \nNOT ENOUGH FUNDS")
#         return withdrawal
#
#
#     isMoney = False
#
#     try:
#         withdrawal = int(input("PLEASE ENTER WITHDRAWAL AMOUNT: £"))
#         account_balance = 100
#         balance = account_balance - withdrawal
#         withdrawal_validation(balance)
#
#     except ValueError as ve:
#         print(ve)
#
#     else:
#         isMoney = True
#         print('WITHDRAWAL GRANTED \nYOUR REMAINING BALANCE IS = £{}'.format(balance))
