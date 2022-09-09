# TASK 1

# Q1
# question = input('Is it raining out, y / n ? ')
# if question == 'y':
#     print('Take an umbrella')
# elif question == 'n':
#     print('You don\'t need an umbrella')
# else:
#     print('You didn\'t seem to answer the question, try again')
#     question = input('Is it raining out, y / n ? ')

# Q2
# my_money = int(input('How much money do you have? '))
# boat_cost = 20 + 5
#
# if my_money > boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')

# Q3
# year = input('What year is the book from? ')
#
# century = int(year)
#
# is_noughties = year.endswith('0', 2, 3)
# is_tens = year.endswith('1', 2, 3)
# is_twenties = year.endswith('2', 2, 3)
# is_thirties = year.endswith('3', 2, 3)
# is_forties = year.endswith('4', 2, 3)
# is_fifties = year.endswith('5', 2, 3)
# is_sixties = year.endswith('6', 2, 3)
# is_seventies = year.endswith('7', 2, 3)
# is_eighties = year.endswith('8', 2, 3)
# is_nineties = year.endswith('9', 2, 3)
#
#
# if century < 1900:
#     if century < 1800:
#         print("Sorry, we don\'t stock books published that early")
#     else:
#         if century >= 1800 and is_noughties:
#             print("19th Century, noughties")
#         elif century > 1800 and is_tens:
#             print("19th Century, tens")
#         elif century > 1800 and is_twenties:
#             print("19th Century, twenties")
#         elif century > 1800 and is_thirties:
#             print("19th Century, thirties")
#         elif century > 1800 and is_forties:
#             print("19th Century, forties")
#         elif century > 1800 and is_fifties:
#             print("19th Century, fifties")
#         elif century > 1800 and is_sixties:
#             print("19th Century, sixties")
#         elif century > 1800 and is_seventies:
#             print("19th Century, seventies")
#         elif century > 1800 and is_eighties:
#             print("19th Century, eighties")
#         else:
#             print("18th Century, nineties")
# elif 1900 <= century < 1950:
#     if century > 1950:
#         print("too late")
#     else:
#         if century >= 1900 and is_noughties:
#             print("20th Century, noughties")
#         elif century > 1900 and is_tens:
#             print("20th Century, tens")
#         elif century > 1900 and is_twenties:
#             print("20th Century, twenties")
#         elif century > 1900 and is_thirties:
#             print("20th Century, thirties")
#         else:
#             print("20th Century, forties")
# else:
#     print("Sorry, we don\'t stock books published that late")


# TASK 2

# Q2
# chocolates = {
#
#     'white': 1.50,
#     'milk': 1.20,
#     'dark': 1.80,
#     'vegan': 2.00,
#
# }
#
# item = input("Chocolate type: ").lower()
#
#
# if item in chocolates:
#     print('£',chocolates.get(item))
# else:
#     print('Sorry, no item')

# Q3
# import random
#
# number_list = [3, 33, 13, 36, 48, 19, 29]
#
#
# random_numbers = random.sample(range(1, 100), 7)
#
#
# matching_numbers = set(number_list).intersection(random_numbers)
# print('Matching numbers:', list(matching_numbers))
#
# matches = len(matching_numbers)
#
# if matches == 3:
#     print('\n*PRIZE* £20!')
# elif matches == 4:
#     print('\n*PRIZE* £40!')
# elif matches == 5:
#     print('\n*PRIZE* £100!')
# elif matches == 6:
#     print('\n*PRIZE* £10,000,000! *PRIZE*')
# else:
#     print('\nSorry, no win')
#
#
# import random
#
# number_list = list(int(number)
#                    for number in input("Enter your seven lottery numbers - separated by a space: ").strip().split())
#
# random_numbers = random.sample(range(1, 100), 7)
#
# matching_numbers = set(number_list).intersection(random_numbers)
# print('Matching numbers:', list(matching_numbers))
#
# matches = len(matching_numbers)
#
# if matches == 3:
#     print('\n*PRIZE* £20!')
# elif matches == 4:
#     print('\n*PRIZE* £40!')
# elif matches == 5:
#     print('\n*PRIZE* £100!')
# elif matches == 6:
#     print('\n*PRIZE* £10,000,000! *PRIZE*')
# else:
#     print('\nSorry, no win')

# TASK 3

# Q2

# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w') as poem_file:
#     poem_file.write(poem)

# Q3
# PART 1
# still_standing = 'You could never know what it\'s like \nYour blood like winter freezes just like ice\nAnd there\'s a cold lonely light that shines from you\nYou\'ll wind up like the wreck you hide behind that mask you use\n\nAnd did you think this fool could never win?\nWell look at me, I\'m coming back again\nI got a taste of love in a simple way\nAnd if you need to know while I\'m still standing, you just fade away\n\nDon\'t you know I\'m still standing better than I ever did\nLooking like a true survivor, feeling like a little kid\nI\'m still standing after all this time\nPicking up the pieces of my life without you on my mind\n\nI\'m still standing (Yeah, yeah, yeah)\nI\'m still standing (Yeah, yeah, yeah)'
# with open('song.txt', 'w') as song_file:
#     song_file.write(still_standing)

# PART 3
# from pprint import pprint as pp
#
# file = open('song.txt', 'r')
# lines = file.readlines()
# word = 'still'
#
# for line in lines:
#     if word in line:
#         pp(line.strip())
# file.close()



# TASK 4

# Q1


### EXERCISE 5 ###
# """
# This API is called 'Pokéapi' pokeapi.co/
# It gives access to data about Pokémons
# This API is free and does not require any authentication!
#
# Each Pokemon has a number that identifies it
#
# You can retrieve information about different Pokemon from urls
#
# https://pokeapi.co/api/v2/pokemon/6/
# """

import requests

pokemon_number = [33, 3, 5, 34, 55, 56]

for number in pokemon_number:
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(number)
    response = requests.get(url)
    pokemon = response.json()
    pokemon_name = pokemon['name']
    with open('../pokemon.txt', 'a+') as file:
        file.write('\n{}:\n'.format(pokemon_name))
    moves = pokemon['moves']

    for move in moves:
        pokemon_move = move['move']['name']
        with open('../pokemon.txt', 'a+') as file:
            file.write('{}'.format(pokemon_move))






# import requests
#
#
# endpoint1 = 'https://opentdb.com/api.php?amount=10&category=10&difficulty=easy'  # this endpoint returns data about astronauts currently in space
#
# response = requests.get(endpoint1)
#
# data = response.json()
#
# questions = input(data['results'][8]['question'])
# answers = (data['results'][8]['correct_answer'])
# if questions == answers:
#     print('Correct')
# else:
#     print(answers)
