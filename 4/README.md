## Day 4 Notes

[Advent of Code 2023 Day 4](https://adventofcode.com/2023/day/4)

We have scratchcards in our problem part of the solution requires parsing the winning numbers and the numbers to check against.
- Remove unnecessary values from delimitters ':', '|'
- Split to get the winning number values and compare values.

### Part 1
We can place the winning numbers within a set. We can then iterate through the compare values and see if there is a winning number that exists,

Once we have the winning numbers found in our compare values, we can then find the power 2^(n-1) to find the solution. Since it would be 1 for the first match and doubled every single time afterwards. We can assume that for one value found we can use 2^0 and use that logic to find 2^1 (found two values) or 2^2 (found three values)

With these values we can just add them to a running total.

### Part 2
We can use similar logic within Part 1 to find the total punchcards. 

First, we need to find the total number of cards. This number we can create an array that should be initialized to 1.

Next, we should iterate through the cards in the same manner as Part 1, but once we find the winning numbers instead of finding the power as we did in Part 1, we should the winning counts to use as a index j for our array from our current card file found. We can add the cards found at cards[i] to cards[i + (j + 1)]