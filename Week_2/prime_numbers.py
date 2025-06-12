# prime numbers: 2, 3, 5, 7
n = int(input())
if n < 2:
    print("Not prime")
else:
    for i in range(2, n):
        if n % 2 == 0:
            print("Not prime")
            break
    else:
        print("It is a prime")
# Check if the number is a prime or not
# Example: n = 7, print(7 is prime), n = 10, print(10 is not a prime)