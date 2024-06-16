import pytest
def fib_fun(n):
    x, y = 1, 2 
    for i in range(n+1):
        yield x
        x, y = y, x + y

def test_func_test():
    a = 1
    assert a == 1

for item in fib_fun(10):
    print (item)



# Create a set using curly brackets
s1 = {1, 2, 3}

# Create a set using the set() constructor
s2 = set([1, 2, 3, 4])

# Print out sets
print(f"Set s1: {s1}")
print(f"Set s2: {s2}")

# Create two new sets
names1 = set(["Glory", "Tony", "Joel", "Dennis"])
names2 = set(["Morgan", "Joel", "Tony", "Emmanuel", "Diego"])

# Create a union of two sets using the union() method
names_union = names1.union(names2)

# Create a union of two sets using the | operator
names_union = names1 | names2

# Print out the resulting union
print(names_union)

diff_union = names2 - names1

print(diff_union)