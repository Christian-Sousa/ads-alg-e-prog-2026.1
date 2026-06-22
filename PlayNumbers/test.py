numbers = [1,23,4,5,56] 

for i in numbers:
    new_number = 0
    aux = i
    #i = new_number
    numbers.remove(aux)
    numbers.append(new_number)

print(numbers)