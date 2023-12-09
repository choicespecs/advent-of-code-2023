## Day 5 Notes

[Advent of Code 2023 Day 5](https://adventofcode.com/2023/day/5)

Given an input file, we need to parse seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location
- These parts are separated by two new lines (\n\n)
- Can separate and parse these separate maps. If we read the maps from the beginning to end of file, we can assume that once we complete one portion of the mapping we can simply move onto the next without keeping prior information from previous mapping

### Part 1
We know there is a mapping that is decided on (dest, src, range). Instead of iterating and creating a mapping for each block, we can work through with this equation

1. Seed = x
2. If we have a value of (45, 98, 2). If our seed x = 72. we cannot apply the mapping to this value since it does not apply to our range.
3. If we have the range value (45, 98, 2) and our seed is 99 we can apply this mapping (98, 99) -> can map to destination
4. If we have the range value (45, 98, 2) and our seed is 100 we cannot apply this mapping


With this logic we can apply this logic
- If we have seed x and have (dest a, src b, range c)
  - If x > b, then we cannot apply mapping and x = x
  - If x > b + c, then we cannot apply mapping and x = x
  - So if b  <= x <= b + c, then we can apply mapping.

Mapping then for (45, 98, 2) would be (98 = 45, 99 = 46). We can see that each mapping will be from a + i meaning i = 1,2,3,4...c. So we can simply mapping would be a + c = new map.

So from our seed x. If we can apply x to our mapping we must assume that the new mapping can be x - b (calculate the potential possible range that we must apply 98 = 0, 99 = 1) then we can apply this to our dest meaning our new mapping.

So to solve (we have our seeds x)
- Iterate through the ranges (dest a, src b, range c)
- If b <= x <= b + c, we can apply our mapping else we can assume x = x for the new mapping
  - If we can apply mapping, we must subtract x - b (get range to apply for dest a) then we can add a to new dest value.
- Iterate through all blocks and we can safely assume iterating from one block can be applied to next block until we reach final iteration.
