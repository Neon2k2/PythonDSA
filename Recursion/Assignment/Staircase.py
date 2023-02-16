# A child is running up a staircase with N steps,
# and can hop either 1 step, 2 steps or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up to the stairs. 
# You need to return number of possible ways W.We can solve this problem recursively.
# Let's define a function count_ways that takes an integer n as input,
# and returns the number of ways a child can run up the stairs of n steps.

# If the child is already at the top (i.e., n = 0), 
# then there is only one way to climb the stairs: don't move (return 1).

# Otherwise, the child has three options: hop 1, 2 or 3 steps. 
#     We can count the number of ways by summing the number of ways
#     the child can climb the remaining steps after taking each of these steps.


def count_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


print(count_ways(int(input())))
