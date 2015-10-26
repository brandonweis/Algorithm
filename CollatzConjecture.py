import time

"""
Take a positive integer, like 9, and apply the following rule:

If it's odd, multiply it by 3 and add 1
If it's even, divide it in half
For example, applying this rule to 9 yields (9 * 3) + 1 = 28

Apply this rule repeatedly and you'll create a chain:

9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
This particular chain hits 1 after 19 steps.

The Collatz conjecture says that all such chains will hit 1 eventually. Calling 1 the end of a chain, for what integer less than a million is the Collatz chain the longest?
"""

def getMaxStepCountOptimize (number, results):

    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1

        if 0 <= number-1 < len(results):
            steps += results[number-1]
            number = 1
        else:
            steps += 1

    return steps

def getMaxStepCount (number, results):

    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1

        steps += 1

    return steps

if __name__ == "__main__":
    rangeNum = 1000001

    # non-optimised algorithm
    results = [];
    start_time = time.time()
    for x in range(1, rangeNum):
        steps = getMaxStepCount(x, results)
        results.append(steps)

    x = results.index(max(results)) + 1
    elapsed_time = time.time() - start_time

    # find the max
    print 'result: ', x, 'in', elapsed_time


    # optimised algorithm
    results = [];
    start_time = time.time()
    for x in range(1, rangeNum):
        steps = getMaxStepCountOptimize(x, results)
        results.append(steps)

    x = results.index(max(results)) + 1
    elapsed_time = time.time() - start_time

    # find the max
    print 'optimised result: ', x, 'in', elapsed_time
