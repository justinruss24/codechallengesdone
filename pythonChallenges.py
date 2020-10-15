# Add Two Digits

import math
# You are given a two-digit integer n. Return the sum of its digits.

def addTwoDigits(n):
    stringify = str(n)
    return int(stringify[0]) + int(stringify[1])
# Largest Number

# Given an integer n, return the largest number that contains exactly n digits.

def largestNumber(n):
    nines = "9" * n
    return int(nines)


# Candies

# n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. Individual pieces of candy cannot be split.

def candies(n, m):
    sameAmount = math.floor(m/n)
    return sameAmount * n

# Seats in Theater

# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

def seatsInTheater(nCols, nRows, col, row):
    seats = (nCols - col + 1) * (nRows - row)

    return seats


# Max Multiple

# Given a divisor and a bound, find the largest integer N such that:
# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.

def maxMultiple(divisor, bound):
    options = []

    for i in range(0, bound+1):
        if i % divisor == 0:
            options.append(i)

    return max(options)

# Circle of Numbers

# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).
# Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.


def circleOfNumbers(n, firstNumber):

    # radialOpp = (n/2) + firstNumber

    if firstNumber > (n/2):
        return firstNumber - (n/2)
    elif firstNumber == (n/2):
        return 0
    else:
        return (n/2) + firstNumber


# // check palindrome
# // Given the string, check if it is a palindrome.


def checkPalindrome(inputString):
    rev = ''.join(reversed(inputString))

    if inputString == rev:
        return True
    else:
        return False


# Adjacent Elements Product
# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def adjacentElementsProduct(inputArray):
    largest = []

    for i in range(0, len(inputArray)-1):
        holder = inputArray[i] * inputArray[i+1]
        largest.append(holder)
    return max(largest)

# shape area
# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3 - and 4-interesting polygons in the picture below.


def shapeArea(n):
    if n == 1:
        return 1
    else:
        return n**2 + (n-1)**2


# Make array consecutive 2
# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
    count = 0
    minVal = min(statues)
    maxVal = max(statues)

    for i in range(minVal, maxVal + 1):
        if i not in statues:
            count += 1
    return count

# Longest Palindrome

class Solution1:
    def longestPalindrome(self, s: str) -> int:
        # count the number of times each letter appears
        ltr_count = {}
        #iterate through string counting letters
        for ltr in s:
            #if we haven't seen the letter before
            if ltr not in ltr_count:
                ltr_count[ltr] = 1
            #if we have...
            else:
                ltr_count[ltr] += 1
        # initialize var for total letters we can add to palindrome
        max_length = 0
        # check count for each letter
        for count in ltr_count.values():
            # if letter count is even, we can add all of them
            # if it's the first odd count, we can still add all to allow for an extra middle letter
            if count % 2 == 0 or max_length % 2 == 0:
                max_length += count
            # if it's odd and we've already added a middle letter, we can add all but one
            else:
                max_length += count - 1
        return max_length

# Find the Town Judge


class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            # Quick response for small case
            return 1

        # first cell is dummy, just for the convenience of indexing start from 1 to N
        trust_score = [0 for _ in range(N+1)]

        for p1, p2 in trust:

            # decrease one point from p1 when p1 trusts other people
            trust_score[p1] -= 1

            # increase one point to p2 when p2 is trusted by others
            trust_score[p2] += 1

        for person in range(1, N+1):

            # town judge will be trusted by other N-1 people, and town judge trust nobody.
            if trust_score[person] == N-1:
                return person

        return -1

# Contains Duplicates

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False


# Remove Kth From End of LL

# Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def remove_kth_from_end(head, k):
    p1 = head
    p2 = head
    length = 1

    if k == 0:
        return head

    while p1.next:
        length += 1
        p1 = p1.next
        if length > k + 1:
            p2 = p2.next
    if length == k:
        return head.next
    else:
        p2.next = p2.next.next
        return head

# First Not Repeating Character

# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.


def first_not_repeating_character(s):
    visited = set()

    for i in range(len(s)):
        if s[i] not in visited:
            visited.add(s[i])
            if s.count(s[i]) == 1:
                return s[i]
    return "_"
