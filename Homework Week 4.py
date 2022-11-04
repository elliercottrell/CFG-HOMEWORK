"""
HOMEWORK WEEK 4

Two Sum
-------------------------------------------------------------------------------------------------------------------------
Given an array of integers - nums - and an integer - target - , return two numbers inside that array such that
they add up to target. You may assume that each input would have at least one solution, and you may not use the
same element twice.

You can return the answer in any order.

EXAMPLE 1:
---------------------------------------------------------------
Input: nums = [2,7,11,15], target = 9
Output: [2, 7]
Explanation: Because nums[0] + nums[1] == 9, we return [2, 7].

EXAMPLE 2:
---------------------------------------------------------------
Input: nums = [3,2,4], target = 6
Output: [2, 4]

EXAMPLE 3:
---------------------------------------------------------------
Input: nums = [3,3], target = 6
Output: [3, 3]

NOTES:
---------------------------------------------------------------
- An input MAY HAVE no two numbers at all (an empty one still counts as a solution)
    - in this case, return an empty array
- It's an array of integer numbers - these numbers are not necessarily distinct / unique
- Make sure to discuss your solution - what is the Big O Time & Space complexity?
    Was there anyway you could've done better or not? Why or why not? Justify.
"""


def two_sum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return [array[i], array[j]]
    return []


nums = [2, 7, 11, 15]
targetSum = 9

print(two_sum(nums, targetSum))


"""
This was the best solution I could find on my own. The idea being to loop through each element checking it against 
the other numbers, if two added together make the target, returning the two elements to an array, if none are found, 
an empty array is returned. 

While I believe this solution works, it is not the optimum solution as it is simplistic at best and it does not have 
the most efficient Time/Space Complexity. 

This solution would make O(1)for Space Complexity but O(n^2)for Time Complexity. 
The Space Complexity is good because it remains constant. Although the size of the array input can increase, it does 
not take up any more extra space inside the function.

Unfortunately the use of the nested For Loops drastically impacts the Time Complexity if/when a larger array is 
inputed. Due to the function repeatedly having to look through each number in the array and having to compare that 
with the other numbers to find a sum, the complexity will grow quadratically, and with a large array could take a 
substantial amount of time to complete (if at all). This makes the solution quite inefficient in Time Complexity. 

An interesting way to improve on this would be to use a hash map or dictionary data structure. This would mean that 
you could remove the use of a nested for loop by essentially storing already searched through values elsewhere to 
refer back to. This was not something I was able to implement without further research, as I could see what I would 
like to do, but was unable to make this work without help. This solution would implement a hash map to store each 
element of the input array as a key. An example of this would be something like the code below, but this is not 
complete either. The idea here would be to bring the time complexity down to O(n) which would be considerably better, 
however the hash map would change the Space Complexity to O(n) also. Overall this would be much more desirable even 
with the trade off of Space Complexity.

"""


def twoSumHashing(array, target):
    sums = []
    hash_table = {}

    for i in range(len(array)):
        hashed = target - array[i]
        if hashed in hash_table:
            print([array[i], hashed])
        hash_table[array[i]] = array[i]


nums = [4, 5, 1, 8]
target = 6

print(twoSumHashing(nums, target))

"""
I believe there is also a way this could be done with pointers and a binary search algorithm which would be 
something like O(n) even in the worst case, but this is not something which I have attempted to implement. 
"""