transactions = [
    {'type':"purchase", 'amount':23, "date":'2024-01-14'},
    {'type':"sale", 'amount':50, "date":'2024-01-14'},
    {'type':"purchase", 'amount':20, "date":'2024-01-14'},
]

def sum_up(stype: str):
    sum = 0
    for transaction in transactions:
        if transaction["type"] == stype:
            sum += transaction["amount"]
    return sum

print("Summ of sales: " , sum_up("sale"))
print("Summ of purchases: " , sum_up("purchase"))