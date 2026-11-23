expenses = []


def add_expenses(expenses):
    item = input("\nWhat did you spend money on: ")
    category = input("category (e.g Food, School, Tech, Fun): ")

    try:
        amount = input("What is the cost: ")
        cleaned = amount.lstrip("$").strip()
        amount = float(cleaned)
    except ValueError:
        print("Invalid input")
        return
    entry = {
        "item": item.strip().lower(),
        "category": category.strip().lower(),
        "amount": amount,
    }
    expenses.append(entry)
    print("Expenses recorded!")


def view_summary(expenses):
    if expenses == []:
        print("\nNo expenses logged yet.")
        return

    print("\n--- Logged Expenses ---")
    total = 0.0
    totals_by_category = {}

    for index, entry in enumerate(expenses, start=1):
        print(
            f"{index}. {entry['item']} [{entry['category']}] - ${entry['amount']:.2f}"
        )
        total += entry["amount"]
        category = entry["category"].strip().title()

        if category not in totals_by_category:
            totals_by_category[category] = 0.0
        totals_by_category[category] += entry["amount"]

    print(f"\nTotal Spend: ${total:.2f}")
    print("\n---Spending by category")
    for category, subtotal in totals_by_category.items():
        print(f"{category}: ${subtotal:.2f}")


def main():
    while True:
        print("\n1. Add an expense.")
        print("2. View your expenses.")
        print("3. Exit.")

        selection = input("Choose an option (1-3): ")

        if selection == "1":
            add_expenses(expenses)
        elif selection == "2":
            view_summary(expenses)
        elif selection == "3":
            print("Have a nice day!")
            break
        else:
            print("ERROR! \nWrong selection")
            break


if __name__ == "__main__":
    main()
