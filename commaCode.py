# A function that takes a list value as an argument and returns a string where all items are separated by a comma and a space, with and before the last item.

userInput = input("Enter your items: ")
# separate items in user input and create a list
separateItems = userInput.split(',')

def punctuation(items):
    numberOfItems = len(items)
    if items == ['']:
        print("You have no items.")
    elif numberOfItems == 1:
        print("Your item is " + items[0] + ".")
    elif numberOfItems == 2:
        print("Your items are: " + items[0] + ' and ' + items[1] + ".")
    else:
        print('Your items are: ')
        # iterate items from the first to second-last
        for i in items[:-1]:
            print(i, end=', ')
        # join last item with the rest of the items
        print('and ' + items[-1] + '.')
    
punctuation(separateItems)
