## Day 2 Notes

Ids are lines within a file given 3 sets of cubes which are separated via semicolon
- Remove unnecessary string until colon
- Split string by semicolon to determine the 3 sets of cubes
- Split each set of cube by the number and color given by comma
- Hashmap count each color to number within a set
- Once this has happened just compare between the given color,number values to determine if this is possible or not
- Impossible sets means entire game is not valid so can continue to next line / game

Finding the minimum number of color necessary between sets means finding the max possible for a specific color within a set.
- Perform the same split between game sets as in part 1
- Check for the max needed for sets
- Calculate the power and place into an array
- Sum the array at the end
