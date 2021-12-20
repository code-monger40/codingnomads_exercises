# Print out every prime number between 1 and 1000.

num = 1001
for i in range(1, num):
    if num % i == 0:
        break
    else:
        print(num)
        count += 1

#  for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#             count += 1

count = 0
for num in range(1, 1001):
    if num != 1:  # Not a prime
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            count += 1

print("There are", count, "prime numbers.")  # 168 Primes