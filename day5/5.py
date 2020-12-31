from sys import stdin
from string import ascii_lowercase, ascii_uppercase

def react(polymer, units):

    poly = polymer

    while any(pair in poly for pair in units):
    
        for pair in units:
            poly = poly.replace(pair, "")


    return poly

polymer = stdin.read()

pairs = set("".join(x) for x in list(zip(ascii_lowercase, ascii_uppercase)) + list(zip(ascii_uppercase, ascii_lowercase)))

# Part One
print(len(react(polymer, pairs)))


# Pair Two

best = 999999

for c in ascii_lowercase:

    substitution = polymer.replace(c, "").replace(c.upper(), "")
    if (result := len(react(substitution, pairs))) < best:
        best = result

print(best)