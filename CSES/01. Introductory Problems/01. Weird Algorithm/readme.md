
# Weird Algorithm
> Original Source: [CSES - Weird Algorithm](https://cses.fi/problemset/task/1068)

## Description
Consider an algorithm that takes as input a positive integer $n$. If n is even, the algorithm divides it by two, and if $n$ is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until $n$ is one. For example, the sequence for $n=3$ is as follows:

$3→10→5→16→8→4→2→1$

Your task is to simulate the execution of the algorithm for a given value of $n$.

## I/O
### Input
The only input line contains an integer $n$.
### Output
Print a line that contains all values of $n$ during the algorithm.

## Constraints

| | |
|--|--|
|Time| $1.00s$ |
|Memory| $512$MB |
|Constraints| $$1\le n\le 10^{6} $$|

## Testcases
### test 1
Input:
```
3
```
output:

```
3 10 5 16 8 4 2 1
```
