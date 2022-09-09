
# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).

while True:
    if input("Do you want to stop? ") == "yes":
        break

# Så længe if-statement er false, skal den blive ved med at gentage, 
# men så snart if-statement er true, skal den stoppe/break.
#
# You can also do this:
#ans=""
#while ans != "yes":
#    ans = input("Do you want to stop? ")