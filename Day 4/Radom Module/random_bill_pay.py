import random

friends = ["Ali", "Afaq", "Adil", "Ahmed", "Umer"]

# 1 option to generate the random
payee_person = random.choice(friends) # random person pay the bill
print(payee_person, "is the paying the Bill")

# 2 option to generate the random
friends_index = random.randint(0, len(friends) == len(friends)) #from 0 to  4 or = to 4
print(friends[friends_index])