import sys

# Read all the input into a string, spaces, newlines and all, but
# I remove the newlines since these are annoying to print...
x = sys.stdin.read().replace("\n", "")

count = {}
# Count the characters in `x`` and put the counts in `counts`.
# Your code goes here.

for i in range(len(x)):
    char=x[i]
    if char not in count:
        x[char]=1
    else:
        count[char]+=1


# Get the keys, i.e., the characters, in sorted order
# and print the count
for a in sorted(count):
    print(f"{a}: {count[a]}")
