import csv
from collections import defaultdict
def top(fName):
    customer_expenses = defaultdict(float)
    product_sales = defaultdict(int)
    with open(fName,'r') as fin:
        sales = csv.DictReader(fin)
        for record in sales:
            customer_name = record['CustomerName']
            product_name = record['ProductName']
            customer_expenses[customer_name] += float(record['Price'])
            product_sales[product_name] += 1
    
    highest_expense = max(customer_expenses.values())
    highest_sale = max(product_sales.values())
    for customer in customer_expenses:
        if customer_expenses[customer] == highest_expense:
            top_customer = customer
            break
    for product in product_sales:
        if product_sales[product] == highest_sale:
            top_product = product
            break
    return top_customer,top_product
print top('Sales.txt')