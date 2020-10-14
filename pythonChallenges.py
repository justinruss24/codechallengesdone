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

# Circle of Numbers
