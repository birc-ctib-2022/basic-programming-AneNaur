
# Print the numbers described in the exercise

x = []
for i in range(10):
    x.append(i+1)
    print(" ".join([str(y)for y in x]))

# You can also do this:
#x = []
#for i in range(10):
#    x.append(str(i+1))
#    print(" ".join(x))
#
# You can apparently also do this:
#z = []
#for j in range(10):
#    z.append(j+1)
#    print(*z)
#
# Magic star:
# f(x,y,z)
# w=[1,2,3]
# f(w) wont work, because it puts all the numbers in the list into x.
# f(*w) works, because it puts the first number in w to x, and the second number to y, and the third number to z.