
# Print the pattern

x = []
for i in range(5):
    x.append("*")
    print("".join([str(y)for y in x]))

for i in range(5):
    x.remove("*")
    print("".join([str(y)for y in x]))
