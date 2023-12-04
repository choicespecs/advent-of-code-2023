## Day 3 Notes

[Advent of Code 2023 Day 3](https://adventofcode.com/2023/day/3)

We are given a 2d array where we are finding numbers adjacent to symbols.
- defined symbols as any value that is not a digit and not '.'
- Numbers are found from left to right -> meaning we only need to search digit this way as well
- once a number is found we must just search every adjacent value that is surrounding the digit for a value not equal to '.' to accept that value

### Part 1
We should create a helper function to just simply parse and check whether a value is a symbol or not.
- We are only checking if a symbol is not '.' and not a digit

First, Iterate through the 2d array until the end of the row. If we can find a digit in the grid
- Iterate through until a digit is not found which means we will find our total digit (123, 23, 3)

Next, once we have now found a digit, we should also have the start, end column index that we have traversed to create this digit with this start index and end index, we just need to first see if the value before the number and after the number is a symbol or not equal to '.'

If this has not found a symbol we should next traverse through every single column from the row previously and the row next to check for a symbol

Continue on and repeat until the end of row has been traversed from j -> y

### Part 2

We now need to find gear ratios which are two numbers that are adjacent to a gear "*"

To find the two adjacent numbers to a gear we will create an array within n * n grid meaning each [n][n] value will be an array.

Once we find a "*" at [i][j] value within our grid, we will add this number to our array n * n grid. 

This means we can locate all the specific gear values at i,j and find whether the gears have length of 2 we can multiply those values and put them into our answer