fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # here fruits is on 0 index and vegetables is on 1 index

print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2]) # this line of code mean in dirty_dozen array get second array element [fruits = 0 index, vegetables = 1 ]
print(dirty_dozen[1][3])