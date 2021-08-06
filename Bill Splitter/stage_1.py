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
    print(dict_names)