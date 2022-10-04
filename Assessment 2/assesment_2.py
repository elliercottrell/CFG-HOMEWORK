"""
PART 3

Write a function that takes in a non-empty array of integers that are sorted in
ascending order and returns a new array of the same length with the squares of
the original integers also sorted in ascending order.

Example Input:
numbers = [1,2,3,5,6,8,9]

Example Output:
[1,4,9,25,36,65,81]

"""

my_array = [10, 20, 2, 3]
my_array.sort()


def sorted_squared(array):
    my_array.sort()
    new_array = []
    for num in array:
        new = num ** 2
        new_array.append(new)
    print(new_array)
    return new_array


sorted_squared(my_array)

# used map - not sure this was right for what was asked
# def my_function(array):
#     return array ** 2
#
#
# new_array = list(map(my_function, my_array))
# print(new_array)


"""
PART 4
Write tests for the newly created Sorted Squared Numbers function (in Q3). 
Provide a brief explanation for your test case options. 

"""

# First test is to check the array is not empty, that it contains values.
# Second to test the array is sorted - to make sure array is in the correct order before it is squared


from unittest import TestCase, main
from assesment_2 import sorted_squared


class SortedSquaredFunction(TestCase):
    def test_sorted_array(self):
        expected = [4, 9, 100, 400]
        result = sorted_squared(my_array)
        print(result)
        self.assertEqual(expected, result)

    def test_sorted_is_sorted(self):
        expected = [2, 3, 10, 20]
        result = my_array.sort()
        self.assertEqual(expected, result)


"""
PART 9
TWO NUMBER SUM: 
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no to numbers sum up to the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array. You cannot add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers summing up to the target sum. 
Sample Input: numbers = [3, 5, -4 ,8, 11, 1, -1, 6]  target_sum = 10
Sample Output: [-1, 11] the numbers can be in any  order, it does not matter. 

"""



my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
my_target = 12


def sum_target(numbers, target):
    for i in range(len(my_numbers)):
        for j in range(i, len(my_numbers)):
            if my_numbers[i] + my_numbers[j] != target:
                result = []
            else:
                result = [my_numbers[i], my_numbers[j]]
                print(result)
                return result


sum_target(my_numbers, my_target)