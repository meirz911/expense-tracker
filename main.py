import json

while True:
    print('''Hello!
    What do you want?

    1.Add expense
    2.Show all expenses
    3.Show total
    4.Exit
    ''')

    type = int(input('Enter a number: '))


    match type:
        case 1:
            print('What have you spent today?')

            title = input('Title: ')
            while True:
                try:
                    amount = float(input('Amount ($): '))
                    break
                except ValueError:
                    print('Enter a correct type!')
            category = input('Category: ')
            date = input('Date (YYYY-MM-DD): ')

            data = {'title': title, 'amount': amount, 'category': category, 'date': date}

            try:
                with open('data.json', 'r', encoding='utf-8') as file:
                    expenses = json.load(file)
            except FileNotFoundError:
                expenses = []
                expenses.append(data)

            with open('data.json', 'w', encoding='utf-8') as file:
                json.dump(expenses, file, indent=4, ensure_ascii=False)
            
            print('Expenses successfully added!')
            break

        case 2:
            with open('data.json', 'r', encoding='utf-8') as data:
                expenses = json.load(data)
                print(sorted(expenses, key=lambda item: item['date']))
            break

        case 3:
            with open('data.json', 'r', encoding='utf-8') as data:
                expenses = json.load(data)
                
                total = 0
                for price in expenses:
                    total += price['amount']
                
                print(total)
            break

        case 4:
            break