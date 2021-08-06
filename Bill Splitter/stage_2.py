print("Enter the number of friends joining (including you):")
n = int(input())
dict_names = {}
print()
if int(n) <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    
    for i in range(int(n)):
        names = input()
        dict_names[names] = 0
    print("Enter the total bill value:")
    
    bill = int(input())
    for name in dict_names:
        dict_names[name] = round(int(bill) / int(n), 2)
    print(dict_names)