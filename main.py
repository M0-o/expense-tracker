from expenseTracker import Category, create_spend_chart
from os import system , name 
from colorama import init, Fore, Style

init()

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def main():
    categories = {}

    while True:
        clear()
        print(Fore.CYAN + Style.BRIGHT + "\nExpense Tracker Menu:" + Style.RESET_ALL)
        print("1. Create a new category")
        print("2. Deposit to a category")
        print("3. Withdraw from a category")
        print("4. Transfer between categories")
        print("5. Show category details")
        print("6. Display spend chart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cat_name = input("Enter the category name: ")
            if cat_name not in categories:
                categories[cat_name] = Category(cat_name)
                print(Fore.GREEN + f"Category '{cat_name}' created." + Style.RESET_ALL)
            else:
                print("Category already exists.")

        elif choice == "2":
            if not categories:
                print("No categories available.")
            else:
                print("Select the category to deposit to:")
                cat_list = list(categories.keys())
                for i, c in enumerate(cat_list, start=1):
                    print(f"{i}. {c}")
                sel = int(input("Enter choice: ")) - 1
                if 0 <= sel < len(cat_list):
                    cat_name = cat_list[sel]
                    amount = float(input("Enter amount: "))
                    desc = input("Enter description: ")
                    categories[cat_name].deposit(amount, desc)
                    print(Fore.GREEN + "Deposit completed." + Style.RESET_ALL)
                else:
                    print("Invalid choice.")

        elif choice == "3":
            if not categories:
                print("No categories available.")
            else:
                print("Select the category to withdraw from:")
                cat_list = list(categories.keys())
                for i, c in enumerate(cat_list, start=1):
                    print(f"{i}. {c}")
                sel = int(input("Enter choice: ")) - 1
                if 0 <= sel < len(cat_list):
                    cat_name = cat_list[sel]
                    amount = float(input("Enter amount: "))
                    desc = input("Enter description: ")
                    if categories[cat_name].withdraw(amount, desc):
                        print(Fore.GREEN + "Withdrawal successful." + Style.RESET_ALL)
                    else:
                        print("Insufficient funds.")
                else:
                    print("Invalid choice.")

        elif choice == "4":
            if len(categories) < 2:
                print("Not enough categories to transfer between.")
            else:
                print("Select the category to transfer from:")
                cat_list = list(categories.keys())
                for i, c in enumerate(cat_list, start=1):
                    print(f"{i}. {c}")
                from_sel = int(input("Enter choice: ")) - 1
                if 0 <= from_sel < len(cat_list):
                    from_cat = cat_list[from_sel]
                else:
                    print("Invalid choice.")
                    continue

                print("Select the category to transfer to:")
                for i, c in enumerate(cat_list, start=1):
                    print(f"{i}. {c}")
                to_sel = int(input("Enter choice: ")) - 1
                if 0 <= to_sel < len(cat_list):
                    to_cat = cat_list[to_sel]
                else:
                    print("Invalid choice.")
                    continue

                amount = float(input("Enter amount: "))
                if categories[from_cat].transfer(amount, categories[to_cat]):
                    print(Fore.GREEN + "Transfer completed." + Style.RESET_ALL)
                else:
                    print("Insufficient funds.")

        elif choice == "5":
            if not categories:
                print("No categories available.")
            else:
                print("Select the category to show details:")
                cat_list = list(categories.keys())
                for i, c in enumerate(cat_list, start=1):
                    print(f"{i}. {c}")
                sel = int(input("Enter choice: ")) - 1
                if 0 <= sel < len(cat_list):
                    cat_name = cat_list[sel]
                    print(Fore.YELLOW + str(categories[cat_name]) + Style.RESET_ALL)
                else:
                    print("Invalid choice.")

        elif choice == "6":
            if categories:
                try:
                    print(Fore.MAGENTA + create_spend_chart(list(categories.values())) + Style.RESET_ALL)
                except:
                    print("No spendings yet")
            else:
                print("No categories to display.")

        elif choice == "7":
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
        system('pause')
        

if __name__ == "__main__":
    main()
