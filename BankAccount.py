def add_account(new_account):
    ##function adds an account to the list of bank accounts###
    # starting balance is $0
    from csv import writer

    filename = "bank.csv"
    with open(filename, "a+", newline="") as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow([new_account, 0])


def delete_account(account):
    ###function deletes a selected account###
    # returns erros message not_zero() if balance() is not 0
    import shutil
    import csv

    filename = "bank.csv"
    temp = "temp_bank.csv"

    with open(filename, "r") as csvFile:
        reader = csv.DictReader(csvFile)

        with open(temp, "w") as temp:
            fieldnames = ["acc_name", "balance"]
            writer = csv.DictWriter(temp, fieldnames=fieldnames)
            writer.writeheader()
            for line in reader:
                if line["acc_name"] == str(account):
                    next
                else:
                    writer.writerow(line)

    shutil.move(temp.name, filename)


def withdraw(account, ammount):
    ### function withfraws money from a selected account###
    # return error message not_enought() if fund not sufficient
    import shutil
    import csv

    filename = "bank.csv"
    temp = "temp_bank.csv"

    with open(filename, "r") as csvFile:
        reader = csv.DictReader(csvFile)

        with open(temp, "w") as temp:
            fieldnames = ["acc_name", "balance"]
            writer = csv.DictWriter(temp, fieldnames=fieldnames)
            writer.writeheader()
            for line in reader:
                if line["acc_name"] == str(account):
                    line["balance"] = int(line["balance"]) - int(ammount)
                    writer.writerow(line)
                else:
                    writer.writerow(line)

    shutil.move(temp.name, filename)


def top_up(account, ammount):
    ### function tops up a selected account###
    # shutil to merge temp into the old file
    import shutil
    import csv

    filename = "bank.csv"
    temp = "temp_bank.csv"

    with open(filename, "r") as csvFile:

        reader = csv.DictReader(csvFile)

        with open(temp, "w") as temp:

            fieldnames = ["acc_name", "balance"]
            writer = csv.DictWriter(temp, fieldnames=fieldnames)
            writer.writeheader()
            for line in reader:
                if line["acc_name"] == str(account):
                    line["balance"] = int(line["balance"]) + int(ammount)
                    writer.writerow(line)
                else:
                    writer.writerow(line)

    shutil.move(temp.name, filename)


def record_action(account, action):
### function records when a bank account was opened or closed###
    from datetime import datetime
    dateTimeObj = datetime.now()
    with open('record.txt', 'a') as record:
        time_stamp = ('\n'+str(dateTimeObj)+' '+str(account)+' '+str(action))
        record.writelines(time_stamp)


def record_transaction(account,sum,action):
### function records all transactions in the bank###
    from datetime import datetime
    dateTimeObj = datetime.now()
    with open('record.txt', 'a') as record:
        time_stamp = ('\n'+str(dateTimeObj)+' '+str(account)+' $'+str(sum)+" "+str(action))
        record.writelines(time_stamp)



def balance(account):
    ### function returns the balance of selected account###
    import csv

    filename = "bank.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        x = None
        for line in reader:
            if line["acc_name"] == str(account):
                x = line["balance"]
    return x


def list_accounts():
    ### function lists all accounts in the bank###
    import csv

    filename = "bank.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        print("\nThe current status of your accounts: \n")
        for line in reader:
            print(line["acc_name"] + "\t\t$" + line["balance"])


def exist(account):
    ### function checks if a selected account exist###
    # true is exist / false otherwise
    import csv

    flag = False
    filename = "bank.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            if line["acc_name"] == str(account):
                flag = True
    return flag

def print_record():
    ### function prints the record of all transactions in the bank###
    with open('record.txt','r') as f:
        for line in f:
            print(line.strip())



def not_empty():
    ### function returns an error message 'the balance not zero###
    print(
        "\nThe balance of the selected account is not zero. Withdraw your money and try again\n"
    )


def not_enought():
    ### function returns error 'not enough money'
    print("\nThere are no sufficient funds in the selected account\n")


def already_exists():
    ### return error message 'account already exist###
    print("\nThe selected account already exists. Please try again.\n")


def doesnt_exist():
    ### return error message 'account doestn exist###
    print("\nThe selected account does not exist. Please try again.\n")


# start of the program
ch = ""
num = 0


while ch != 8:
    # system("cls");
    print("\n\tMAIN MENU")
    print("\t*********")
    print("1. ADD ACCOUNT")
    print("2. CLOSE AN ACCOUNT")
    print("3. WITHDRAW MONEY")
    print("4. DEPOSIT MONEY")
    print("5. LIST ALL ACCOUNTS")
    print("6. PRINT ALL TRANSACTIONS")
    print("7. EXIT")
    print("Select Options 1-7 ")
    ch = input()
    # system("cls");

    if ch == "1":
        acc = input("Type the name of an account you want to open ")
        if exist(acc) == False:
            add_account(acc)
            record_action(acc,'account was opened')
        else:
            already_exists()

    elif ch == "2":
        acc = input("Type the name of an account you want to close ")
        if exist(acc) == False:
            doesnt_exist()
        elif int(balance(acc)) != 0:
            not_empty()
        else:
            delete_account(acc)
            record_action(acc,'account was closed')

    elif ch == "3":
        acc = input("Which account you want to withdraw money from? ")
        money = input("How much money do you want to withdraw? ")
        if exist(acc) == False:
            doesnt_exist()
        elif int(balance(acc)) <= int(money):
            not_enought()
        else:
            withdraw(acc, money)
            record_transaction(acc,money,'withdrawn')

    elif ch == "4":
        acc = input("Which account you want to deposit money to? ")
        money = input("How much money do you want to deposit? ")
        if exist(acc) == False:
            doesnt_exist()
        else:
            top_up(acc, money)
            record_transaction(acc,money,'deposited')

    elif ch == "5":
        list_accounts()

    elif ch == "6":
        print_record()

    elif ch == "7":
        print("See you next time!")
        break
    else:
        print("Invalid choice")

    ch = input("\nPress any key to continue ")
