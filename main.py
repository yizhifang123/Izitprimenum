prime_num = False

number = input("number:")

number = int(number)

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            prime_num = True
            break
if prime_num:
    print("no")
else:
    print("yes")
