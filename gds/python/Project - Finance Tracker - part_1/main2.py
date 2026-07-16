import json



try:
    with open("financial_report.json" , 'r') as file:

        finance_data= json.load(file)

except FileNotFoundError:
        finance_data={'expense':[],'income':[]}



def save_data():
    with open("financial_report.json" , 'w') as file:
         
        json.dump(finance_data, file)


def add_transaction(transaction_type):
     
     description=input("Description :")

     amount=float(input("Amount : "))

     finance_data[transaction_type].append({"description":description,"amount":amount})

     print(f' Transaction of amount {amount} is added for {description}')
     save_data()


def list_transaction(transaction_type):
     
    if not finance_data[transaction_type]:
         print("No transaction to list")

    for data in finance_data[transaction_type]:
         print(data['description'] , data['amount'])


def generate_report():
     
    total_expense=sum(item['amount'] for item in finance_data['expense'])
    total_income=sum(item['amount'] for item in finance_data['income'])

    balance=total_income-total_expense

    print(f' Your total expenses is {total_expense}')
    print(f' Your total income is {total_income}')
    print(f' Your total balance is {balance}')


def main():
     
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. List Expenses")
        print("4. List Incomes")
        print("5. Generate Report")
        print("6. Exit")
        choice = input("Select an option: ")


        if choice == '1':
            add_transaction('expense')
        elif choice == '2':
            add_transaction('income')
        elif choice == '3':
            list_transaction('expense')
        elif choice == '4':
            list_transaction('income')
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("Exiting Personal Finance Tracker.")
            break
        else:
            print("Invalid option, please try again.")


main()