num = int(input("Please provide anumber = "))
isprime = True
if num == 0:
    print(num, "is neither prime nor composite")
if num == 1:
    print(num, "is a prime number")
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num, "is not a prime number i.e, its a composite number")
            isprime = False
            break
    if isprime == True:
        print(num, "is a prime number")