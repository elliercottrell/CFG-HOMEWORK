# PYTHON TASK 3

# Q1
# chairs = 15
# nails = 4
# total_nails = chairs * nails
# message = 'I need to buy {} nails'.format(total_nails)
# print(message)

# Q2
# my_name = 'Penelope'
# my_age = 29
# message = 'My name is {} and I am {} years old'.format(my_name, my_age)
# print(message)

#Q3
# boxes_in_fridge = int(input("How many boxes of eggs are in your fridge? "))
# eggs_in_box = 6
# eggs_in_omlette = 4
#
# omlettes = (eggs_in_box * boxes_in_fridge) / eggs_in_omlette
#
# output = 'You can make {} omlettes with {} boxes of eggs'.format(omlettes, boxes_in_fridge)
# print(output)


# Q4 - 1
# my_str = "I love coding."
# my_str = "I love coding.".replace('.', '!')
# print(my_str)

# Q4 - 2
# my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
# my_str_1 = my_str_1.lower()
# print(my_str_1)

# Q4 - 3
# my_str_2 = "We enjoy travelling"
# ans_1 = my_str_2.startswith('A')
# print(ans_1)

# Q4 - 4
# my_str_3 = "1.458.001"
# ans_2 = len(my_str_3)
# print(ans_2)

# Q5 - 1
# wrd = "Python"
# ans_1 = wrd[2:]
# print(ans_1)

# Q5 - 2
# wrd = "Python"
# ans_1 = wrd[:4]
# print(ans_1)

# Q5 - 3
# wrd = "Python"
# ans_1 = wrd[2:4]
# print(ans_1)

# Q5 - 4
# wrd = "Python"
# ans_1 = wrd[1:5:2]
# print(ans_1)

# Q6
# for number in range(100):
# 	output = 'o' * number
# 	print(output)

# def calculate_vat(amount):
#     total = amount * 1.2
#     return total
#
#
# print(calculate_vat(100))
#
#
# def sum(x,y):
#     add_numbers = x + y
#     return add_numbers

# item_1 = 'cheesy chips'
# item_1_price = 5.00
# item_2 = 'classic burger'
# item_2_price = 14.00
# item_3 = 'buffalo wings'
# item_3_price = 7.00
#
#
# def my_receipt(a, b, c, d, e, f):
#
#     total = b + d + f
#     items = [[a, b], [c, d], [e, f]]
#
#     for item in items:
#         print(item[0], item[1])
#
#     receipt_total = '\nTOTAL ' + str(total)
#     return receipt_total
#
#
# print(my_receipt(item_1, item_1_price, item_2, item_2_price, item_3, item_3_price))


item_1 = input('first item: ')
item_1_price = int(input('first item price: '))
item_2 = input('second item: ')
item_2_price = int(input('second item price: '))
item_3 = input('third item: ')
item_3_price = int(input('third item price: '))
print('\n')


def my_receipt(a, b, c, d, e, f):

    total = b + d + f
    items = [[a, b], [c, d], [e, f]]

    for item in items:
        print(item[0], item[1])

    receipt_total = '\nTOTAL ' + str(total)
    return receipt_total


print(my_receipt(item_1, item_1_price, item_2, item_2_price, item_3, item_3_price))