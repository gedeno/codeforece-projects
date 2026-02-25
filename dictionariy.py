expence = {}
all_expence  = []
def expence_tracker():
    while True:
        catagories = input('enter categories: ')
        if catagories == 'quit':
            break
        amount = int(input('enter amount: '))
        expence["catagories"] = catagories
        expence["amount"] = amount
        all_expence.append(expence)
    for i in all_expence:
        print(f'{i["catagories"]} : {i["amount"]}')
expence_tracker()