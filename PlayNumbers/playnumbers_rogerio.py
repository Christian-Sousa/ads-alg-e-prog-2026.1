import os
import math

def main():
    clear_screen()
    # colecao de dados
    numbers = load_numbers()

    menu = '''
    **** Play Numbers ****
    1 - New Number
    2 - List Numbers
    3 - Number existence
    4 - Replace number
    5 - Count number
    6 - Remove number
    7 - Even numbers (filter)
    8 - Prime numbers (filter)
    9 - Negative numbers (filter)

    0 - Exit >>> '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1: # New
            number = int(input('New number: '))
            numbers.append(number)
            success()
        elif opcao == 2: # List
            list_numbers(numbers)
        elif opcao == 3: # existence
            number = int(input('Number: '))
            exist = contain(numbers, number)
            result = 'Yes' if exist else 'No'
            print(f'Exist: {result}')
        elif opcao == 4: # update -> replace
            old_number = int(input('Actual number: '))
            while not contain(numbers, old_number):
                print('Number not found!')
                old_number = int(input('Actual number: '))
            
            new_number = int(input('New number: '))
            replace(numbers, old_number, new_number)
            success()
        elif opcao == 5: # Count
            number = int(input('Number: '))
            count = count_item(numbers, number)
            print(f'There are {count} "{number}"s')
            success()
        elif opcao == 6: # remove
            number = int(input('Number: '))
            while not contain(numbers, number):
                print('Number not found!')
                number = int(input('number: '))
            count = count_item(numbers, number)
            numbers = remove_item(numbers, number)
            print(f'> {count} numbers "{number}" removed!')
            success()
        elif opcao == 7:
            even_numbers = filter_evens(numbers)
            list_numbers(even_numbers)
            success()
        elif opcao == 8:
            prime_numbers = filter_primes(numbers)
            list_numbers(prime_numbers)
            success()
        elif opcao == 9:
            negative_numbers = filter_negatives(numbers)
            list_numbers(negative_numbers)
            success()


        input('Enter to continue...')
        clear_screen()
        opcao = int(input(menu))

    # save values
    save_numbers(numbers)


def clear_screen():
    os.system('clear')


def success():
    print('Success!')


def contain(collection, element):
    for item in collection:
        if item == element:
            return True
    return False


def replace(collection, old_value, new_value):
    for i in range(len(collection)):
        item = collection[i]
        if item == old_value:
            collection[i] = new_value


def count_item(collection, element):
    count = 0
    for item in collection:
        if item == element:
            count += 1
    return count


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
    print('Chiao!')


# Filters
def filter_evens(numbers):
    filtereds = []
    for number in numbers:
        if number % 2 == 0:
            filtereds.append(number)
    
    return filtereds


def filter_negatives(numbers):
    filtereds = []
    for number in numbers:
        if number < 0:
            filtereds.append(number)
    
    return filtereds


def filter_primes(numbers):
    filtereds = []
    for number in numbers:
        if is_prime(number):
            filtereds.append(number)
    
    return filtereds


def is_prime(number):
    if number <= 1:
        return False
    
    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False
    
    return True





main()