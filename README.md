# Study Notes

### Purpose of this

It's important to keep the knowledge of CS basics alive. That way you're not 
caught off guard when new opportunities arise. This notebook will contain 
questions that I encountered from Leetcode, HackerRank and other places as well
as concepts that I've forgotten that need studying.

Hopefully this will also be good material for blog posts and revisions when needed.

### Structure

Each directory will contain a subject. If there is no directory for a certain 
subject then I haven't studied this subject at all.

### Handy Tools

Python is neat. This repo is 100% Python, so naturally I picked up some really great tools. 
Some I've used in the past and got re-introduced to as I'm building this repo. 

#### `zip`

`zip` is used to combine iterables into tuples.

```python
a = [1, 3]
b = [2, 4]
c, d = zip(a, b)

assert(c == (1, 2))
assert(d == (3, 4))
```

The reason why this is great to use for algorithm questions 
is because it allows you to quickly split arrays of the same
size into usable iterables.

A clean way to do this is using the `*` syntax as follows.

```python
intervals = [[10, 20], [1, 5], [50, 90]]
start_times, end_times = zip(*intervals)

assert(start_times == (10, 1, 50))
assert(end_times == (20, 5, 90))
```

Very clean :D

#### `all`

`all` is a clean way to verify if an iterable is all `True`. Basically `all` is a 
reducer that just uses the `and` operator.

```python
assert(all([True, True, True]) == True)
assert(all([True, True, False]) == False)
```

This could be a good way for finding out if something is sorted or not.

```python
array = [1, 5, 6, 7, -1]
n = len(array)
all([array[i-1] <= array[i] for i in range(1, n - 1)])
```

#### `sorted`

There is no replacing `sorted` as a utility. `sorted` uses a method 
called [Timsort](https://en.wikipedia.org/wiki/Timsort) which uses a 
hybrid of mergesort and insertion sort with space `O(N)`.

You can modify `sorted` by giving it a `key` function with a `lambda`.
For example, if you want to sort elements that are of type `TreeNode` 
you can extract the val in the lambda itself.

#### `enumerate`

`enumerate` is a simple function that gives a more convenient way of looping an array.
Instead of writing a typical `for i in range...` it gives you the index and the element.

```python
array = [1, -3, 5, -4]
for index, element in enumerate(array):
    print(index, element)

# Will return
# 0 1
# 1 -3
# 2 5
# 3 -4
```

#### `math.inf`

`math.inf` is a convenient way to get a number that is bigger than any other number.
This is a great way to start off min or max when you don't know what the range is for the input.

```python
import math
high = -math.inf
low = math.inf

array = [1, 2, 4, 5, 6]
for elem in array:
    high = max(high, elem)
    low = min(low, elem)
```

#### `ii, jj`

Some graph questions have a tedious iteration especially in an adjacency matrix question.
Instead of having a bunch of `if` conditions where each one moves a pointer once, a 
cleaner and less error-prone way would be to put all the places that the pointers will go
and then iterate through them.

```python
def visit_perpendicular(graph, i, j):
    """ Visit perpendicular nodes to node [i][j]"""
    for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        # do something
        graph[ii][jj] = 2
```

#### `defaultdict`

`defaultdict` allows you to define a special type of library that whenever accessed with a
key that doesn't exist, it initializes a value for it. This way you don't get any `KeyError`
exceptions as you're coding.

`defaultdict` takes a callable not a value for it to be called during initialization. 
For example, you can use `defaultdict(list)` to return a new `list` everytime the `dict` is accessed.
This especially useful for building graphs.

```python
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for node, neighbour in edges:
        graph[node].append(neighbour)
    return graph
```

#### `gen`

Generators in python are a great way to keep going without storing into a list.


#### `[::-1]`

Simple way to reverse a `list` or a `string`.