import math

def main():
    clear_screen()

    print()
    print('-='*50)
    print()
    print('Welcome to PlayNumbers!')
    input('Press <Enter> to continue...')

    numbers = load_numbers()

    menu = '''
        Choose one command...

        1 - New Number
        2 - Print Collection
        3 - Reset Collection
        4 - Replace number
        5 - Number existence
        6 - Count Collection
        7 - Count number
        8 - Remove number
        9 - Even numbers
        10 - Prime numbers
        11 - Negative numbers
        12 - Odd numbers (filter)
        13 - Powered by 2 (map)
        14 - Halfered (map)
        15 - Half of Even numbers (filter/map)
        16 - Sum of all
        17 - Sum of all odd
        18 - Sum of double of even
        19 - The Largest odd number
        20 - The largest number of all

        0 - Exit 

        Command: '''
    
    option_menu = int(input(menu))

    while option_menu != 0:
        if option_menu == 1: # New number
            number = int(input('Number: '))
            numbers.append(number)
            success()

        elif option_menu == 2: # Print
            print(numbers)

        elif option_menu == 3: # Reset
            new_number = int(input('Input some number for replace all the list numbers: '))
            for i in range(len(numbers)):
                numbers[i] = new_number
            success()
        
        elif option_menu == 4: # Replace
            old_number = int(input('Actual number: '))
            while not contain(numbers, old_number):
                print('Number not found!')
                old_number = int(input('Actual number: '))
            
            new_number = int(input('New number: '))
            replace(numbers, old_number, new_number)
            success()

        elif option_menu == 5: # Existence
            number = int(input('Number: '))
            if contain(numbers,number):
                result = 'Yes'    
            else:
                result = 'No'
            print(f'Exist: {result}')

        elif option_menu == 6: # Count collection
            print()
            print(f'There are {count_collection(numbers)} items.')

        elif option_menu == 7: # Count number
            number = int(input('Number: '))
            count = count_item(numbers, number)
            print(f'There are {count} "{number}"s')
            success()

        elif option_menu == 8: # Remove
            number = int(input('Number: '))
            while not contain(numbers, number):
                print('Number not found!')
                number = int(input('number: '))
            count = count_item(numbers, number)
            numbers = remove_item(numbers, number)
            print(f'> {count} number(s) "{number}" removed!')
            success()

        elif option_menu == 9:
            even_numbers = filter(numbers, is_even)
            list_numbers(even_numbers)
            success()

        elif option_menu == 10:
            prime_numbers = filter(numbers, is_prime)
            list_numbers(prime_numbers)
            success()

        elif option_menu == 11:
            # negative_numbers = filter(numbers, is_negative)
            negative_numbers = filter(numbers, lambda n:n < 0)
            list_numbers(negative_numbers)
            success()

        elif option_menu == 12:
            list_numbers(filter(numbers, is_odd))
            success()

        elif option_menu == 13:
            # powered = powered_by_2(numbers)
            # list_numbers(map(numbers, pow_by_2))
            list_numbers(map(numbers, lambda r:r**2))
            success()

        elif option_menu == 14:
            # halfereds = halfered(numbers)
            list_numbers(map(numbers, half_value))
            success()

        elif option_menu == 15:
            list_numbers(map(filter(numbers, is_even), half_value))
            success()

        elif option_menu == 16:
            sum_of_all = reduce_sum(numbers)
            print(f'Sum of all numbers --> {sum_of_all}')

        elif option_menu == 17:
            result = reduce_sum(filter(numbers, is_odd))
            print(f'Sum of all odd numbers --> {result}')

        elif option_menu == 18:
            # result = reduce_sum(map(filter(numbers, is_even), double_value))

            result = reduce(map(filter(numbers, is_even), lambda x:x*2), lambda acc, actual: acc + actual, 0)

            print(f'Sum of double of even numbers --> {result}')

        elif option_menu == 19:
            result = reduce_largest(filter(numbers, is_odd))
            print(f'The largest odd number is {result}')

        elif option_menu == 20:
            # result = reduce(numbers, largest, numbers[0])
            result = reduce(numbers, lambda acc, actual: actual if actual >= acc else acc, numbers[0])

            print(f'The largest number is {result}')

        print()
        input('Press <Enter> to continue...')
        clear_screen()
        print('-='*50)
        option_menu = int(input(menu))

    clear_screen()
    save_numbers(numbers)

    print()
    print('-='*50)
    print()

def clear_screen():
    import os
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def success():
    print()
    print('Sucess!')

def replace(collection, old_value, new_value):
    for i in range(len(collection)):
        item = collection[i]
        if item == old_value:
            collection[i] = new_value

def count_collection(collection):
    counter = 0
    for item in collection:
        counter+=1
    return counter

def count_item(collection, element):
    count = 0
    for item in collection:
        if item == element:
            count += 1
    return count

def contain(collection, element):
    for item in collection:
        if item == element:
            return True
    return False

def remove_item(collection, element):
    new_collection = []

    for item in collection:
        if item != element:
            new_collection.append(item)
    return new_collection

def list_numbers(numbers):
    print(f'> {len(numbers)} numbers:')
    for item in numbers:
        print(f'{item}', end=' ')
    print('\n---------------')

def load_numbers():
    collection = []
    file = open('numbers.txt')
    
    for line in file:
        number = line.strip()
        collection.append(int(number))

    file.close()
    return collection

def save_numbers(numbers):
    lines = []
    for number in numbers:
        lines.append(str(number)+'\n')
    
    file = open('numbers.txt', 'w')
    file.writelines(lines)
    file.close()
    print()
    print("""                                                       See you later...""")

# Criterion Functions
def is_even(number):
    return number % 2 == 0

def pow_by_2(number):
    return number**2

def is_odd(number):
    return not is_even(number)

def is_negative(number):
    return number < 0

def is_prime(number):
    if number <= 1:
        return False
    
    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False
    return True

# Filters
def filter(collection, fn_criterion):
    filtereds = []
    for item in collection:
        if fn_criterion(item):
            filtereds.append(item)  
    return filtereds

# Tranform function
def half_value(value):
    return value/2

def double_value(value):
    return value*2

# Maps
def map(collection, fn_transformation):
    new_collection = []
    for item in collection:
        new_item = fn_transformation(item)
        new_collection.append(new_item)
    return new_collection

def powered_by_2(numbers):
    new_list = []
    for number in numbers:
        new_number = number**2
        new_list.append(new_number)
    return new_list

def halfered(numbers):
    new_list = []
    for number in numbers:
        new_number = number/2
        new_list.append(new_number)
    return new_list

# Reduce
def reduce(collection, operation, initial_value):
    acc = initial_value
    for actual in collection:
        acc = operation(acc, actual)
    return acc

def reduce_sum(numbers):
    sum_all = 0
    for number in numbers:
        sum_all = sum_all + number
    return sum_all

def reduce_largest(numbers):
    largest = numbers[0]
    for item in numbers:
        if item > largest:
            largest = item
    return largest

main()