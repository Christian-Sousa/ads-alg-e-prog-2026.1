def main():
    clear_screen()

    print()
    print('-='*50)
    print('Welcome to PlayNumbers!')
    input('Press <Enter> to continue...')

    menu = '''
        Choose one command...

        1 - New Number
        2 - Print Collection
        3 - Reset Collection
        4 - Count Collection
        5 - Larger and Smaller Number
        6 - Sum of values
        7 - Average of values
        8 - Positive Values
        9 - Negative Values

        0 - Exit 

        Command: '''
    numbers = []
    option_menu = int(input(menu))

    while option_menu != 0:
        if option_menu == 1: 
            number = int(input('Number: '))
            numbers.append(number)
            sucess()

        elif option_menu == 2:
            print(numbers)

        elif option_menu == 3:
            new_number = int(input('Input some number for replace all the list numbers: '))
            for i in range(len(numbers)):
                numbers[i] = new_number
            sucess()
        
        elif option_menu == 4:
            print()
            print(f'The collection has {count(numbers)} items.')

        elif option_menu == 5:
            larger = larger_number(numbers)
            larger_index = numbers.index(larger)
            smaller = small_number(numbers)
            smaller_index = numbers.index(smaller)
            print(f'The SMALLER number is {smaller} -> position: {smaller_index+1}º. ')
            print(f'The LARGER number is {larger} -> position: {larger_index+1}º. ')

        elif option_menu == 6:
            print(f'Sum of values: {sum_values(numbers)}')
        
        elif option_menu == 7:
            print(f'Average of values: {average_values(numbers):.2f}')
        
        #FAZER A OPCAO DE SUBSTITUIR E VERIFICAR EXISTENCIA
        #CONTINUAR COM LAMBDA, FILTER, etc

        elif option_menu == 8:
            positive_collection,positive_amount = positive_numbers(numbers)
            print(f'Collection <numbers> has {positive_amount} items > 0.')
            print(f'>> {positive_collection}')

        elif option_menu == 9:
            negative_collection, negative_amount = negative_numbers(numbers)
            print(f'Collection <numbers> has {negative_amount} items < 0.')
            print(f'>> {negative_collection}')


        print()
        input('Press <Enter> to continue...')
        clear_screen()
        print('-='*50)
        option_menu = int(input(menu))

    print('-='*50)



def clear_screen():
    import os
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def sucess():
    print()
    print('Sucess!')

def count(collection):
    counter = 0
    for item in collection:
        counter+=1

    return counter

def larger_number(collection):
    larger_item = 0
    for item in collection:
        if item > larger_item:
            larger_item = item

    return larger_item

def small_number(collection):
    smaller_item = collection[0]
    smaller_item = float('inf')

    for item in collection:
        if item < smaller_item:
            smaller_item = item

    return smaller_item

def sum_values(collection):
    sum_counter=0
    for item in collection:
        sum_counter+=item

    return sum_counter

def average_values(collection):
    return sum_values(collection)/count(collection)

def positive_numbers(collection):
    positives = []
    for item in collection:
        if item > 0:
            positives.append(item)
    return positives, count(positives)

def negative_numbers(collection):
    negatives = []
    for item in collection:
        if item < 0:
            negatives.append(item)
    return negatives, count(negatives)

main()