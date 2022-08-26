import mysql.connector as connector
import random
import math

connect = connector.connect(host="LocalHost", user="root", passwd="skyrex", database="bank3")
cursor = connect.cursor()
# querry = "SELECT * FROM hospital"
# cursor.execute(querry)
# results = cursor.fetchall()
# for i in results:
#     print(i)
# q2 = "SELECT hospital_id FROM hospital AS a WHERE a.name ='REMEDYREPACK INC.' AND a.license_no = 67968076;"
# querr2 = "SELECT * FROM hospital WHERE name = 'REMEDYREPACK INC.'"
# cursor.execute(querr2)
# r = cursor.fetchall()
# for i in r:
#     print(i)
print()
print()

# cursor.execute(q2)
# r = cursor.fetchall()
# # print(r)
# for i in r:
#     for j in i:
#         print(j)

#
# cursor.execute("SELECT * FROM customer;")
# for i in cursor.fetchall():
#     print(i)
def transaction_id_generator():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(8):
        index = math.floor(random.random() * 10)
        random_str += str(index)
    return int(random_str)


def check_customer_info(user_id, password):
    # q = f"SELECT EXISTS(SELECT * FROM user_info WHERE user_id = {user_id} , AND password = {password});"
    q = f"SELECT EXISTS(SELECT * FROM cust_login_info WHERE user_id={user_id});"
    cursor.execute(q)
    res = int

    for i in cursor.fetchall():
        for j in i:
            res = j
    # print(res)
    return res


# cursor.execute("SELECT * FROM emp_login_info")
# for i in cursor.fetchall():
#     print(i)

def check_admin_info(user_id, password):
    q = f"SELECT EXISTS(SELECT * FROM emp_login_info WHERE user_id={user_id});"
    cursor.execute(q)
    # print(cursor.fetchall())
    res = int

    for i in cursor.fetchall():
        for j in i:
            res = j
    # print(res)
    return res


def account_number_generator():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(index)
    return int(random_str)

# print(account_number_generator())


def user_id_generator():
    return account_number_generator()


def password_generator():
    passw = ["ft[[64Du", "hz<>98DU", "tyDY98", "moCK78", "UYin89"]
    return passw[int(random.randrange(0,4,1))]


def pin_generator():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(4):
        index = math.floor(random.random() * 10)
        random_str += str(index)
    return int(random_str)

# print(pin_generator())
def employee_id_generator():
    return account_number_generator()
#
#
# print(password_generator())

#
# cursor.execute("SELECT * FROM customer WHERE name = 'deepak';")
# for i in cursor.fetchall():
#     print(i)



# function to deposit money.





# UI STARTS
print(""""  *****************   """)

print("Welcome To Bank Of Paradis")
print()

user_input = int()

while(user_input != 3):
    print(""""  *****************   """)
    print("Log in as:")
    print("1: Customer")
    print("2: Admin")
    print("3: Exit")
    print()

    user_input = int(input("Enter 1, 2, 3: "))
    if (user_input == 1):
        user_id = int(input("Enter your user id: "))
        password = input("Enter your password: ")
        result = check_customer_info(user_id, password)
        # while result == False:
        #     user_id = int(input("Enter user id: "))
        #     password = (input("Enter your password: "))
        #     result = check_customer_info(user_id, password)
        #     if(result == 0):
        #         print("Invalid credentials")
        while(result == False):
            print("Invalid credentials.")
            user_id = int(input("Enter user id: "))
            password = (input("Enter your password: "))
            result = check_customer_info(user_id, password)
            if(result == 1):
                break

        # querry_account_number = "SELECT account_number FROM cust_login_info AS a WHERE a.user_id = {0}" \
        #                         "AND a.password = {1}".format(user_id, password)
        querry_account_number = "SELECT acc_no from cust_login_info AS a WHERE a.user_id = {0};".format(user_id)

        cursor.execute(querry_account_number)
        result = cursor.fetchall()
        account_number = 0
        for i in result:
            for j in i:
                account_number = j

        name = str
        cursor.execute("SELECT name FROM customer WHERE acc_no = {0};".format(account_number))
        for i in cursor.fetchall():
            for j in i:
                name = j
        print()
        print("Welcome {0}".format(name))

        print()
        option = int()
        while option != 7:

            print(""""  *****************   """)
            print("Please select a option")
            print("1: Deposit")
            print("2: Withdraw")
            print("3: Change Pin")
            print("4: Check Balance")
            print("5: View transactions")
            print("6: Transfer money")
            print("7: Exit")
            print()

            option = int(input("Enter here: "))

            if option == 1:  # deposit


                current_amount = 0
                cursor.execute("SELECT balance FROM customer AS a WHERE a.acc_no = {0};".format(account_number))
                for i in cursor.fetchall():
                    for j in i:
                        current_amount = int(j)
                print()

                print("Current amount is: {0}".format(current_amount))

                deposit_amount = int(input("Enter amount to be deposited: "))
                current_amount += deposit_amount

                cursor.execute("UPDATE customer SET balance = {0} WHERE acc_no = {1};"
                               .format(int(current_amount), account_number))
                connect.commit()
                print()
                print("Amount {0} has been credited to your account, avaialable balance is {1}"
                      .format(deposit_amount, current_amount))


            elif option == 2:  # withdraw
                current_amount = 0
                cursor.execute("SELECT balance FROM customer AS a WHERE a.acc_no = {0};".format(account_number))
                for i in cursor.fetchall():
                    for j in i:
                        current_amount = int(j)
                print()
                print("Available balance is: {0} ".format(current_amount))
                withdraw_amount = int(input("Enter amount to be withdraw: "))
                while withdraw_amount > current_amount:
                    print("Withdrawl amount cannot be > avaialble amount")
                    withdraw_amount = int(input("Enter amount to be withdraw: "))
                # 4416458
                current_amount -= withdraw_amount
                cursor.execute("UPDATE customer SET balance = {0} WHERE acc_no = {1};"
                               .format(current_amount, account_number))
                connect.commit()
                print()
                print("Amount {0} has been debited from account, available balance is {1}"
                      .format(withdraw_amount, current_amount))




            elif option == 3:  # change pin
                current_pin = int()
                cursor.execute("SELECT pin FROM cust_login_info AS a WHERE a.acc_no = {0};".format(account_number))
                for i in cursor.fetchall():
                    for j in i:
                        current_pin = int(j)

                change_pin = int(input("Enter new pin: "))
                confirm_pin = int(input("Enter new pin again: "))

                while (change_pin != confirm_pin):
                    print("pin dosenot match enter again")
                    print()
                    change_pin = int(input("Enter new pin: "))
                    confirm_pin = int(input("Enter new pin again: "))
                # if (change_pin == confirm_pin):
                cursor.execute(
                    "UPDATE cust_login_info SET pin = {0} WHERE acc_no = {1};".format(change_pin, account_number))
                connect.commit()
                print("PIN has been succesfully changed.")


            elif option == 4:  # check balance
                current_amount = 0
                cursor.execute("SELECT balance FROM customer AS a WHERE a.acc_no = {0};".format(account_number))
                for i in cursor.fetchall():
                    for j in i:
                        current_amount = int(j)
                print()
                print("Avaialable amount is: {0}".format(current_amount))


            elif option == 5:  # show transaction history of that customer.
                cursor.execute("SELECT * FROM transaction_hist WHERE debit_from = {0} or credit_to = {0}".format(account_number))
                result = cursor.fetchall()
                for i in result:
                    row = []
                    for j in i:
                        row.append(j)
                    print(row)

            elif option == 6:
                current_amount = 0
                cursor.execute("SELECT balance FROM customer AS a WHERE a.acc_no = {0};".format(account_number))
                for i in cursor.fetchall():
                    for j in i:
                        current_amount = int(j)
                transfer_amount = int(input("Enter amount to be transfered: "))
                credit_acc_no = int(input("Enter reciever's account number: "))
                cursor.execute("UPDATE customer SET balance = {0} WHERE acc_no = {1};"
                               .format(current_amount - transfer_amount, account_number))
                # connect.commit()

                curr_2 = 0
                cursor.execute("SELECT balance FROM customer WHERE acc_no={0}".format(credit_acc_no))

                for i in cursor.fetchall():
                    for j in i:
                        current_2 = int(j)


                cursor.execute("UPDATE customer SET balance = {0} WHERE acc_no = {1};".format(curr_2 + transfer_amount, credit_acc_no))
                connect.commit()

            elif option == 7:
                print("Exited Successfully")
                break





    if(user_input == 2):
        print("ADMIN LOGIN")
        admin_id = int(input("Enter your user id: "))
        admin_password = input("Enter your password: ")
        result = check_admin_info(admin_id, admin_password)
        while(result == False):
            print()
            print("Invalid credentials.")
            admin_id = int(input("Enter your admin id: "))
            admin_password = str(input("Enter your password"))
            if(check_admin_info(admin_id, admin_password) == 1):
                break
        cursor.execute("SELECT employee_id FROM emp_login_info AS a WHERE a.user_id = {0}".format(admin_id))

        employee_id = int()
        for i in cursor.fetchall():
            for j in i:
                employee_id = j

        emp_name = str
        cursor.execute("SELECT name FROM employee WHERE EMPLOYEE_ID = {0}".format(employee_id))
        for i in cursor.fetchall():
            for j in i:
                emp_name = j
        print()
        print("Welcome {0}".format(emp_name))


        admin_option = int()
        while(admin_option != 6):
            print(""""  *****************   """)
            print("Please select a option")
            print("1: Create new customer account")
            print("2: Close a customer account")
            print("3: Create admin account")
            print("4: Show all customers")
            print("5: Show all employees")
            print("6: Exit")

            admin_option = int(input("Enter here: "))

            if(admin_option == 1): # create new customer account
                name = input("Enter customer name: ")
                adhar_id = int(input("Enter adhar id: "))
                age = int(input("Enter your age: "))
                acc_no = account_number_generator()
                contact = int(input("Enter your phone number: "))
                city = input("Enter your city: ")
                account_type = (input("Enter account type: "))
                balance = 0
                branch_no = 16773
                cursor.execute("INSERT INTO customer VALUES({0}, '{1}', {2}, {3}, {4}, '{5}', '{6}', {7}, {8});"
                               .format((acc_no), (name), (adhar_id), (age), (contact), city,
                                       account_type, (balance), (branch_no)))
                connect.commit()

                cursor.execute("INSERT INTO cust_login_info VALUES({0}, {1}, '{2}', {3});"
                               .format(acc_no, user_id_generator(), password_generator(), pin_generator()))
                connect.commit()
                print("Account has been successfully created, account number is {0}".format(acc_no))


            elif admin_option == 2:   # close a customer account
                closing_account_number = int(input("Enter account number of customer: "))
                closing_adhar_id = int(input("Enter Aadhaar number of customer"))
                cursor.execute("DELETE FROM customer WHERE acc_no = {0};"
                               .format(closing_account_number))
                connect.commit()


                print("Customer account with account number = {0}, adhar_id = {1} has been successfully closed"
                      .format(closing_account_number, closing_adhar_id))


            elif admin_option == 3:  # create admin account
                name = str(input("Enter new employee name: "))
                employee_id = user_id_generator()
                age = int(input("Enter age: "))
                gender = int(input("Enter gender, 1 - Male or 2 - Female"))
                designation = input("Enter designation: ")
                branch_no = user_id_generator()
                cursor.execute("INSERT INTO employee VALUES ({0}), ({1}), ({2}), ({3}), ({4}), ({5});"
                               .format(employee_id, name, age, gender, designation, branch_no))
                print("Account has been sucessfully created, employee id is = {0}".format(employee_id))
                #### MORE ENTRIES


            elif admin_option == 4:  # show all customers
                cursor.execute("SELECT * FROM customer;")
                for i in cursor.fetchall():
                    print(i)


            elif admin_option == 5:  # show all employees.
                cursor.execute("SELECT * FROM employee;")
                for i in cursor.fetchall():
                    print(i)


        else:
            print("Exited successfully")

else:
    print("Thank You, Visit again")



















