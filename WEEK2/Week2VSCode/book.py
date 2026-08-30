tax_rate = 9.181
tax_per = round(tax_rate / 100, 3) #percentage of the tax rate rounded to 3 decimal places
print(f"Book percentage of the 9.181 tax: ${tax_per}")

#collect price input from user
#collect = input("What is the price of the book?: $")

#print(f"The price of the book is: ${collect}")

#convert the text collection to numbers
collect = float(input(str("What is the price of the book?: ")))

print(f"The price of the book is: ${collect}")

#calculate the book price's tax
book_tax = round(tax_per * collect, 2)

#caculate the total cost (book price plus tax)
book_cost = round(collect + book_tax, 2)

#print all outputs
#print(f"book price: ${collect}")
#print(f"book tax: ${book_tax}")
#print(f"total cost: ${book_cost}")

#print all outputs in one line
print(f"book price: ${collect}, book tax: ${book_tax}, total cost: ${book_cost}")
