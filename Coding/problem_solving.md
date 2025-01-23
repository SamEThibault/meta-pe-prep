# Problem Solving
1. Listen for clues, for example, if the interviewer mentions that 2 arrays are sorted and distinct, that's a clue that the optimal solution uses the fact that the arrays are sorted.
2. Draw an example of an input and output. Make sure the inputs are sufficiently large and generic.
3. Write down the brute force solution first, even if it doesn't work
4. Optimize before you start coding (sometimes you'll need to start coding the brute force solution first)
5. Walk through algorithm, ensure you know what you have to do before you start writing code for the solution
6. Code. Usually you don't actually compile and run it, but try your hardest to write good and correct code
7. Verification. Double check the runtime, space complexity, and edge cases. Think of this like a code review.

# Optimizing with BUD (Bottlenecks, Unnecessary work, Duplicated work)
1. Find bottlenecks, and find a way to optimize them.
2. Find unnecessary work, and eliminate it. For example, if you can eliminate a pass through an array, even though it might not change the time complexity of the algorithm, it's worth optimizing and can help avoid future passes later.
3. Try to reuse work. For example, if you're calculating the sum of an array multiple times, try to store the sum in a variable and reuse it.

# Optimizing with Space and Time
1. There are trade-offs between time and space complexity. Discuss these trade-offs with the interviewer.
2. Figure out Best Conceivable Runtime (BCR), given the nature of the problem, what is the best runtime you could possibly imagine getting? That's not necessarily the runtime you'll get, but it's a good goal to aim for. So if you can do something in O(N), and you know the BCR is O(nlogn), the that step won't matter, go for it.

# Optimizing with DIY (Do It Yourself)
- Come up with a good example (large and generic), then figure out the output yourself
- Reverse engineer your intuitive thought process, try to figure out how you got to the answer