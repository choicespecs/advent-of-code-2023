## Day 2 Notes

[Advent of Code Day 2](https://adventofcode.com/2023/day/2)

### Part 1
Ids are lines within a file given 3 sets of cubes which are separated via semicolon. 
- Remove unnecessary string until colon
- Split string by semicolon to determine the 3 sets of cubes
- Split each set of cube by the number and color given by comma

Since we have parsed the amount to each specific set. 

First, we can count each color to number within a set and add it to a hashmap for that given set.

After we have perform all our counts for that set, we just compare between the limit color,number values to determine if this is possible or not 

If we have determined this is impossible that would mean the entire game is not valid so can continue to next line / game and not need to check any other ones.

### Part 2
Finding the minimum number of color necessary between sets means finding the max possible for a specific color within a set. 

First, we perform the same split between game sets as in part 1 

Afterwards, we need to check for the max needed for a color given all sets.

Once we have the maximum, we can calculate the power and place into an array 

After all powers have been found we can sum the array at the end
