## Day 1 Notes

[Advent of Code Day 1](https://adventofcode.com/2023/day/1)

### Part 1
Looking for first and last digits in a string means we can utilize a stack.
- First value is always first digit in our 2 digit number
- Last value collected should be the last digit.

First, Iterate through every single character within a string in a line.

Next, if we find a digit within the string we can simply add to our stack.

At the end of the stack we can simply check if the stack length is 1 or greater than 1.
- If one, we can make this our 2 digit number (1 = 11)
- If more than one, we can make our 2 digit number from our first and last value on stack.

### Part 2

We can use same logic we implemented in part 1, but we need to account for when words or strings can appear.
- Check if number string, "one", "two", etc... exists within a string
- Check using a key following character located at i in string to j value
- Once you find and verify that the value does exist and create digit to add to stack
- perform same calculation as part 1

First, we create a hashmap that should contain the string values of all the strings of numbers like "one", "two", etc...

Second, we do the same iteration but we also check from each index if the value can be found in our hashmap
- We compare the length of 3 for "one", "two", "six"
- we compare the length of 4 for "four", "five", "nine"
- we compare the length of 5 for "three", "seven", "eight"

If we find this value we can simply add this to our stack as well.

Perform the same calculation as part 1