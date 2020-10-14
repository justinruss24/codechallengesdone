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
