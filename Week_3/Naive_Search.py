l =  [480, 296, 3993, 4668, 1483, 730, 6280, 1329, 4571, 625]
g = int(input("Guess a number between 1 and 10,000 "))

# if question in l:
#     print("You guessed one of the numbers")
# else:
#     print("You did not guess one of the numbers")


# flag = 0
# for i in range(len(l)):
#     if question == l[i]:
#         print("You guessed one of the numbers")
#         flag = 1
#         break
# if flag == 0:
#     print("You guessed it wrong")


# write a function search(list, input) this should return the output


def guess_number(l, g):
    flag = 0
    for i in range(len(l)):
        if g == l[i]:
            return "You guessed one of the numbers"
            flag = 1
            break
    if flag == 0:
        return "You guessed it wrong"
print(guess_number(l, g))