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
