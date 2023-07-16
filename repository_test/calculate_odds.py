even_list = []
odd_list = []

for x in range(1,11):
    is_odd = x % 2
    if is_odd > 0 :
        odd_list.append(x)
    else:
        even_list.append(x)
print("Welcome to number calculator!")
print('Odd List:', odd_list)
print('Even List:', even_list)

print("2 + 2 = 4")