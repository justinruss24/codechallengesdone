// add
// Write a function that returns the sum of two numbers.

function add(param1, param2) {
    return param1 + param2
}

// Century From Year
// Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

function centuryFromYear(year) {
    // if year is 1-100 return 1
    // check if the year is a whole number or has decimals when divided by 100
    const results = (year / 100)

    if (year <= 100) {
        return 1
    } else if (Number.isInteger(results)) {
        return results
    } else {
        return Math.floor(results) + 1
    }

}



