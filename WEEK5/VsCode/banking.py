# banking.py

balance = 1.00
years = 0

while balance < 2.00:
    balance = balance * 1.05
    years += 1

print(f"It will take {years} years for the money to double.")